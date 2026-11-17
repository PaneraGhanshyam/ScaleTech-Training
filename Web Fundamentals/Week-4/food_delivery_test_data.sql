-- ============================================================
-- FOOD DELIVERY DATABASE: REALISTIC TEST / SEED DATA
-- Target: PostgreSQL, public schema
-- Run AFTER food_delivery_database_postgresql_fixed.sql
-- This script is intended for a freshly-created, empty schema.
-- It uses explicit IDs so the relationships are easy to inspect.
-- Run it ONCE. Do not rerun unless you first clear the seed data.
-- ============================================================

BEGIN;
SET LOCAL search_path TO public;

-- ------------------------------------------------------------
-- 1. CUSTOMERS (8 records: active and inactive accounts)
-- ------------------------------------------------------------
INSERT INTO customers
(customer_id, full_name, email, phone, is_active, created_at, updated_at)
VALUES
(1, 'Aarav Shah',       'aarav.shah@example.com',       '9876500001', TRUE,  '2026-08-10 09:00:00+05:30', '2026-11-10 09:00:00+05:30'),
(2, 'Diya Patel',       'diya.patel@example.com',       '9876500002', TRUE,  '2026-08-12 10:15:00+05:30', '2026-11-11 10:15:00+05:30'),
(3, 'Ishaan Mehta',     'ishaan.mehta@example.com',     '9876500003', TRUE,  '2026-08-15 11:30:00+05:30', '2026-11-12 11:30:00+05:30'),
(4, 'Kavya Desai',      'kavya.desai@example.com',      '9876500004', TRUE,  '2026-08-18 12:00:00+05:30', '2026-11-13 12:00:00+05:30'),
(5, 'Rohan Joshi',      'rohan.joshi@example.com',      '9876500005', TRUE,  '2026-08-20 13:20:00+05:30', '2026-11-14 13:20:00+05:30'),
(6, 'Ananya Trivedi',   'ananya.trivedi@example.com',   '9876500006', TRUE,  '2026-08-22 14:45:00+05:30', '2026-11-15 14:45:00+05:30'),
(7, 'Vivaan Rao',       'vivaan.rao@example.com',       '9876500007', TRUE,  '2026-08-25 16:00:00+05:30', '2026-11-16 16:00:00+05:30'),
(8, 'Myra Kulkarni',    'myra.kulkarni@example.com',    NULL,         FALSE, '2026-08-27 17:10:00+05:30', '2026-11-14 20:15:00+05:30');

-- ------------------------------------------------------------
-- 2. SAVED ADDRESSES (11 records; one default per customer)
-- ------------------------------------------------------------
INSERT INTO addresses
(address_id, customer_id, address_type, recipient_name, recipient_phone,
 address_line, landmark, city, state, pincode, is_default, created_at, updated_at)
VALUES
(1,  1, 'home',   'Aarav Shah',     '9876500001', 'B-204, Shantam Residency, Vastrapur', 'Near Alpha One Mall', 'Ahmedabad', 'Gujarat', '380015', TRUE,  '2026-08-10 09:10:00+05:30', '2026-08-10 09:10:00+05:30'),
(2,  1, 'work',   'Aarav Shah',     '9876500001', '4th Floor, Westgate Business Bay, SG Highway', 'Near YMCA Club', 'Ahmedabad', 'Gujarat', '380054', FALSE, '2026-08-10 09:15:00+05:30', '2026-08-10 09:15:00+05:30'),
(3,  2, 'home',   'Diya Patel',     '9876500002', 'A-301, Saffron Heights, Satellite', 'Near Shivranjani Cross Road', 'Ahmedabad', 'Gujarat', '380015', TRUE,  '2026-08-12 10:20:00+05:30', '2026-08-12 10:20:00+05:30'),
(4,  3, 'home',   'Ishaan Mehta',   '9876500003', 'C-12, Maple County, Thaltej', 'Near Zydus Hospital', 'Ahmedabad', 'Gujarat', '380059', TRUE,  '2026-08-15 11:40:00+05:30', '2026-08-15 11:40:00+05:30'),
(5,  4, 'home',   'Kavya Desai',    '9876500004', '702, Orchid Elegance, Bodakdev', 'Near Iscon Cross Road', 'Ahmedabad', 'Gujarat', '380054', TRUE,  '2026-08-18 12:10:00+05:30', '2026-08-18 12:10:00+05:30'),
(6,  5, 'home',   'Rohan Joshi',    '9876500005', 'A-7, Shreeji Apartments, Maninagar', 'Near Maninagar Railway Station', 'Ahmedabad', 'Gujarat', '380008', TRUE,  '2026-08-20 13:30:00+05:30', '2026-08-20 13:30:00+05:30'),
(7,  6, 'home',   'Ananya Trivedi', '9876500006', '16, Prernatirth Derasar Road, Jodhpur', 'Near Jodhpur Cross Road', 'Ahmedabad', 'Gujarat', '380015', TRUE,  '2026-08-22 14:50:00+05:30', '2026-08-22 14:50:00+05:30'),
(8,  7, 'home',   'Vivaan Rao',     '9876500007', 'B-5, Satyam Enclave, Naranpura', 'Near Naranpura Railway Crossing', 'Ahmedabad', 'Gujarat', '380013', TRUE,  '2026-08-25 16:10:00+05:30', '2026-08-25 16:10:00+05:30'),
(9,  8, 'home',   'Myra Kulkarni',  '9876500008', '503, Riverfront Residency, Paldi', NULL, 'Ahmedabad', 'Gujarat', '380007', TRUE,  '2026-08-27 17:20:00+05:30', '2026-08-27 17:20:00+05:30'),
(10, 4, 'work',   'Kavya Desai',    '9876500004', '2nd Floor, Commerce House, Navrangpura', 'Near Swastik Cross Road', 'Ahmedabad', 'Gujarat', '380009', FALSE, '2026-09-01 08:30:00+05:30', '2026-09-01 08:30:00+05:30'),
(11, 5, 'family', 'Rohan Joshi',    '9876500005', '12, Shivalik Bunglows, Chandkheda', 'Near IOC Road', 'Ahmedabad', 'Gujarat', '382424', FALSE, '2026-09-05 18:00:00+05:30', '2026-09-05 18:00:00+05:30');

