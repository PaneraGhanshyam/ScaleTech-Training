"use strict";

let customerName = prompt("Enter your name:", "");

alert(`Welcome ${customerName}!`);

let confirmOrder = confirm("Do you want to place your order?");

console.log("Customer:", customerName);
console.log("Confirmed:", confirmOrder);