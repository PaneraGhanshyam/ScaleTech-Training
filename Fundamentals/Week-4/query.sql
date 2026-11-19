-- ============================================================
-- FOOD DELIVERY DATABASE: WEEK 3 SQL PRACTICE
-- Target: PostgreSQL / DBeaver
-- Run against: food_delivery_db, schema public
-- Uses the exact column names and enum values from the supplied DDL.
-- This file is read-only except for the clearly marked OPTIONAL
-- index statements and the optional no-order restaurant test row.
-- ============================================================

SET search_path TO public;

-- ------------------------------------------------------------
-- 0. QUICK SANITY CHECK: tables and row counts
-- ------------------------------------------------------------
SELECT 'customers' AS table_name, COUNT(*) AS rows FROM customers
UNION ALL SELECT 'addresses', COUNT(*) FROM addresses
UNION ALL SELECT 'restaurants', COUNT(*) FROM restaurants
UNION ALL SELECT 'restaurant_operating_hours', COUNT(*) FROM restaurant_operating_hours
UNION ALL SELECT 'menus', COUNT(*) FROM menus
UNION ALL SELECT 'menu_items', COUNT(*) FROM menu_items
UNION ALL SELECT 'delivery_partners', COUNT(*) FROM delivery_partners
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'order_address_history', COUNT(*) FROM order_address_history
UNION ALL SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL SELECT 'delivery_assignments', COUNT(*) FROM delivery_assignments
UNION ALL SELECT 'payments', COUNT(*) FROM payments
UNION ALL SELECT 'refunds', COUNT(*) FROM refunds
UNION ALL SELECT 'restaurant_reviews', COUNT(*) FROM restaurant_reviews
UNION ALL SELECT 'food_item_reviews', COUNT(*) FROM food_item_reviews
UNION ALL SELECT 'delivery_partner_reviews', COUNT(*) FROM delivery_partner_reviews
ORDER BY table_name;

-- ============================================================
-- REQUIRED TASK 1: A customer's complete order history
-- Example customer_id = 1. Change the ID to inspect another customer.
-- LATERAL aggregates line items so each order appears only once.
-- ============================================================
SELECT
    c.customer_id,
    c.full_name AS customer_name,
    o.order_id,
    r.name AS restaurant_name,
    o.status,
    o.placed_at,
    o.total_amount,
    COALESCE(item_list.items, 'No order items found') AS ordered_items
FROM customers AS c
JOIN orders AS o
    ON o.customer_id = c.customer_id
JOIN restaurants AS r
    ON r.restaurant_id = o.restaurant_id
LEFT JOIN LATERAL (
    SELECT STRING_AGG(
        oi.quantity::text || ' x ' || oi.item_name_snapshot,
        ', ' ORDER BY oi.order_item_id
    ) AS items
    FROM order_items AS oi
    WHERE oi.order_id = o.order_id
) AS item_list ON TRUE
WHERE c.customer_id = 1
ORDER BY o.placed_at DESC;

-- ============================================================
-- REQUIRED TASK 2: Most ordered food items
-- Definition: quantity_sold = SUM(quantity), not merely number of
-- order-item rows. item_name_snapshot is used because it preserves
-- the purchased name even when menu_items is later deleted/changed.
-- ============================================================
SELECT
    oi.item_name_snapshot AS item_name,
    SUM(oi.quantity) AS quantity_sold,
    COUNT(DISTINCT oi.order_id) AS number_of_orders_containing_item
FROM order_items AS oi
GROUP BY oi.item_name_snapshot
ORDER BY quantity_sold DESC, number_of_orders_containing_item DESC, item_name ASC
LIMIT 10;

-- Optional variation: most ordered items within each restaurant.
SELECT
    r.restaurant_id,
    r.name AS restaurant_name,
    oi.item_name_snapshot AS item_name,
    SUM(oi.quantity) AS quantity_sold,
    COUNT(DISTINCT oi.order_id) AS number_of_orders
FROM order_items AS oi
JOIN orders AS o
    ON o.order_id = oi.order_id
JOIN restaurants AS r
    ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name, oi.item_name_snapshot
ORDER BY r.name, quantity_sold DESC, oi.item_name_snapshot;