-- ------------------------------------------------------------
-- 3. RESTAURANTS (4 records; status combinations covered)
-- ------------------------------------------------------------
INSERT INTO restaurants
(restaurant_id, name, description, email, phone, address_line, city, state, pincode,
 business_timezone, is_active, is_accepting_orders, created_at, updated_at)
VALUES
(1, 'Tasty Gujarat Kitchen', 'Authentic Gujarati and Kathiyawadi meals made fresh.', 'hello@tastygujarat.example', '07940001001', 'Shop 12, Himalaya Mall Road, Vastrapur', 'Ahmedabad', 'Gujarat', '380015', 'Asia/Kolkata', TRUE, TRUE,  '2026-07-01 08:00:00+05:30', '2026-11-16 08:00:00+05:30'),
(2, 'Urban Tandoor House', 'North Indian grills, curries and biryani.', 'orders@urbantandoor.example', '07940001002', 'Ground Floor, Swastik Plaza, Navrangpura', 'Ahmedabad', 'Gujarat', '380009', 'Asia/Kolkata', FALSE, FALSE, '2026-07-05 09:00:00+05:30', '2026-11-17 08:20:00+05:30'),
(3, 'Green Bowl Kitchen', 'Healthy bowls, salads and balanced meals.', 'care@greenbowl.example', '07940001003', 'Gala Business Centre, Prahlad Nagar', 'Ahmedabad', 'Gujarat', '380015', 'Asia/Kolkata', TRUE, TRUE,  '2026-07-10 10:00:00+05:30', '2026-11-16 10:00:00+05:30'),
(4, 'Coastal Spice', 'Coastal Indian seafood and regional specialities.', 'contact@coastalspice.example', '07940001004', 'Satellite Road, Anand Nagar', 'Ahmedabad', 'Gujarat', '380015', 'Asia/Kolkata', TRUE, FALSE, '2026-07-15 11:00:00+05:30', '2026-11-17 08:59:00+05:30');

-- ------------------------------------------------------------
-- 4. RESTAURANT OPERATING HOURS
-- Demonstrates all 7 weekdays, split lunch/dinner slots and closed days.
-- ------------------------------------------------------------
INSERT INTO restaurant_operating_hours
(operating_hours_id, restaurant_id, day_of_week, slot_number, opens_at, closes_at, is_closed)
VALUES
-- Restaurant 1: lunch and dinner every day
(1, 1, 'monday',    1, '11:00', '15:00', FALSE), (2, 1, 'monday',    2, '19:00', '23:00', FALSE),
(3, 1, 'tuesday',   1, '11:00', '15:00', FALSE), (4, 1, 'tuesday',   2, '19:00', '23:00', FALSE),
(5, 1, 'wednesday',1, '11:00', '15:00', FALSE), (6, 1, 'wednesday',2, '19:00', '23:00', FALSE),
(7, 1, 'thursday',  1, '11:00', '15:00', FALSE), (8, 1, 'thursday',  2, '19:00', '23:00', FALSE),
(9, 1, 'friday',    1, '11:00', '15:00', FALSE), (10,1, 'friday',    2, '19:00', '23:30', FALSE),
(11,1, 'saturday',  1, '11:00', '15:30', FALSE), (12,1, 'saturday',  2, '19:00', '23:30', FALSE),
(13,1, 'sunday',    1, '11:00', '15:30', FALSE), (14,1, 'sunday',    2, '19:00', '23:00', FALSE),
-- Restaurant 2: lunch and dinner Monday-Saturday; closed Sunday
(15,2, 'monday',    1, '12:00', '15:30', FALSE), (16,2, 'monday',    2, '19:00', '23:00', FALSE),
(17,2, 'tuesday',   1, '12:00', '15:30', FALSE), (18,2, 'tuesday',   2, '19:00', '23:00', FALSE),
(19,2, 'wednesday',1, '12:00', '15:30', FALSE), (20,2, 'wednesday',2, '19:00', '23:00', FALSE),
(21,2, 'thursday',  1, '12:00', '15:30', FALSE), (22,2, 'thursday',  2, '19:00', '23:00', FALSE),
(23,2, 'friday',    1, '12:00', '15:30', FALSE), (24,2, 'friday',    2, '19:00', '23:30', FALSE),
(25,2, 'saturday',  1, '12:00', '16:00', FALSE), (26,2, 'saturday',  2, '19:00', '23:30', FALSE),
(27,2, 'sunday',    1, NULL,    NULL,    TRUE),
-- Restaurant 3: one continuous daily service; closed Monday
(28,3, 'monday',    1, NULL,    NULL,    TRUE),
(29,3, 'tuesday',   1, '10:00', '22:00', FALSE),
(30,3, 'wednesday',1, '10:00', '22:00', FALSE),
(31,3, 'thursday',  1, '10:00', '22:00', FALSE),
(32,3, 'friday',    1, '10:00', '22:00', FALSE),
(33,3, 'saturday',  1, '10:00', '22:00', FALSE),
(34,3, 'sunday',    1, '10:00', '21:00', FALSE),
-- Restaurant 4: lunch/dinner, closed Tuesday (restaurant currently inactive)
(35,4, 'monday',    1, '11:30', '15:00', FALSE), (36,4, 'monday',    2, '19:00', '22:30', FALSE),
(37,4, 'tuesday',   1, NULL,    NULL,    TRUE),
(38,4, 'wednesday',1, '11:30', '15:00', FALSE), (39,4, 'wednesday',2, '19:00', '22:30', FALSE),
(40,4, 'thursday',  1, '11:30', '15:00', FALSE), (41,4, 'thursday',  2, '19:00', '22:30', FALSE),
(42,4, 'friday',    1, '11:30', '15:00', FALSE), (43,4, 'friday',    2, '19:00', '23:00', FALSE),
(44,4, 'saturday',  1, '11:30', '15:30', FALSE), (45,4, 'saturday',  2, '19:00', '23:00', FALSE),
(46,4, 'sunday',    1, '11:30', '15:30', FALSE), (47,4, 'sunday',    2, '19:00', '22:30', FALSE);

