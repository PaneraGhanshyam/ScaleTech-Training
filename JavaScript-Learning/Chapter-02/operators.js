"use strict";

const itemPrice = 250;
const quantity = 2;
const deliveryFee = 40;

let subtotal = itemPrice * quantity;

let discount = 50;

let finalAmount = subtotal + deliveryFee - discount;

console.log("Subtotal:", subtotal);
console.log("Delivery fee:", deliveryFee);
console.log("Discount:", discount);
console.log("Final amount:", finalAmount);