-- ============================================================
-- REQUIRED TASK 3: Restaurants that have never received an order
-- NOT EXISTS is an anti-join: return a restaurant only when no
-- matching order row exists. Cancelled orders still count as orders.
-- In the supplied seed data all four restaurants have orders, so
-- this query is expected to return ZERO rows until a new restaurant
-- without an order is added.
-- ============================================================
SELECT
    r.restaurant_id,
    r.name AS restaurant_name,
    r.city,
    r.is_active,
    r.is_accepting_orders
FROM restaurants AS r
WHERE NOT EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.restaurant_id = r.restaurant_id
)
ORDER BY r.name;

-- Optional test row (run only if you want the previous query to
-- return a result; skip if you do not want to change your seed data):
-- INSERT INTO restaurants
--     (name, address_line, city, state, pincode, is_active, is_accepting_orders)
-- VALUES
--     ('Demo Restaurant - No Orders', '100 Test Road', 'Ahmedabad',
--      'Gujarat', '380001', TRUE, FALSE);

-- ============================================================
-- REQUIRED TASK 4: Restaurant revenue / delivered food sales
-- Business definition used here:
--   food_sales_after_discount = subtotal - discount_amount
--   counted only for delivered orders.
-- This excludes delivery fees and tax because they are not food sales.
-- It does not subtract refunds because the schema does not record
-- which order component (food/tax/delivery) a refund relates to.
-- ============================================================
SELECT
    r.restaurant_id,
    r.name AS restaurant_name,
    COUNT(o.order_id) FILTER (WHERE o.status = 'delivered') AS delivered_orders,
    COALESCE(
        SUM(o.subtotal - o.discount_amount)
            FILTER (WHERE o.status = 'delivered'),
        0
    ) AS food_sales_after_discount
FROM restaurants AS r
LEFT JOIN orders AS o
    ON o.restaurant_id = r.restaurant_id
GROUP BY r.restaurant_id, r.name
ORDER BY food_sales_after_discount DESC;

-- Optional date-filtered revenue example for one restaurant.
-- The date range is inclusive at start and exclusive at end.
SELECT
    r.name AS restaurant_name,
    COUNT(*) AS delivered_orders,
    SUM(o.subtotal - o.discount_amount) AS food_sales_after_discount
FROM orders AS o
JOIN restaurants AS r ON r.restaurant_id = o.restaurant_id
WHERE o.restaurant_id = 1
  AND o.status = 'delivered'
  AND o.placed_at >= TIMESTAMPTZ '2026-11-01 00:00:00+05:30'
  AND o.placed_at <  TIMESTAMPTZ '2026-12-01 00:00:00+05:30'
GROUP BY r.restaurant_id, r.name;

-- ============================================================
-- REQUIRED TASK 5: Customers who ordered from multiple restaurants
-- Cancelled orders are excluded so the query counts non-cancelled
-- customer activity. Change/remove this filter if cancelled attempts
-- should also count as restaurant interactions in your reporting.
-- ============================================================
SELECT
    c.customer_id,
    c.full_name AS customer_name,
    COUNT(DISTINCT o.restaurant_id) AS different_restaurants_count,
    STRING_AGG(DISTINCT r.name, ', ' ORDER BY r.name) AS restaurants_ordered_from
FROM customers AS c
JOIN orders AS o
    ON o.customer_id = c.customer_id
JOIN restaurants AS r
    ON r.restaurant_id = o.restaurant_id
WHERE o.status <> 'cancelled'
GROUP BY c.customer_id, c.full_name
HAVING COUNT(DISTINCT o.restaurant_id) > 1
ORDER BY different_restaurants_count DESC, c.full_name;

-- ============================================================
-- REQUIRED TASK 6: Orders currently being delivered
-- In this schema, the order-level status is out_for_delivery and
-- the matching active assignment is picked_up (food collected).
-- ============================================================
SELECT
    o.order_id,
    c.full_name AS customer_name,
    r.name AS restaurant_name,
    o.delivery_address_snapshot ->> 'address_line' AS delivery_address,
    o.delivery_address_snapshot ->> 'city' AS delivery_city,
    dp.partner_id,
    dp.full_name AS delivery_partner,
    da.status AS assignment_status,
    da.picked_up_at
