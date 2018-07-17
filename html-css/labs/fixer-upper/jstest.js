

function sendAlert(){
alert("This is an alert box!");
}


function sendConfirmation(){
confirm("This is a confirmation box!");
}

function submit(){
  var txt;
  var r = confirm("Are you sure?");
  if (r == true) {
    alert("Yay, thanks!")
  } else {
    alert("Booooo");
  }
}

function ages(age){
  if (age >=15){
    alert("You can get your driver's license!");
  }else{
    alert("Not yet!");
  }
}
