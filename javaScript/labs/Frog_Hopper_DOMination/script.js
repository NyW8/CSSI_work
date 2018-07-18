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

let currentlily = 1;
let tricky = document.getElementById('lilypad4');
let tlVisible = true;

let frogger = document.querySelector('#frog');/*use a querySelector to grab your frog from your HTML*/;

frogger.addEventListener('click'/* Insert type of event are we listening for */, function(){
// Insert what should happen when you click on the frog!
console.log("hop");
setActiveLillyPad();
});

setInterval(visibleOrInvisible, 1000);

document.getElementById('win-text').style.display="none";

frogger.addEventListener('mouseover', function(){

  frogger.style.width = "80px";
  frogger.style.height = "80px";
});

frogger.addEventListener('mouseout', function(){

  frogger.style.width = "70px";
  frogger.style.height = "70px";
});

document.body.onkeyup = function(e){
  if (e.keyCode ==32){

    frogger.style.left = "17%";
    frogger.style.top = "50%";
    document.getElementById('lilypad1').classList.add('active');
    document.getElementById('lilypad2').classList.remove('active');
    document.getElementById('lilypad3').classList.remove('active');
    document.getElementById('lilypad4').classList.remove('active');
    document.getElementById('lilypad5').classList.remove('active');
    currentlily = 1;
    document.getElementById('win-text').innerText = "You won!"
    document.getElementById('win-text').style.display="none";
  }
}
function reset(){
      frogger.style.left = "17%";
      frogger.style.top = "50%";
      document.getElementById('lilypad1').classList.add('active');
      document.getElementById('lilypad2').classList.remove('active');
      document.getElementById('lilypad3').classList.remove('active');
      document.getElementById('lilypad4').classList.remove('active');
      document.getElementById('lilypad5').classList.remove('active');
      currentlily = 1;
      document.getElementById('win-text').innerText = "You won!"
      document.getElementById('win-text').style.display="none";
}

function visibleOrInvisible(){
  if (tricky.style.display === "none") {
    tricky.style.display = "block";
    tlVisible = true;
  } else {
    tricky.style.display = "none";
    tlVisible = false;
  }
}

function setActiveLillyPad(){
  currentlily++;
  if (currentlily==6){
    document.getElementById('lilypad'+1).classList.add('active');
    document.getElementById('lilypad'+5).classList.remove('active');
    frogger.style.left = "17%";
    frogger.style.top = "50%";
    currentlily = 1;
  } else{
    document.getElementById('lilypad'+currentlily).classList.add('active');
    document.getElementById('lilypad'+(currentlily-1)).classList.remove('active');
    switch (currentlily){
      case 2:
        frogger.style.left = "33.5%";
        frogger.style.top = "24%";
        break;
      case 3:
        frogger.style.left = "50%";
        frogger.style.top = "50%";
        break;
      case 4:
        frogger.style.left = "68%";
        frogger.style.top = "75%";
        if (!tlVisible){
          document.getElementById('win-text').innerText = "You lost!"
          document.getElementById('win-text').style.display="block";
          let a = confirm("YOU LOST! Would you like to play again?");
          reset();
        }
        break;
      case 5:
        frogger.style.left = "83%";
        frogger.style.top = "50%";
        document.getElementById('win-text').style.display="block";
        let a = confirm("YOU WON! Would you like to play again?");
        reset();
        break;
        //YOU WON!
    }
  }
}