FROM orders AS o
JOIN customers AS c
    ON c.customer_id = o.customer_id
JOIN restaurants AS r
    ON r.restaurant_id = o.restaurant_id
JOIN delivery_assignments AS da
    ON da.order_id = o.order_id
   AND da.status = 'picked_up'
JOIN delivery_partners AS dp
    ON dp.partner_id = da.partner_id
WHERE o.status = 'out_for_delivery'
ORDER BY da.picked_up_at;

-- ============================================================
-- REQUIRED TASK 7: Most active delivery partners
-- Definition: successful completed deliveries, not offers or rejects.
-- Also show all assignments to distinguish workload from success.
-- LEFT JOIN keeps partners with zero assignments in the result.
-- ============================================================
SELECT
    dp.partner_id,
    dp.full_name AS delivery_partner,
    COUNT(da.assignment_id) AS total_assignment_attempts,
    COUNT(da.assignment_id) FILTER (WHERE da.status = 'delivered') AS completed_deliveries,
    COUNT(da.assignment_id) FILTER (WHERE da.status = 'rejected') AS rejected_assignments
FROM delivery_partners AS dp
LEFT JOIN delivery_assignments AS da
    ON da.partner_id = dp.partner_id
GROUP BY dp.partner_id, dp.full_name
ORDER BY completed_deliveries DESC, total_assignment_attempts DESC, dp.full_name;

-- ============================================================
-- ADDITIONAL TASK 8: Average restaurant ratings
-- ============================================================
SELECT
    r.restaurant_id,
    r.name AS restaurant_name,
    COUNT(rr.restaurant_review_id) AS review_count,
    ROUND(AVG(rr.rating)::numeric, 2) AS average_rating
FROM restaurants AS r
LEFT JOIN restaurant_reviews AS rr
    ON rr.restaurant_id = r.restaurant_id
GROUP BY r.restaurant_id, r.name
ORDER BY average_rating DESC NULLS LAST, review_count DESC;

-- ============================================================
-- ADDITIONAL TASK 9: Average rating for each food item
-- Review rows identify purchased order lines; use item snapshots
-- so the review can still be reported if its menu item is deleted.
-- ============================================================
SELECT
    oi.item_name_snapshot AS item_name,
    COUNT(fir.food_review_id) AS review_count,
    ROUND(AVG(fir.rating)::numeric, 2) AS average_rating
FROM order_items AS oi
JOIN food_item_reviews AS fir
    ON fir.order_item_id = oi.order_item_id
GROUP BY oi.item_name_snapshot
ORDER BY average_rating DESC, review_count DESC, item_name;

-- ============================================================
-- ADDITIONAL TASK 10: Average delivery-partner rating
-- ============================================================
SELECT
    dp.partner_id,
    dp.full_name AS delivery_partner,
    COUNT(dpr.delivery_review_id) AS review_count,
    ROUND(AVG(dpr.rating)::numeric, 2) AS average_rating
FROM delivery_partners AS dp
LEFT JOIN delivery_assignments AS da
    ON da.partner_id = dp.partner_id
LEFT JOIN delivery_partner_reviews AS dpr
    ON dpr.assignment_id = da.assignment_id
GROUP BY dp.partner_id, dp.full_name
ORDER BY average_rating DESC NULLS LAST, review_count DESC;

-- ============================================================
-- ADDITIONAL TASK 11: Pending payments that need reconciliation
-- ============================================================
SELECT
    p.payment_id,
    p.order_id,
    c.full_name AS customer_name,
    p.amount,
    p.payment_method,
    p.payment_provider,
    p.created_at
FROM payments AS p
JOIN orders AS o ON o.order_id = p.order_id
JOIN customers AS c ON c.customer_id = o.customer_id
WHERE p.status = 'pending'
ORDER BY p.created_at;

-- ============================================================
-- ADDITIONAL TASK 12: Refund totals by payment
-- Aggregate refunds before joining to avoid multiplying payment rows.
-- ============================================================
SELECT
    p.payment_id,
    p.order_id,
    p.amount AS payment_amount,
    COALESCE(SUM(rf.amount) FILTER (WHERE rf.status = 'succeeded'), 0) AS successful_refund_total,
    COALESCE(SUM(rf.amount) FILTER (WHERE rf.status = 'pending'), 0) AS pending_refund_total
