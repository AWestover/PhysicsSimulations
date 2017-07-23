// Alek Westover
// A simple diffusion simulation

// variables initialized
var screen_dims = [500, 500];
var screen_color = [0, 0, 0];
var particles = [];
var num_particles = [10, 10]; // type a, type b
var dt = 1;


// setup function
function setup() {
	createCanvas(screen_dims[0], screen_dims[1]);
	for (var i = 0; i < num_particles[0]; i++) {
		particles.push(new Particle(p5.Vector.random2D(), p5.Vector.random2D(), [10, 10], 'allowed', 10));
	}
	for (var i = 0; i < num_particles[1]; i++) {
		particles.push(new Particle(p5.Vector.random2D(), p5.Vector.random2D(), [7, 7], 'not allowed', 10));
	}

}

// main loop
function draw() {
	background(screen_color[0], screen_color[1], screen_color[2]);
	for (var i = 0; i < particles.length; i++) {
		particles[i].show();
		particles[i].update(dt);
		particles[i].handle_wall_collide(screen_dims);
		//particles[i].hit_membrane(pos, dims);
	}

}