-- ------------------------------------------------------------
-- 5. MENUS (published and unpublished examples)
-- ------------------------------------------------------------
INSERT INTO menus
(menu_id, restaurant_id, menu_name, description, is_published, created_at, updated_at)
VALUES
(1, 1, 'Gujarati Main Course', 'Thalis, breads and traditional curries.', TRUE,  '2026-07-01 08:30:00+05:30', '2026-11-10 08:30:00+05:30'),
(2, 1, 'Beverages',            'Traditional drinks and coolers.', TRUE,  '2026-07-01 08:35:00+05:30', '2026-11-10 08:35:00+05:30'),
(3, 2, 'Tandoor and North Indian', 'Tandoori starters, curries and rice.', TRUE, '2026-07-05 09:30:00+05:30', '2026-11-10 09:30:00+05:30'),
(4, 3, 'Healthy Meals',       'Salads, bowls and lighter meals.', TRUE,  '2026-07-10 10:30:00+05:30', '2026-11-10 10:30:00+05:30'),
(5, 4, 'Coastal Specials',    'Seafood and coastal accompaniments.', FALSE, '2026-07-15 11:30:00+05:30', '2026-11-01 11:30:00+05:30');

-- ------------------------------------------------------------
-- 6. MENU ITEMS (vegetarian/non-vegetarian and available/unavailable)
-- ------------------------------------------------------------
INSERT INTO menu_items
(menu_item_id, menu_id, item_name, description, price, is_vegetarian, is_available_for_order, created_at, updated_at)
VALUES
(1,  1, 'Gujarati Unlimited Thali', 'Seasonal vegetables, dal, rice, roti and farsan.', 249.00, TRUE,  TRUE,  '2026-07-01 09:00:00+05:30', '2026-11-10 09:00:00+05:30'),
(2,  1, 'Kathiyawadi Thali',        'Traditional spicy Kathiyawadi meal.',              289.00, TRUE,  TRUE,  '2026-07-01 09:05:00+05:30', '2026-11-10 09:05:00+05:30'),
(3,  1, 'Paneer Butter Masala',    'Paneer in a rich tomato and butter gravy.',        220.00, TRUE,  TRUE,  '2026-07-01 09:10:00+05:30', '2026-11-10 09:10:00+05:30'),
(4,  1, 'Butter Naan',              'Tandoor-baked naan finished with butter.',          40.00, TRUE,  TRUE,  '2026-07-01 09:15:00+05:30', '2026-11-10 09:15:00+05:30'),
(5,  1, 'Masala Chaas',             'Chilled spiced buttermilk.',                        35.00, TRUE,  TRUE,  '2026-07-01 09:20:00+05:30', '2026-11-10 09:20:00+05:30'),
(6,  2, 'Mango Lassi',              'Yoghurt drink with mango pulp.',                    70.00, TRUE,  TRUE,  '2026-07-01 09:25:00+05:30', '2026-11-10 09:25:00+05:30'),
(7,  3, 'Chicken Tikka',            'Charcoal-grilled chicken tikka.',                  280.00, FALSE, TRUE,  '2026-07-05 10:00:00+05:30', '2026-11-10 10:00:00+05:30'),
(8,  3, 'Paneer Tikka',             'Marinated paneer grilled in a tandoor.',           210.00, TRUE,  TRUE,  '2026-07-05 10:05:00+05:30', '2026-11-10 10:05:00+05:30'),
(9,  3, 'Chicken Biryani',          'Aromatic basmati rice with chicken and spices.',   260.00, FALSE, TRUE,  '2026-07-05 10:10:00+05:30', '2026-11-10 10:10:00+05:30'),
(10, 3, 'Dal Makhani',              'Slow-cooked black lentils with cream.',            190.00, TRUE,  TRUE,  '2026-07-05 10:15:00+05:30', '2026-11-10 10:15:00+05:30'),
(11, 4, 'Quinoa Buddha Bowl',      'Quinoa, roasted vegetables and house dressing.',  220.00, TRUE,  TRUE,  '2026-07-10 11:00:00+05:30', '2026-11-10 11:00:00+05:30'),
(12, 4, 'Grilled Paneer Salad',    'Grilled paneer with greens and citrus dressing.', 180.00, TRUE,  TRUE,  '2026-07-10 11:05:00+05:30', '2026-11-10 11:05:00+05:30'),
(13, 4, 'Sprout Salad',             'Fresh sprouts, vegetables and lemon.',              130.00, TRUE,  TRUE,  '2026-07-10 11:10:00+05:30', '2026-11-10 11:10:00+05:30'),
(14, 4, 'Cold Coffee',              'Chilled coffee with milk.',                         110.00, TRUE,  FALSE, '2026-07-10 11:15:00+05:30', '2026-11-16 11:15:00+05:30'),
(15, 5, 'Prawn Masala',             'Prawns cooked in coastal masala.',                  390.00, FALSE, TRUE,  '2026-07-15 12:00:00+05:30', '2026-11-01 12:00:00+05:30'),
(16, 5, 'Fish Curry',              'Fish simmered in coconut-based curry.',            320.00, FALSE, TRUE,  '2026-07-15 12:05:00+05:30', '2026-11-01 12:05:00+05:30'),
(17, 5, 'Steamed Rice',             'Steamed basmati rice.',                              80.00, TRUE,  TRUE,  '2026-07-15 12:10:00+05:30', '2026-11-01 12:10:00+05:30'),
(18, 5, 'Sol Kadhi',                'Kokum and coconut milk digestive drink.',           60.00, TRUE,  TRUE,  '2026-07-15 12:15:00+05:30', '2026-11-01 12:15:00+05:30');

-- ------------------------------------------------------------
-- 7. DELIVERY PARTNERS (all vehicle types and account states)
-- ------------------------------------------------------------
INSERT INTO delivery_partners
(partner_id, full_name, phone, email, vehicle_type, vehicle_model, vehicle_registration_number,
 is_verified, is_available_for_delivery, is_active, last_known_latitude, last_known_longitude,
 last_location_updated_at, total_deliveries, created_at, updated_at)
