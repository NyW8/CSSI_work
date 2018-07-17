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
function printer(name, time, fav=false){
  let words;
  if (!fav){
    words = "I will walk "+name.charAt(0).toUpperCase()+name.substr(1)+" today at "+time;

  }else{
    words = "I will walk "+name.charAt(0).toUpperCase()+name.substr(1)+", one of my favorite dogs, today at "+time;
  }
  document.getElementById("hi").innerHTML = words;
}

let favDogs = ['spike', 'jeremy', 'lola', 'peaches', 'steve'];
// Task 1
let dogName1 = "Steve";
let dogType1 = "beagle";

// Complete Task 1 Below
printer(dogName1, "12:00 pm");




let dogName2 = "Joe";
let dogType2 = "bulldog";

// Complete Task 2 Below

if (dogType2 == "corgi"){
  printer(dogName2, "12:00 pm");
} else {
  printer(dogName2, "1:00 pm");
}


let dogName = "Lola";
let dogType = "poodle";

// Complete Task 3 Below
if (dogType == "corgi" || dogType == "beagle"){
  printer(dogName, "1:00 pm");
} else {
  printer(dogName, "2:00 pm");
}

function walking(){
  let name = document.getElementById('dog-name').value.toLowerCase();
  let type = document.getElementById('dog-type').value.toLowerCase();
  let found = false;
  for (var v in favDogs) {
    if (v == name) {
      if (type== "corgi" || type== "beagle"){
        printer(name, "1:00 pm", true);
      } else {
        printer(name, "2:00 pm", true);
      }
      found = true;
      break;
    }
  }
  if (!found && (type == "corgi" || type == "beagle")){
    printer(name, "1:00 pm");
  } else {
    printer(name, "2:00 pm");
  }
}
