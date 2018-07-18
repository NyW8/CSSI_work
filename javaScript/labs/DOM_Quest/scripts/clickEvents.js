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

console.log("Running Click Events Script");
let boxes = document.getElementsByClassName('box');


function changeColor(color){
  for (i = 0; i < 3; i++){
  console.log(i+" "+boxes[i].style.background);
    boxes[i].style.backgroundColor = color;
  }
  console.log("done"+color+" "+color.type);
}

let fourOn = true; 
let fiveOn = false;

function switchIt(num) {

  /*if (num == 4){

    if (fourOn){
      boxes[4].style.backgroundColor = "blue";
      fourOn = false;
    }else{
      fourOn = true;
      boxes[4].style.backgroundColor = "yellow";
    }

  }else{

    if (fiveOn){
      boxes[5].style.backgroundColor = "blue";
      fiveOn = false;
    }else{
      fiveOn = true;
      boxes[5].style.backgroundColor = "yellow";
    }

  }*/

}
