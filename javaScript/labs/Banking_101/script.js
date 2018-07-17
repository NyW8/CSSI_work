// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;
let logged_in = false;
let password;

function show(words){
  document.getElementById("hi").innerHTML = words;
}

function openAccount(){
  let name = document.getElementById('name').value;
  let pass = document.getElementById('pass').value;
  if (name == null || pass == null){
    show("Please enter your information.");

  }else{
  balance = 0;
  password = pass;
  // Set the value for customer_name equal to name below
  customer_name = name;
  logged_in = true;
  show(customer_name+" has opened a new account with a balance of $"+balance+"."); //write the statement you need to return here
}
}

function logIn(){
    let name = document.getElementById('name').value;
    let pass = document.getElementById('pass').value;
    if (name == null || pass == null){
      show("Please enter your information.");
    }
  if (name == customer_name && pass == password){
    logged_in = true;
    show("Welcome back, "+customer_name+".");
  } else{
    show("Incorrect log in, please try again.");
  }
}

function logOut(){
  logged_in = false;
  show(customer_name+" has logged out.");
}

function deposit(){
  let value = Number(document.getElementById('wd-amt').value);
  if (!logged_in){
    show("Please log in to deposit money into your account.");
  } else{
  balance +=value;
  // update the value of balance
  //return the correct statement
  show(customer_name + " has deposited $"+value+". "+ customer_name+"'s total balance is $"+balance+".");
}
}

function withdraw(){
  let value = Number(document.getElementById('wd-amt').value);
  if (!logged_in){
    show("Please log in to withdraw money from your account.");
  }else{
  //update the value of balance
  if (balance - value > 0){
    balance -= value;
    show(customer_name+" has withdrawn "+ value+". "+customer_name+" has $"+balance+" remaining.");
  }else{
    show("Sorry "+customer_name+", you do not have enough money in your account. You need $"+(value - balance)+" more to withdraw this amount.");
  }
}
  //return the correct statement
}


// Write your script below
