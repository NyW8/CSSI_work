

const likeButton = document.getElementById('likeButton');


//can get this information through the console by calling article.etc
//        e.g.: article.editors[2].name is "Salman Rushdie"
const article = {
  name:"Dog family gives birth to litter of 10 puppies",
  views:1234,
  datePublished:"03/25/2018",
  author:{
    name:"Joe Corgi",
    title:"Senior Canine Editor",
  },
  editors: [{
    name:"Brian Brushwood",
    title:"Person1",
  },{
    name:"Betty Bumblebee",
    title:"Person2",
  },{
    name:"Salman Rushdie",
    title:"Person3"
  }
  ]
}
let boxTop = 100;
let boxLeft = 100;
const floatingBox = document.querySelector(".floatingBox");

document.addEventListener('keydown', e => {
  const key = e.key;
  if (key == "ArrowLeft"){
    boxLeft-=50;
    console.log("left!");
  } else if(key == "ArrowRight"){
    boxLeft+=50;
    console.log("right!");
  } else if (key == "ArrowDown"){
    boxTop+=50;
    console.log("down!");
  } else if (key == "ArrowUp"){
    boxTop-=50;
    console.log("up!");
  } else{
    return;
  }
  floatingBox.style.top= boxTop+"px";
  floatingBox.style.left = boxLeft+"px";
})
