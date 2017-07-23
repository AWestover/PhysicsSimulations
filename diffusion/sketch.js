// Alek Westover
// A simple diffusion simulation

// variables initialized
var screen_dims = [500, 400];
var channel_pos = [0.4*screen_dims[0], 0.4*screen_dims[1]];
var channel_dims = [0.2*screen_dims[0], 0.2*screen_dims[1]];
var boundary_bands_loc = [[0, 0.45*screen_dims[1]], [0.6*screen_dims[0], 0.45*screen_dims[1]]]; //impassable strips on either side of the channel
var boundary_bands_dims = [[0.4*screen_dims[0], 0.1*screen_dims[1]], [0.4*screen_dims[0], 0.1*screen_dims[1]]];
var screen_color = [0, 0, 100];

var particles;
var num_particles = [10, 10]; // type allowed through channel, type not allowed through channel
var max_speed;

var dt;


// resets all of the particels, initializes the particles array to empty set and then repopulates it
function reset_sim () {
	//initialize variables
	particles = [];
	// creates the allowed particles
	for (var i = 0; i < num_particles[0]; i++) {
		particles.push(new Particle(createVector(random()*screen_dims[0], random()*channel_pos[1]), p5.Vector.random2D(), [10, 10], 'allowed', max_speed));
	}
	// Create the not allowed particles
	for (var i = 0; i < num_particles[1]; i++) {
		particles.push(new Particle(createVector(random()*screen_dims[0], random()*channel_pos[1]), p5.Vector.random2D(), [7, 7], 'not allowed', max_speed));
	}
}

// handles the input tags, makes sure calid integer input is given
function env_changes() {
	if (!isNaN(parseInt(document.getElementById('dt').value))) {
		dt = parseInt(document.getElementById('dt').value);
	}
	if (!isNaN(parseInt(document.getElementById('heat').value))) {
		max_speed = parseInt(document.getElementById('heat').value);
	}
	if (!isNaN(parseInt(document.getElementById('canvas height').value))) {
		screen_dims[1] = parseInt(document.getElementById('canvas height').value);
	}
	if (!isNaN(parseInt(document.getElementById('canvas width').value))) {
		screen_dims[0] = parseInt(document.getElementById('canvas width').value);
	}
	var proposed_allowed_particles_num = parseInt(document.getElementById('number of allowed particles'));
	var proposed_not_allowed_particles_num = parseInt(document.getElementById('number of not allowed particles'));
	if (!isNaN(proposed_allowed_particles_num) && !isNaN(proposed_not_allowed_particles_num)) {
		//initialize variables
		num_particles = [proposed_allowed_particles_num, proposed_not_allowed_particles_num];
		particles = [];
		// creates the allowed particles
		for (var i = 0; i < num_particles[0]; i++) {
			particles.push(new Particle(createVector(random()*screen_dims[0], random()*channel_pos[1]), p5.Vector.random2D(), [10, 10], 'allowed', max_speed));
		}
		// Create the not allowed particles
		for (var i = 0; i < num_particles[1]; i++) {
			particles.push(new Particle(createVector(random()*screen_dims[0], random()*channel_pos[1]), p5.Vector.random2D(), [7, 7], 'not allowed', max_speed));
		}
	}
	resizeCanvas(screen_dims[0], screen_dims[1]);
	for (var i = 0; i < particles.length; i++) {
		particles[i].max_speed = max_speed;
	}
}

// setup function
function setup() {
	createCanvas(screen_dims[0], screen_dims[1]);
	// Make all particles
	reset_sim();
}

// main loop
function draw() {
	frameRate(dt);
	// background color for simulation window
	background(screen_color[0], screen_color[1], screen_color[2]);
	// Draw the boundaries that nothing is let through
	fill(70, 70, 70);
	rect(boundary_bands_loc[0][0], boundary_bands_loc[0][1], boundary_bands_dims[0][0], boundary_bands_dims[0][1]);
	rect(boundary_bands_loc[1][0], boundary_bands_loc[1][1], boundary_bands_dims[1][0], boundary_bands_dims[1][1]);
	//Draw the channel
	fill(30, 30, 30);
	rect(channel_pos[0], channel_pos[1], channel_dims[0], channel_dims[1]);

	for (var i = 0; i < particles.length; i++) {
		// show and update and check boundaries for all particles
		particles[i].show();
		particles[i].handle_wall_collide(screen_dims);
		particles[i].hit_boundary(boundary_bands_loc[0], boundary_bands_dims[0], 'no one');
		particles[i].hit_boundary(boundary_bands_loc[1], boundary_bands_dims[1], 'no one');
		particles[i].hit_boundary(channel_pos, channel_dims, 'allowed');
		//only sets random velocity if velocity hasn't changed yet this round
		particles[i].set_random_vel();
		particles[i].update(dt);
	}

}


