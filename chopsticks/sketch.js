//***********ALEK*****************//
//Coded by Alek Westover

//Constants and imported stuff
var screen_dims;
var screen_color;
var startScreen;
var Hands;
var OldHands;
var won;
var validMove;
var playerConfirmationStage;
var firstChance;
var oked;
var Match;
var train;
var playerStrat;
var stolenStrat;
var Strat;
var countelements;
var countelementsagain;

//strategy
var BestCompStrat=[
[2,1,1,0,3,1,1,0],
[1,1,1,2,1,2,0,2],
[1,3,0,2,1,3,0,0],
[1,4,0,0,0,4,0,0],
[2,1,1,0,3,1,1,0],
[1,1,1,2,1,0,2,2],
[1,0,4,2,1,2,2,2],
[1,2,4,2,0,2,4,2],
[1,2,4,1,1,2,4,0],
[1,3,4,0,0,3,4,0],
[1,1,1,1,1,0,2,1],
[1,0,3,1,1,2,1,1],
[2,2,1,0,4,2,1,0],
[2,2,1,2,4,2,1,2],
[4,1,1,2,0,1,1,2],
[0,1,3,2,0,1,3,0],
[1,2,1,1,1,0,3,1],
[1,0,4,1,1,3,1,1],
[1,4,1,1,1,2,3,1],
[1,2,4,1,0,2,4,1],
[0,3,4,1,0,3,4,0],
[1,2,4,1,0,2,4,1],
[0,3,4,1,0,3,4,0],
[1,1,1,1,1,1,1,2],
[3,1,1,0,4,1,1,0],
[2,1,1,2,2,2,0,2],
[2,4,0,2,2,2,2,2],
[1,2,2,3,1,2,2,0],
[1,3,2,0,3,3,2,0],
[1,3,2,2,1,3,2,0],
[1,4,2,0,0,4,2,0],
[2,1,1,0,3,1,1,0],
[1,1,1,2,1,0,2,2],
[3,0,2,0,0,0,2,0],
[1,1,1,1,1,0,2,1],
[1,0,3,1,1,2,1,1],
[1,3,1,1,1,2,2,1],
[1,3,2,1,4,3,2,1],
[4,3,1,1,0,3,1,1],
[0,4,1,1,0,4,1,0],
[1,2,1,1,1,0,3,1],
[2,0,3,0,0,0,3,0]
];

function initialize_vars() {
  screen_dims = [window.innerWidth*0.6, window.innerHeight*0.6];
  screen_color = [255, 255, 255];
  startScreen = 1;
  Hands = [1, 1, 1, 1];
  OldHands = [1, 1, 1, 1];
  won = 'no one';
  validMove = 0;
  playerConfirmationStage = 0;
  firstChance = 1;
  oked = 1;
  Match = 0;
  train = 0;
  playerStrat = [];
  stolenStrat = [];
  Strat = BestCompStrat;
  countelements = 0;
  countelementsagain = 0;
}

// initialize everything
function setup() {
  initialize_vars();
  var my_canvas = createCanvas(screen_dims[0], screen_dims[1]);
  my_canvas.class("my_canvas");
}

function dontAddDuplicates(){
  for(var i = 0; i<playerStrat.length; i++){
    for(var a = 0; a<Strat.length; a++){
      countelements=0;
      for(var c = 0; c<8; c++){
        if(playerStrat[i][c]===Strat[a][c]){
          countelements+=1;
        }
      }
    }

    for(var l = 0; l<stolenStrat.length; l++){
      countelementsagain=0;
      for(var c = 0; c<8; c++){
        if(playerStrat[i][c]===stolenStrat[l][c]){
          countelementsagain+=1;
        }
      }
    }

    if(countelements<8&&countelementsagain<8){
      stolenStrat.push(playerStrat[i]);
    }
  }
  return stolenStrat;
};

function drawHand(){
    for (var i=0; i<Hands[0]; i++){ellipse(0.9375*width,0.225*height+0.05*height*i,0.1875*width,0.05*height);}
    for (var i=0; i<Hands[2]; i++){ellipse(0.025*width,0.725*height+0.05*height*i,0.1875*width,0.05*height);}
    for (var i=0; i<Hands[1]; i++){ellipse(0.025*width,0.225*height+0.05*height*i,0.1875*width,0.05*height);}
    for (var i=0; i<Hands[3]; i++){ellipse(0.9375*width,0.725*height+0.05*height*i,0.1875*width,0.05*height);}
};

function updateScreen(){
    background(0, 101, 168);
    line(0,height/2,width,height/2);
    line(width/2,0,width/2,height);
    fill(0, 0, 0);
    textSize(20);
    text("Computer",0.0625*width,0.075*height);
    text("Player",0.7625*width,0.075*height);
    text(Hands[0],0.5375*width,0.475*height);
    text(Hands[1],0.4425*width,0.475*height);
    text(Hands[2],0.4425*width,0.5725*height);
    text(Hands[3],0.5375*width,0.5725*height);
    drawHand();
};
var turn = 'no one';

function setUpGame(){
    turn = ['computer','player'][round(random(0,1))];
    Hands = [1,1,1,1];
    won = 'no one';
    startScreen = 0;
    firstChance = 1;
    train = 0;
};

// resets hands that are over 5
function over5Reset(){
  for(var i=0; i<4;i++) {
    if(Hands[i]>4){
      Hands[i]-=5;
    }
  }
};

// Checks if the game has ended
function checkGameOver(){
    over5Reset();
    if(Hands[1]===0&&Hands[2]===0){won='player';}
    if(Hands[0]===0&&Hands[3]===0){won='computer';}
    if(train===5&&won!=='no one'){
        dontAddDuplicates();
        for(var i = 0; i<stolenStrat.length;i++){
            console.log('['+stolenStrat[i]+'], ');
        }
    }
};

// main loop
function draw(){
  background(screen_color[0], screen_color[1], screen_color[2]);
  over5Reset();
  if(startScreen===1) {
      fill(0,0,255);
      textSize(0.025*width+0.025*height);
      text("When it is your turn click on the hand configuration buttons.\n\
If you input a possible outcome and click 'done' the computer will go after you.\n\
Your objective is to get the computer to have all 0's\n\
(The game is played in mod 5 so a '5' goes to a zero).\n\
Click Start to begin.\n\
Good Luck!",0.01*width,30,width*0.9);
  }
  if(won==='no one' && startScreen===0){
    if(turn==='computer'){
      checkGameOver();
      if(won==='no one'){
        computerMove();
        over5Reset();
        checkGameOver();
      }
    }
    if(turn==='player'){
      playerMove();
      over5Reset();
    }
  }
  if (won!=='no one') {
      textSize(37);
      if(won==='player'){
          background(255,0,0);
          text("Good Job, You Won",46,200);
      }
      if(won==='computer') {
          background(0, 255, 0);
          text("Bad Job, You didn't Win",46,200);
      }
  }
}
