"use strict";

const foodName = "Paneer Tikka";

let itemPrice = 250;
let quantity = 2;

let deliveryCharge = 40;

let subtotal = itemPrice * quantity;

let total = subtotal + deliveryCharge;

console.log("Food:", foodName);
console.log("Subtotal:", subtotal);
console.log("Delivery:", deliveryCharge);
console.log("Total:", total);