VALUES
(1, 'Manish Parmar',  '9876510001', 'manish.parmar@example.com',  'motorcycle', 'Hero Splendor Plus', 'GJ01AB1234', TRUE,  FALSE, TRUE,  23.0396, 72.5301, '2026-11-17 08:30:00+05:30', 1, '2026-08-01 08:00:00+05:30', '2026-11-17 08:30:00+05:30'),
(2, 'Nikhil Solanki', '9876510002', 'nikhil.solanki@example.com', 'scooter',    'TVS Jupiter',        'GJ01CD5678', TRUE,  TRUE,  TRUE,  23.0305, 72.5590, '2026-11-17 08:32:00+05:30', 2, '2026-08-02 08:00:00+05:30', '2026-11-17 08:32:00+05:30'),
(3, 'Jatin Chauhan',  '9876510003', 'jatin.chauhan@example.com', 'bicycle',    'Firefox Road Runner',NULL,         TRUE,  TRUE,  TRUE,  23.0225, 72.5714, '2026-11-17 08:25:00+05:30', 1, '2026-08-03 08:00:00+05:30', '2026-11-17 08:25:00+05:30'),
(4, 'Sahil Khan',     '9876510004', 'sahil.khan@example.com',    'car',        'Maruti WagonR',      'GJ01EF9012', TRUE,  FALSE, TRUE,  23.0120, 72.5100, '2026-11-17 08:40:00+05:30', 0, '2026-08-04 08:00:00+05:30', '2026-11-17 08:40:00+05:30'),
(5, 'Parth Makwana',  '9876510005', 'parth.makwana@example.com', 'other',      'Electric Cargo Trike','GJ01GH3456', TRUE,  FALSE, TRUE, NULL,    NULL,    NULL,                                1, '2026-08-05 08:00:00+05:30', '2026-11-10 08:00:00+05:30'),
(6, 'Kunal Shah',     '9876510006', 'kunal.shah@example.com',    'motorcycle', 'Honda Activa 6G',    'GJ01JK7890', FALSE, FALSE, FALSE, 23.0700, 72.5200, '2026-11-01 19:00:00+05:30', 0, '2026-08-06 08:00:00+05:30', '2026-11-01 19:00:00+05:30');

-- ------------------------------------------------------------
-- 8. ORDERS (all order_status enum values represented)
-- Totals are calculated as subtotal + delivery_fee + tax - discount.
-- ------------------------------------------------------------
INSERT INTO orders
(order_id, customer_id, restaurant_id, selected_address_id, delivery_address_snapshot,
 subtotal, delivery_fee, tax_amount, discount_amount, total_amount, currency, status,
 special_instructions, cancellation_reason, placed_at, confirmed_at, delivered_at,
 cancelled_at, delivery_address_changed_at)
VALUES
(1, 1, 1, 1,
 '{"recipient_name":"Aarav Shah","recipient_phone":"9876500001","address_line":"B-204, Shantam Residency, Vastrapur","landmark":"Near Alpha One Mall","city":"Ahmedabad","state":"Gujarat","pincode":"380015"}'::jsonb,
 324.00, 30.00, 16.20, 20.00, 350.20, 'INR', 'delivered', 'Please pack the chaas separately.', NULL, '2026-11-10 12:05:00+05:30', '2026-11-10 12:07:00+05:30', '2026-11-10 12:52:00+05:30', NULL, NULL),
(2, 2, 2, 3,
 '{"recipient_name":"Diya Patel","recipient_phone":"9876500002","address_line":"A-301, Saffron Heights, Satellite","landmark":"Near Shivranjani Cross Road","city":"Ahmedabad","state":"Gujarat","pincode":"380015"}'::jsonb,
 540.00, 25.00, 27.00, 0.00, 592.00, 'INR', 'delivered', 'Less spicy, please.', NULL, '2026-11-11 19:10:00+05:30', '2026-11-11 19:12:00+05:30', '2026-11-11 20:00:00+05:30', NULL, NULL),
(3, 3, 3, 4,
 '{"recipient_name":"Ishaan Mehta","recipient_phone":"9876500003","address_line":"C-12, Maple County, Thaltej","landmark":"Near Zydus Hospital","city":"Ahmedabad","state":"Gujarat","pincode":"380059"}'::jsonb,
 400.00, 20.00, 20.00, 40.00, 400.00, 'INR', 'delivered', 'No disposable cutlery.', NULL, '2026-11-12 13:00:00+05:30', '2026-11-12 13:02:00+05:30', '2026-11-12 13:45:00+05:30', NULL, NULL),
(4, 1, 4, 2,
 '{"recipient_name":"Aarav Shah","recipient_phone":"9876500001","address_line":"22, Shilaj Road, near Shilaj Circle","landmark":"Call on arrival","city":"Ahmedabad","state":"Gujarat","pincode":"380059"}'::jsonb,
 460.00, 25.00, 23.00, 10.00, 498.00, 'INR', 'out_for_delivery', 'Please call before reaching.', NULL, '2026-11-17 07:45:00+05:30', '2026-11-17 07:47:00+05:30', NULL, NULL, '2026-11-17 08:00:00+05:30'),
(5, 4, 1, 5,
 '{"recipient_name":"Kavya Desai","recipient_phone":"9876500004","address_line":"702, Orchid Elegance, Bodakdev","landmark":"Near Iscon Cross Road","city":"Ahmedabad","state":"Gujarat","pincode":"380054"}'::jsonb,
 429.00, 30.00, 21.45, 0.00, 480.45, 'INR', 'ready_for_pickup', 'Keep the lassi chilled.', NULL, '2026-11-17 08:05:00+05:30', '2026-11-17 08:07:00+05:30', NULL, NULL, NULL),
(6, 5, 2, 6,
 '{"recipient_name":"Rohan Joshi","recipient_phone":"9876500005","address_line":"A-7, Shreeji Apartments, Maninagar","landmark":"Near Maninagar Railway Station","city":"Ahmedabad","state":"Gujarat","pincode":"380008"}'::jsonb,
 540.00, 25.00, 27.00, 0.00, 592.00, 'INR', 'preparing', 'Pack biryani and starter separately.', NULL, '2026-11-17 08:15:00+05:30', '2026-11-17 08:17:00+05:30', NULL, NULL, NULL),
