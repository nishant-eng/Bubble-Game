var timer = 60;
var score =0;
var hitrn=0;
var clutter="";
function makeBubble(){for(let i=1;i<=102;i++){
    var rn=Math.floor(Math.random()*10)
   clutter += `<div class="bubble">${rn}</div>`
}
document.querySelector("#pbtm").innerHTML=clutter
}

function getNewHit(){
    hitrn  = Math.floor(Math.random()*10);
     document.querySelector("#hitval").textContent=hitrn;
}

function runTimer(){
    var timerInterval = setInterval(function(){
        if(timer>0){
            timer--;
            document.querySelector('#timerval').textContent=timer;
        }
        else{
            clearInterval(timerInterval);
            document.querySelector("#pbtm").innerHTML=`<h1>Game Over</h1>`;
        }
    },1000);
}

function increaseScore(){
    score += 10;
    document.querySelector("#scoreval").textContent=score;
}

//Event Bubbling
document.querySelector("#pbtm").addEventListener("click",function(details){
    var clickNum=Number(details.target.textContent);
    if(clickNum == hitrn){
        increaseScore();
        makeBubble();
        getNewHit();
    }
});

makeBubble();
getNewHit();
runTimer();
increaseScore();


