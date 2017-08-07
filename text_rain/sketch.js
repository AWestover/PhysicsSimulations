//Coded by Alek Westover

// global variables
var screen_dims;
var dt;

var num_columns;
var char_text_size;
var text_columns;
var tc_colors;


function reset_global_variables() {
  screen_dims = [window.innerWidth, window.innerHeight];
  dt = 1;

  num_columns = 50;
  char_text_size = floor(screen_dims[0]/num_columns);
  text_columns = [];
  tc_colors = [];
  for (var i = 0; i < num_columns; i++) {
    var c_x = round(i*screen_dims[0]/num_columns);
    var c_y = round(random(-screen_dims[1], 0));
    text_columns.push(new text_column(c_x, c_y));
    tc_colors.push([0, 255, 0]);
  }
}


function setup() {
  reset_global_variables();
  createCanvas(screen_dims[0], screen_dims[1]); 
}


function draw(){
  background(0, 0, 0, 50);
  for (var i = 0; i < num_columns; i++) {
    text_columns[i].display(tc_colors[i]);
    text_columns[i].update(dt);
  }
}


function keyReleased() {
  if (key.toLowerCase() == 'r') {
    reset_global_variables();
  }
}


function mousePressed() {
  tc_colors[round(random(0, tc_colors.length))] = [random(0, 255), random(0, 255), random(0, 255)];
}


function touchStarted() {
  tc_colors[round(random(0, tc_colors.length))] = [random(0, 255), random(0, 255), random(0, 255)];
}

