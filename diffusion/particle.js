// Defines the particle class

// initialize the class
function Particle(pos, vel, dims, type, max_speed) {
	this.pos = pos;
	this.vel = vel;
	this.dims = dims;
	this.type = type;
	this.max_speed = max_speed;
};

// displays the particles
Particle.prototype.show = function() {
	if (this.type == 'allowed') {
		fill(0, 255, 0, 50);
		ellipse(this.pos.x, this.pos.y, this.dims[0], this.dims[1]);
	}
	else {
		fill(255, 0, 0, 50);
		ellipse(this.pos.x, this.pos.y, this.dims[0], this.dims[1]);
	}
};

// gives particels random velocities and updates their positions
Particle.prototype.update = function(dt) {
	this.pos.add(p5.Vector.mult(this.vel, dt));
	this.vel = p5.Vector.random2D(); 	
};

// makes particles bounce off of the walls
Particle.prototype.handle_wall_collide = function(screen_dims) {
	if (this.pos.x <= 0) {
		this.vel.x = this.max_speed;
	} 
	else if (this.pos.x >= screen_dims[0]) {
		this.vel.x = -this.max_speed;
	}
	if (this.pos.y >= screen_dims[1]) {
		this.vel.y = -this.max_speed;
	}
	else if (this.pos.y <= 0) {
		this.vel.y = this.max_speed;
	}
};

// handles membrane collision accepting or rejecting particles based on their type
Particle.prototype.hit_membrane = function(membrane_pos, membrane_dims) {
	if (this.type == "allowed") {
		console.log("CARRY ON");
	}
	else {
		console.log("YOU SHALL NOT PASS");
	}
};