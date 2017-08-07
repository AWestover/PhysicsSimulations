//Text column functions

function text_column(x, y) {
	// x and y refer to the top left corner of the first character in the string
	this.x = x;
	this.y = y;
	this.num_chars = round(random(5, 20));
	this.drop_speed = round(random(3, 6));
	this.set_random_chars();
	this.switchRate = random(30, 60);
};


// make the list of characters in unicode
text_column.prototype.set_random_chars = function() {
	this.char_list = [];
	for (var i = 0; i < this.num_chars; i++) {
		var next_rand_char = gen_random_character(); 
		this.char_list.push(next_rand_char);
	}
}


// draws the colum of text
text_column.prototype.display = function() {
	for (var i = 0; i < this.num_chars; i++) {
		fill(0, 255, 0);
		textSize(char_text_size);
		text(this.char_list[i], this.x, this.y + char_text_size*i);
		if (random(0, this.switchRate) < 1) {
			this.char_list[i] = gen_random_character();
		}
	}
}


// moves the columns down the page and recycles ones that are past the bottom of the canvas
text_column.prototype.update = function(dt) {
	if (this.y < screen_dims[1]) {
		this.y += this.drop_speed*dt;
	}
	else {
		this.y = round(random(-screen_dims[1], -this.num_chars*char_text_size));
	}
}


// gets a random greek unicode letter
function gen_random_character() {
	return String.fromCharCode(round(random(945, 970)));
}