FROM payments AS p
LEFT JOIN refunds AS rf ON rf.payment_id = p.payment_id
GROUP BY p.payment_id, p.order_id, p.amount
ORDER BY p.order_id, p.payment_id;

-- ============================================================
-- ADDITIONAL TASK 13: Orders with multiple payment attempts
-- ============================================================
SELECT
    o.order_id,
    c.full_name AS customer_name,
    COUNT(p.payment_id) AS payment_attempts,
    COUNT(p.payment_id) FILTER (WHERE p.status = 'succeeded') AS successful_attempts,
    COUNT(p.payment_id) FILTER (WHERE p.status = 'failed') AS failed_attempts
FROM orders AS o
JOIN customers AS c ON c.customer_id = o.customer_id
JOIN payments AS p ON p.order_id = o.order_id
GROUP BY o.order_id, c.full_name
HAVING COUNT(p.payment_id) > 1
ORDER BY payment_attempts DESC, o.order_id;

-- ============================================================
-- ADDITIONAL TASK 14: List published menus and currently orderable items
-- ============================================================
SELECT
    r.name AS restaurant_name,
    m.menu_name,
    mi.menu_item_id,
    mi.item_name,
    mi.price,
    mi.is_vegetarian
FROM restaurants AS r
JOIN menus AS m ON m.restaurant_id = r.restaurant_id
JOIN menu_items AS mi ON mi.menu_id = m.menu_id
WHERE r.is_active = TRUE
  AND r.is_accepting_orders = TRUE
  AND m.is_published = TRUE
  AND mi.is_available_for_order = TRUE
ORDER BY r.name, m.menu_name, mi.item_name;

-- ============================================================
-- OPTIONAL INDEX IMPROVEMENTS
-- The DDL ALREADY creates indexes for the main foreign-key joins and
-- several reports. These are additional, workload-dependent examples.
-- Run only after understanding the workload; don't index every field.
-- ============================================================

-- 1. Fast lookup of recently placed orders currently out for delivery.
-- CREATE INDEX IF NOT EXISTS idx_orders_out_for_delivery_recent
--     ON orders (placed_at DESC)
--     WHERE status = 'out_for_delivery';

-- 2. Fast partner-level reporting over completed deliveries only.
-- CREATE INDEX IF NOT EXISTS idx_assignments_delivered_partner
--     ON delivery_assignments (partner_id, completed_at DESC)
--     WHERE status = 'delivered';

-- 3. Find only eligible partners for dispatch. Useful when eligible
-- partners are a small subset of all registered delivery partners.
-- CREATE INDEX IF NOT EXISTS idx_delivery_partners_eligible
--     ON delivery_partners (partner_id)
--     WHERE is_active = TRUE
--       AND is_verified = TRUE
--       AND is_available_for_delivery = TRUE;

-- 4. Fast lookup of available menu items inside one menu. This can
-- help when many menu items are unavailable; test against real data.
-- CREATE INDEX IF NOT EXISTS idx_menu_items_available_by_menu
--     ON menu_items (menu_id, item_name)
--     WHERE is_available_for_order = TRUE;

-- 5. Restaurant discovery for a city, limited to restaurants that
-- are enabled and accepting orders. This is useful for city browsing.
-- CREATE INDEX IF NOT EXISTS idx_restaurants_city_accepting
--     ON restaurants (city, restaurant_id)
--     WHERE is_active = TRUE AND is_accepting_orders = TRUE;

-- BUSINESS-RULE INDEX (OPTIONAL):
-- If the platform allows each delivery partner only ONE active job
-- at a time, this unique partial index enforces that rule even when
-- two requests try assigning the same partner concurrently.
-- Do not create it if batching multiple deliveries per partner is allowed.
-- CREATE UNIQUE INDEX uq_assignments_one_active_per_partner
--     ON delivery_assignments (partner_id)
--     WHERE status IN ('offered', 'accepted', 'picked_up');

-- After creating indexes, refresh planner statistics:
-- ANALYZE;
