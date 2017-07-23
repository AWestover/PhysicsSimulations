// Defines the particle class

// initialize the class
function Particle(pos, vel, dims, type, max_speed) {
	this.pos = pos;
	this.vel = vel;
	this.dims = dims;  //[width, height] (for circle  [diameter, diameter])
	this.type = type;
	this.max_speed = max_speed;
	this.random_vel_needed = true;
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

// updates their positions
Particle.prototype.update = function(dt) {
	this.pos.add(p5.Vector.mult(this.vel, dt));
	this.random_vel_needed = true;
};

// asigns a random velocity to each particle as the default motion
Particle.prototype.set_random_vel = function() {
	if (this.random_vel_needed) {
		this.vel = p5.Vector.random2D().mult(0.7*this.max_speed); 
	}
}

// makes particles bounce off of the walls
Particle.prototype.handle_wall_collide = function(screen_dims) {
	if (this.pos.x - this.dims[0]*0.5 <= 0) {
		this.vel.x = this.max_speed;
		this.random_vel_needed = false;
	} 
	else if (this.pos.x + this.dims[0]*0.5 >= screen_dims[0]) {
		this.vel.x = -this.max_speed;
		this.random_vel_needed = false;
	}
	if (this.pos.y + this.dims[1]*0.5 >= screen_dims[1]) {
		this.vel.y = -this.max_speed;
		this.random_vel_needed = false;
	}
	else if (this.pos.y - this.dims[1]*0.5 <= 0) {
		this.vel.y = this.max_speed;
		this.random_vel_needed = false;
	}
};

// handles non wall boundary collisions accepting or rejecting particles based on their type
Particle.prototype.hit_boundary = function(boundary_pos, boundary_dims, allowed_through) {
	if (this.type != allowed_through) {
		var x_right = this.pos.x + this.dims[0] * 0.5 >= boundary_pos[0];
		var x_left = this.pos.x - this.dims[0] * 0.5 <= boundary_pos[0] + boundary_dims[0];
		var y_bottom = this.pos.y + this.dims[1] * 0.5 >= boundary_pos[1];
		var y_top = this.pos.y - this.dims[1] * 0.5 <= boundary_pos[1] + boundary_dims[1];
		if (x_right && x_left && y_top && y_bottom) {
			this.vel.mult(-1);
			this.random_vel_needed = false;
		}
	}
};