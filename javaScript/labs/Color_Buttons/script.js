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

// Use querySelector to store the div in a variable.
let redButton = document.querySelector('#red');
let greenButton = document.querySelector('#green');
let blueButton = document.querySelector('#blue');
let clearButton = document.querySelector('#clear');
let div = document.getElementById('responseBox');

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', e => {
  console.log("You clicked the red button!");
  div.style.backgroundColor = "red";
  div.innerHTML+="red ";
})

// Use addEventListener to respond to a click event.
greenButton.addEventListener('click', e => {
  console.log("You clicked the green button!");
  div.style.backgroundColor = "green";
  div.innerHTML+="green ";
})

// Use addEventListener to respond to a click event.
blueButton.addEventListener('click', e => {
  console.log("You clicked the blue button!");
  div.style.backgroundColor = "blue";
  div.innerHTML+="blue ";
})

// Use addEventListener to respond to a click event.
clearButton.addEventListener('click', e => {
  console.log("You clicked the 'clear' button!");
  div.style.backgroundColor = "white";
  div.innerHTML="";
})
