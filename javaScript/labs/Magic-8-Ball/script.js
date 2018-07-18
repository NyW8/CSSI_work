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

let answer = document.getElementById('answer');
let positive = ["It is certain", "It is decidedly so", "Without a doubt","Yes – definitely", "You may rely on it", "As I see it", "Most Likely","Outlook good", "Yes", "Signs point to yes"];
let negative = ["Don’t count on it", "My reply is no","My sources say no", "Outlook not so good", "Very doubtful"];
let noncommital = ["Reply hazy", "Try again","Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"];

document.addEventListener('click', ()=>{
  let cat = Math.floor(Math.random()*6);
  let color;
  let arr;
  if (cat <=2){
    arr = positive;
    color = "green";
  }else if (cat <=4){
    arr = negative;
    color = "red";
  }else {
    arr = noncommital;
    color = "yellow";
  }
  let num = Math.floor(Math.random()*arr.length);
  answer.innerText = arr[num];
  answer.style.color = color;
  console.log(cat);
});