(7, 6, 3, 7,
 '{"recipient_name":"Ananya Trivedi","recipient_phone":"9876500006","address_line":"16, Prernatirth Derasar Road, Jodhpur","landmark":"Near Jodhpur Cross Road","city":"Ahmedabad","state":"Gujarat","pincode":"380015"}'::jsonb,
 350.00, 20.00, 17.50, 0.00, 387.50, 'INR', 'confirmed', 'Dressing on the side.', NULL, '2026-11-16 20:10:00+05:30', '2026-11-16 20:12:00+05:30', NULL, NULL, NULL),
(8, 2, 4, 3,
 '{"recipient_name":"Diya Patel","recipient_phone":"9876500002","address_line":"A-301, Saffron Heights, Satellite, Tower B","landmark":"Security gate, Tower B","city":"Ahmedabad","state":"Gujarat","pincode":"380015"}'::jsonb,
 450.00, 25.00, 22.50, 50.00, 447.50, 'INR', 'placed', 'Ring the bell once.', NULL, '2026-11-17 08:50:00+05:30', NULL, NULL, NULL, '2026-11-17 08:55:00+05:30'),
(9, 7, 1, 8,
 '{"recipient_name":"Vivaan Rao","recipient_phone":"9876500007","address_line":"B-5, Satyam Enclave, Naranpura","landmark":"Near Naranpura Railway Crossing","city":"Ahmedabad","state":"Gujarat","pincode":"380013"}'::jsonb,
 284.00, 25.00, 14.20, 0.00, 323.20, 'INR', 'cancelled', 'Customer requested cancellation.', 'Customer cancelled before restaurant preparation.', '2026-11-15 18:20:00+05:30', '2026-11-15 18:22:00+05:30', NULL, '2026-11-15 18:25:00+05:30', NULL),
(10, 8, 3, NULL,
 '{"recipient_name":"Myra Kulkarni","recipient_phone":"9876500008","address_line":"503, Riverfront Residency, Paldi","city":"Ahmedabad","state":"Gujarat","pincode":"380007"}'::jsonb,
 180.00, 20.00, 9.00, 0.00, 209.00, 'INR', 'cancelled', NULL, 'Restaurant could not fulfil the order.', '2026-11-14 20:00:00+05:30', '2026-11-14 20:02:00+05:30', NULL, '2026-11-14 20:10:00+05:30', NULL),
(11, 3, 4, 4,
 '{"recipient_name":"Ishaan Mehta","recipient_phone":"9876500003","address_line":"C-12, Maple County, Thaltej","landmark":"Near Zydus Hospital","city":"Ahmedabad","state":"Gujarat","pincode":"380059"}'::jsonb,
 460.00, 25.00, 23.00, 20.00, 488.00, 'INR', 'delivered', NULL, NULL, '2026-11-13 19:00:00+05:30', '2026-11-13 19:02:00+05:30', '2026-11-13 19:50:00+05:30', NULL, NULL),
(12, 5, 1, 6,
 '{"recipient_name":"Rohan Joshi","recipient_phone":"9876500005","address_line":"A-7, Shreeji Apartments, Maninagar","landmark":"Near Maninagar Railway Station","city":"Ahmedabad","state":"Gujarat","pincode":"380008"}'::jsonb,
 330.00, 25.00, 16.50, 0.00, 371.50, 'INR', 'delivered', 'No onion in paneer gravy.', NULL, '2026-11-16 13:15:00+05:30', '2026-11-16 13:17:00+05:30', '2026-11-16 14:00:00+05:30', NULL, NULL);

-- ------------------------------------------------------------
-- 9. ORDER ADDRESS HISTORY (address changed before dispatch)
-- The current JSON snapshot on order 4 / 8 is the new address.
-- ------------------------------------------------------------
INSERT INTO order_address_history
(address_history_id, order_id, previous_address_snapshot, new_address_snapshot, change_reason, changed_at)
VALUES
(1, 4,
 '{"recipient_name":"Aarav Shah","recipient_phone":"9876500001","address_line":"4th Floor, Westgate Business Bay, SG Highway","landmark":"Near YMCA Club","city":"Ahmedabad","state":"Gujarat","pincode":"380054"}'::jsonb,
 '{"recipient_name":"Aarav Shah","recipient_phone":"9876500001","address_line":"22, Shilaj Road, near Shilaj Circle","landmark":"Call on arrival","city":"Ahmedabad","state":"Gujarat","pincode":"380059"}'::jsonb,
 'Customer changed the delivery destination before dispatch.', '2026-11-17 08:00:00+05:30'),
(2, 8,
 '{"recipient_name":"Diya Patel","recipient_phone":"9876500002","address_line":"A-301, Saffron Heights, Satellite","landmark":"Near Shivranjani Cross Road","city":"Ahmedabad","state":"Gujarat","pincode":"380015"}'::jsonb,
 '{"recipient_name":"Diya Patel","recipient_phone":"9876500002","address_line":"A-301, Saffron Heights, Satellite, Tower B","landmark":"Security gate, Tower B","city":"Ahmedabad","state":"Gujarat","pincode":"380015"}'::jsonb,
 'Customer added tower and gate details.', '2026-11-17 08:55:00+05:30');

