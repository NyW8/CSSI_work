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

let amusementParks = ["Disney World", "Hershey Park", "Six Flags", "Dorney Park", "Sea World"];
//Complete task one below
amusementParks.forEach((name) => {
  console.log(name.toUpperCase()+" is a great amusement park.");
});



let rollerCoasters = ["Big Thunder Mountain Railroad","Splash Mountain","Space Mountain", "Expedition Everest","The Twilight Zone Tower of Terror"];
//Complete task two below
for (let i = 0; i < rollerCoasters.length; i++){
  console.log("I will ride "+rollerCoasters[i]);
  if (rollerCoasters[i] == "Space Mountain"){
    break;
  }
}


let height = 6;
//Complete task three below

while(height > 4){
  console.log("Next Customer");
  height = Math.floor(Math.random()*5)+2;
}
