
let sheep = [];

let death_pr = {
	"AA": 0.004,
	"aa": 0.004,
	"Aa": 0.001,
	"aA": 0.001
};

class Sheep {
	constructor(genotype){
		this.pos = createVector(0,0);
		this.vel = p5.Vector.random2D();
		this.speed = 1;
		this.vel.mult(this.speed);
		this.genotype = genotype;
		this.phenotype = genotype == "aa" ? "blue" : "black";
		this.isdead = false;
	}
	render(){
		if(!this.isdead){
			if (Math.random() < death_pr[this.genotype]){
				this.die();
			}
			else{
				push();
				translate(this.pos.x, this.pos.y);
				scale(Math.sign(this.vel.x), 1);
				image(imgs[this.phenotype], 0,0);
				pop();
			} 
		}
	}
	update() {
		this.pos.add(this.vel);
		if (this.pos.x > width)
			this.pos.x %= width
		if(this.pos.x < 0)
			this.pos.x += width
		if (this.pos.y > height)
			this.pos.y %= height
		if(this.pos.y < 0)
			this.pos.y += height
		let head = this.vel.heading();
		if(Math.random()< 0.1){
			head += Math.random()*0.1;
		}
		this.vel = p5.Vector.fromAngle(head);
		this.vel.mult(this.speed);
	}
	die() {

	}
}

let imgs = {
}

function setup(){
	createCanvas(800,500);
	imgs["black"] = loadImage("dogBlack.png")
	imgs["blue"] = loadImage("dogBlue.png")

	for(let i = 0; i< 10; i++){
		sheep.push(new Sheep("AA"));
	}
	for(let i = 0; i< 10; i++){
		sheep.push(new Sheep("Aa"));
	}
	for(let i = 0; i< 10; i++){
		sheep.push(new Sheep("aa"));
	}
}

function draw(){
	background(211,211,211);
	for( let i in sheep){
		sheep[i].render();
		sheep[i].update();
	}
	
}