-- ------------------------------------------------------------
-- 10. ORDER ITEMS (27 lines; includes quantity > 1 and a null menu_item_id snapshot)
-- ------------------------------------------------------------
INSERT INTO order_items
(order_item_id, order_id, menu_item_id, item_name_snapshot, quantity, unit_price_at_purchase, special_instructions, created_at)
VALUES
(1,  1, 1,  'Gujarati Unlimited Thali', 1, 249.00, 'Regular spice level.', '2026-11-10 12:06:00+05:30'),
(2,  1, 4,  'Butter Naan',              1,  40.00, NULL, '2026-11-10 12:06:00+05:30'),
(3,  1, NULL, 'Masala Chaas',             1,  35.00, 'Original menu item was removed; purchased item snapshot is retained.', '2026-11-10 12:06:00+05:30'),
(4,  2, 7,  'Chicken Tikka',            1, 280.00, 'Medium spicy.', '2026-11-11 19:11:00+05:30'),
(5,  2, 9,  'Chicken Biryani',          1, 260.00, NULL, '2026-11-11 19:11:00+05:30'),
(6,  3, 11, 'Quinoa Buddha Bowl',       1, 220.00, 'Dressing on the side.', '2026-11-12 13:01:00+05:30'),
(7,  3, 12, 'Grilled Paneer Salad',     1, 180.00, NULL, '2026-11-12 13:01:00+05:30'),
(8,  4, 16, 'Fish Curry',               1, 320.00, NULL, '2026-11-17 07:46:00+05:30'),
(9,  4, 17, 'Steamed Rice',             1,  80.00, NULL, '2026-11-17 07:46:00+05:30'),
(10, 4, 18, 'Sol Kadhi',                1,  60.00, 'Keep chilled.', '2026-11-17 07:46:00+05:30'),
(11, 5, 2,  'Kathiyawadi Thali',        1, 289.00, 'Medium spice.', '2026-11-17 08:06:00+05:30'),
(12, 5, 6,  'Mango Lassi',              2,  70.00, 'Keep chilled.', '2026-11-17 08:06:00+05:30'),
(13, 6, 7,  'Chicken Tikka',            1, 280.00, NULL, '2026-11-17 08:16:00+05:30'),
(14, 6, 9,  'Chicken Biryani',          1, 260.00, NULL, '2026-11-17 08:16:00+05:30'),
(15, 7, 11, 'Quinoa Buddha Bowl',       1, 220.00, 'Dressing on the side.', '2026-11-16 20:11:00+05:30'),
(16, 7, 13, 'Sprout Salad',             1, 130.00, 'No extra chilli.', '2026-11-16 20:11:00+05:30'),
(17, 8, 15, 'Prawn Masala',             1, 390.00, NULL, '2026-11-17 08:51:00+05:30'),
(18, 8, 18, 'Sol Kadhi',                1,  60.00, NULL, '2026-11-17 08:51:00+05:30'),
(19, 9, 1,  'Gujarati Unlimited Thali', 1, 249.00, NULL, '2026-11-15 18:21:00+05:30'),
(20, 9, 5,  'Masala Chaas',             1,  35.00, NULL, '2026-11-15 18:21:00+05:30'),
(21,10, 12, 'Grilled Paneer Salad',     1, 180.00, NULL, '2026-11-14 20:01:00+05:30'),
(22,11, 16, 'Fish Curry',               1, 320.00, NULL, '2026-11-13 19:01:00+05:30'),
(23,11, 17, 'Steamed Rice',             1,  80.00, NULL, '2026-11-13 19:01:00+05:30'),
(24,11, 18, 'Sol Kadhi',                1,  60.00, NULL, '2026-11-13 19:01:00+05:30'),
(25,12, 3,  'Paneer Butter Masala',     1, 220.00, 'No onion.', '2026-11-16 13:16:00+05:30'),
(26,12, 4,  'Butter Naan',              1,  40.00, NULL, '2026-11-16 13:16:00+05:30'),
(27,12, 6,  'Mango Lassi',              1,  70.00, NULL, '2026-11-16 13:16:00+05:30');

-- ------------------------------------------------------------
-- 11. DELIVERY ASSIGNMENTS
-- Covers offered/accepted/rejected/picked_up/delivered/cancelled;
-- order 8 and 12 show reassignment history without two active rows.
-- ------------------------------------------------------------
INSERT INTO delivery_assignments
(assignment_id, order_id, partner_id, status, assigned_at, accepted_at, picked_up_at, completed_at)
VALUES
(1,  1, 1, 'delivered', '2026-11-10 12:20:00+05:30', '2026-11-10 12:21:00+05:30', '2026-11-10 12:35:00+05:30', '2026-11-10 12:52:00+05:30'),
(2,  2, 2, 'delivered', '2026-11-11 19:25:00+05:30', '2026-11-11 19:26:00+05:30', '2026-11-11 19:40:00+05:30', '2026-11-11 20:00:00+05:30'),
(3,  3, 3, 'delivered', '2026-11-12 13:15:00+05:30', '2026-11-12 13:16:00+05:30', '2026-11-12 13:25:00+05:30', '2026-11-12 13:45:00+05:30'),
(4,  4, 4, 'picked_up', '2026-11-17 08:10:00+05:30', '2026-11-17 08:12:00+05:30', '2026-11-17 08:35:00+05:30', NULL),
(5,  5, 5, 'accepted', '2026-11-17 08:20:00+05:30', '2026-11-17 08:22:00+05:30', NULL, NULL),
(6,  6, 3, 'offered',  '2026-11-17 08:25:00+05:30', NULL, NULL, NULL),
(7,  7, 3, 'rejected', '2026-11-16 20:20:00+05:30', NULL, NULL, NULL),
(8,  8, 1, 'rejected', '2026-11-17 08:58:00+05:30', NULL, NULL, NULL),
(9,  8, 2, 'offered',  '2026-11-17 09:00:00+05:30', NULL, NULL, NULL),
(10, 9, 1, 'cancelled','2026-11-15 18:30:00+05:30', NULL, NULL, NULL),
(11,10, 2, 'cancelled','2026-11-14 20:05:00+05:30', NULL, NULL, NULL),
(12,11, 5, 'delivered', '2026-11-13 19:15:00+05:30', '2026-11-13 19:16:00+05:30', '2026-11-13 19:28:00+05:30', '2026-11-13 19:50:00+05:30'),
(13,12, 4, 'rejected', '2026-11-16 13:25:00+05:30', NULL, NULL, NULL),
(14,12, 2, 'delivered', '2026-11-16 13:28:00+05:30', '2026-11-16 13:29:00+05:30', '2026-11-16 13:40:00+05:30', '2026-11-16 14:00:00+05:30');

-- ------------------------------------------------------------
-- 12. PAYMENTS
-- Covers every payment_method and payment_status; includes retries.
-- ------------------------------------------------------------
INSERT INTO payments
(payment_id, order_id, amount, currency, payment_method, status,
 payment_provider, provider_transaction_id, idempotency_key, created_at, updated_at)
VALUES
(1,  1, 350.20, 'INR', 'upi',               'failed',    'Razorpay', 'rzp_fail_1001_01', 'order-1-attempt-1',  '2026-11-10 12:05:30+05:30', '2026-11-10 12:06:00+05:30'),
(2,  1, 350.20, 'INR', 'upi',               'succeeded', 'Razorpay', 'rzp_success_1001_02','order-1-attempt-2', '2026-11-10 12:06:30+05:30', '2026-11-10 12:07:00+05:30'),
(3,  2, 592.00, 'INR', 'cash_on_delivery', 'succeeded', NULL,       NULL,                'order-2-cod',       '2026-11-11 19:10:30+05:30', '2026-11-11 20:00:00+05:30'),
(4,  3, 400.00, 'INR', 'card',              'succeeded', 'Stripe',   'stripe_1003_01',    'order-3-card',      '2026-11-12 13:00:30+05:30', '2026-11-12 13:02:00+05:30'),
(5,  4, 498.00, 'INR', 'net_banking',       'succeeded', 'Razorpay', 'rzp_1004_01',       'order-4-netbank',   '2026-11-17 07:45:30+05:30', '2026-11-17 07:47:00+05:30'),
(6,  5, 480.45, 'INR', 'wallet',            'pending',   'Internal Wallet', NULL,             'order-5-wallet',    '2026-11-17 08:05:30+05:30', '2026-11-17 08:05:30+05:30'),
(7,  6, 592.00, 'INR', 'card',              'succeeded', 'Stripe',   'stripe_1006_01',    'order-6-card',      '2026-11-17 08:15:30+05:30', '2026-11-17 08:17:00+05:30'),
(8,  7, 387.50, 'INR', 'wallet',            'succeeded', 'Internal Wallet', 'wallet_1007_01','order-7-wallet',  '2026-11-16 20:10:30+05:30', '2026-11-16 20:12:00+05:30'),
(9,  8, 447.50, 'INR', 'upi',               'pending',   'Razorpay', NULL,                'order-8-upi',       '2026-11-17 08:50:30+05:30', '2026-11-17 08:50:30+05:30'),
(10, 9, 323.20, 'INR', 'card',              'cancelled', 'Stripe',   'stripe_cancel_1009','order-9-card',     '2026-11-15 18:20:30+05:30', '2026-11-15 18:25:00+05:30'),
(11,10, 209.00, 'INR', 'wallet',            'failed',    'Internal Wallet', 'wallet_fail_1010','order-10-wallet',  '2026-11-14 20:00:30+05:30', '2026-11-14 20:02:00+05:30'),
(12,11, 488.00, 'INR', 'cash_on_delivery', 'succeeded', NULL,       NULL,                'order-11-cod',      '2026-11-13 19:00:30+05:30', '2026-11-13 19:50:00+05:30'),
(13,12, 371.50, 'INR', 'card',              'failed',    'Stripe',   'stripe_fail_1012_1','order-12-card-1',  '2026-11-16 13:15:30+05:30', '2026-11-16 13:16:00+05:30'),
(14,12, 371.50, 'INR', 'card',              'succeeded', 'Stripe',   'stripe_success_1012_2','order-12-card-2','2026-11-16 13:16:30+05:30', '2026-11-16 13:17:00+05:30');

-- ------------------------------------------------------------
-- 13. REFUNDS (pending, succeeded and failed; partial refund examples)
-- ------------------------------------------------------------
INSERT INTO refunds
(refund_id, payment_id, amount, status, reason, provider_refund_id, created_at, completed_at)
VALUES
(1, 2, 25.00, 'succeeded', 'Goodwill adjustment for a missing side item.', 'rfnd_1001_01', '2026-11-10 14:00:00+05:30', '2026-11-10 14:05:00+05:30'),
(2, 5, 50.00, 'pending',   'Customer reported a duplicate charge; refund review is pending.', 'rfnd_1004_01', '2026-11-17 08:45:00+05:30', NULL),
(3, 7, 30.00, 'failed',    'Refund attempt failed at payment provider.', 'rfnd_1006_01', '2026-11-17 08:40:00+05:30', '2026-11-17 08:41:00+05:30');

-- ------------------------------------------------------------
-- 14. RESTAURANT REVIEWS (only delivered orders)
-- ------------------------------------------------------------
INSERT INTO restaurant_reviews
(restaurant_review_id, order_id, customer_id, restaurant_id, rating, comment, created_at, updated_at)
VALUES
(1, 1,  1, 1, 5, 'Excellent Gujarati thali and everything arrived warm.', '2026-11-10 13:10:00+05:30', '2026-11-10 13:10:00+05:30'),
(2, 2,  2, 2, 4, 'Tasty food and good portion sizes.',                  '2026-11-11 20:20:00+05:30', '2026-11-11 20:20:00+05:30'),
(3, 3,  3, 3, 5, 'Fresh ingredients and well-packed salad bowls.',       '2026-11-12 14:10:00+05:30', '2026-11-12 14:10:00+05:30'),
(4,11,  3, 4, 3, 'Food was good, but delivery took longer than expected.','2026-11-13 20:20:00+05:30', '2026-11-13 20:20:00+05:30'),
(5,12,  5, 1, 4, 'Paneer gravy was flavourful and naan was soft.',       '2026-11-16 14:20:00+05:30', '2026-11-16 14:20:00+05:30');

-- ------------------------------------------------------------
-- 15. FOOD ITEM REVIEWS (one review per purchased order line)
-- ------------------------------------------------------------
INSERT INTO food_item_reviews
(food_review_id, order_item_id, customer_id, rating, comment, created_at, updated_at)
VALUES
(1,  1, 1, 5, 'Thali was fresh and had a good variety.',             '2026-11-10 13:12:00+05:30', '2026-11-10 13:12:00+05:30'),
(2,  2, 1, 4, 'Naan was soft; could have been a little warmer.',     '2026-11-10 13:13:00+05:30', '2026-11-10 13:13:00+05:30'),
(3,  3, 1, 5, 'Chaas was refreshing.',                               '2026-11-10 13:14:00+05:30', '2026-11-10 13:14:00+05:30'),
(4,  4, 2, 1, 'The chicken was overcooked and too dry.',                  '2026-11-11 20:22:00+05:30', '2026-11-11 20:22:00+05:30'),
(5,  5, 2, 5, 'Biryani was aromatic and delicious.',                 '2026-11-11 20:23:00+05:30', '2026-11-11 20:23:00+05:30'),
(6,  6, 3, 5, 'Fresh bowl with balanced flavours.',                  '2026-11-12 14:12:00+05:30', '2026-11-12 14:12:00+05:30'),
(7,  7, 3, 4, 'Good salad; paneer was nicely grilled.',               '2026-11-12 14:13:00+05:30', '2026-11-12 14:13:00+05:30'),
(8, 22, 3, 4, 'Fish curry had a rich and authentic flavour.',         '2026-11-13 20:22:00+05:30', '2026-11-13 20:22:00+05:30'),
(9, 23, 3, 5, 'Rice was perfectly cooked.',                           '2026-11-13 20:23:00+05:30', '2026-11-13 20:23:00+05:30'),
(10,24, 3, 4, 'Sol kadhi was refreshing.',                            '2026-11-13 20:24:00+05:30', '2026-11-13 20:24:00+05:30'),
(11,25, 5, 5, 'Paneer butter masala was rich and tasty.',             '2026-11-16 14:22:00+05:30', '2026-11-16 14:22:00+05:30'),
(12,26, 5, 4, 'Naan was good.',                                       '2026-11-16 14:23:00+05:30', '2026-11-16 14:23:00+05:30');

-- ------------------------------------------------------------
-- 16. DELIVERY PARTNER REVIEWS (only completed assignments)
-- ------------------------------------------------------------
INSERT INTO delivery_partner_reviews
(delivery_review_id, assignment_id, customer_id, rating, comment, created_at, updated_at)
VALUES
(1,  1, 1, 5, 'Manish was polite and delivered on time.',             '2026-11-10 13:15:00+05:30', '2026-11-10 13:15:00+05:30'),
(2,  2, 2, 5, 'Smooth and quick delivery.',                           '2026-11-11 20:25:00+05:30', '2026-11-11 20:25:00+05:30'),
(3,  3, 3, 2, 'Delivery was considerably delayed, though the partner was polite.',                            '2026-11-12 14:15:00+05:30', '2026-11-12 14:15:00+05:30'),
(4, 12, 3, 3, 'Partner was courteous, but delivery was delayed.',      '2026-11-13 20:25:00+05:30', '2026-11-13 20:25:00+05:30'),
(5, 14, 5, 5, 'Delivered carefully and followed the instructions.',   '2026-11-16 14:25:00+05:30', '2026-11-16 14:25:00+05:30');

-- ------------------------------------------------------------
-- 17. RESET IDENTITY SEQUENCES AFTER EXPLICIT ID INSERTS
-- This ensures future inserts can omit IDs safely.
-- ------------------------------------------------------------
SELECT setval(pg_get_serial_sequence('customers', 'customer_id'), (SELECT MAX(customer_id) FROM customers), TRUE);
SELECT setval(pg_get_serial_sequence('addresses', 'address_id'), (SELECT MAX(address_id) FROM addresses), TRUE);
SELECT setval(pg_get_serial_sequence('restaurants', 'restaurant_id'), (SELECT MAX(restaurant_id) FROM restaurants), TRUE);
SELECT setval(pg_get_serial_sequence('restaurant_operating_hours', 'operating_hours_id'), (SELECT MAX(operating_hours_id) FROM restaurant_operating_hours), TRUE);
SELECT setval(pg_get_serial_sequence('menus', 'menu_id'), (SELECT MAX(menu_id) FROM menus), TRUE);
SELECT setval(pg_get_serial_sequence('menu_items', 'menu_item_id'), (SELECT MAX(menu_item_id) FROM menu_items), TRUE);
SELECT setval(pg_get_serial_sequence('delivery_partners', 'partner_id'), (SELECT MAX(partner_id) FROM delivery_partners), TRUE);
SELECT setval(pg_get_serial_sequence('orders', 'order_id'), (SELECT MAX(order_id) FROM orders), TRUE);
SELECT setval(pg_get_serial_sequence('order_address_history', 'address_history_id'), (SELECT MAX(address_history_id) FROM order_address_history), TRUE);
SELECT setval(pg_get_serial_sequence('order_items', 'order_item_id'), (SELECT MAX(order_item_id) FROM order_items), TRUE);
SELECT setval(pg_get_serial_sequence('delivery_assignments', 'assignment_id'), (SELECT MAX(assignment_id) FROM delivery_assignments), TRUE);
SELECT setval(pg_get_serial_sequence('payments', 'payment_id'), (SELECT MAX(payment_id) FROM payments), TRUE);
SELECT setval(pg_get_serial_sequence('refunds', 'refund_id'), (SELECT MAX(refund_id) FROM refunds), TRUE);
SELECT setval(pg_get_serial_sequence('restaurant_reviews', 'restaurant_review_id'), (SELECT MAX(restaurant_review_id) FROM restaurant_reviews), TRUE);
SELECT setval(pg_get_serial_sequence('food_item_reviews', 'food_review_id'), (SELECT MAX(food_review_id) FROM food_item_reviews), TRUE);
SELECT setval(pg_get_serial_sequence('delivery_partner_reviews', 'delivery_review_id'), (SELECT MAX(delivery_review_id) FROM delivery_partner_reviews), TRUE);

COMMIT;

-- ------------------------------------------------------------
-- VERIFICATION QUERIES
-- These SELECT statements run after COMMIT and show seeded row counts.
-- ------------------------------------------------------------
SELECT 'customers' AS table_name, COUNT(*)::bigint AS row_count FROM customers
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

-- Status coverage: every enum value should appear in the relevant sample data.
SELECT status::text AS order_status, COUNT(*) AS orders_count
FROM orders GROUP BY status ORDER BY status;

SELECT status::text AS payment_status, COUNT(*) AS payments_count
FROM payments GROUP BY status ORDER BY status;

SELECT payment_method::text AS payment_method, COUNT(*) AS payments_count
FROM payments GROUP BY payment_method ORDER BY payment_method;

SELECT status::text AS assignment_status, COUNT(*) AS assignments_count
FROM delivery_assignments GROUP BY status ORDER BY status;

SELECT status::text AS refund_status, COUNT(*) AS refunds_count
FROM refunds GROUP BY status ORDER BY status;
