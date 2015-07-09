var Points = [];
var Lines = [];
var Voltage;
var Resistance = 2;
var count = 0;
var hold = 1;
function setup(){
    frameRate = 30
    colorMode(RGB, 255)
    red = color(255,0,0);
    green = color(0,255,0);
    blue = color(125, 249, 255)
    white = color(255)
    createCanvas(600,300);
    Points.push(new Point(0,100,0),
		new Point(600,100,0),
		new Point(0,200,0),
		new Point(600,200,0)
	       );
    Lines.push(new Line(Points[0],Points[1]),
	       new Line(Points[2],Points[3])
	      );
    firstEmitter = new Emitter(590,150);

    Voltage = createSlider(0,10,1)
    Voltage.position(20,40)
}

function draw(){
    
    background(50);
    //START TEXT//
    textSize(18);
    textAlign(ENTER)
    stroke(white)
    fill(white)
    text("Voltage", 90, 30);
    text('0V',550,230)
    text('+'+Voltage.value()+'V',10,230)

    //END TEXT//
    for(var i = 0;i < Points.length;i++){
	Points[i].display(white);
    }
    for(var i = 0; i < Lines.length; i++){
	Lines[i].display(white);
    }
    for(var i = 0 ;i<Voltage.value(); i++){
	firstEmitter.addParticle();
    }
    count = 0
    if(frameCount%60 == 0){
	for(var i = 0; i < firstEmitter.particles.length; i++){
	    if(firstEmitter.particles[i].position.x >300 && firstEmitter.particles[i].position.x <550){
		count += 1
	    }
	}
	hold = count
    }
    
    text('Current = '+ Math.ceil(hold)/10+'A',250,230)
    firstEmitter.run();
    
}

//Class for points
var Point = function(x_position,y_position,radius){
    this.position = createVector(x_position,y_position);
    this.radius = radius;
    this.moveable = false;
}

//display the point
Point.prototype.display = function(colour){
    fill(colour);
    ellipse(this.position.x,this.position.y,this.radius*2,this.radius*2);
}

//Class for lines
var Line = function(start,end){
    this.start = start;
    this.end = end;
    this.asVector = p5.Vector.sub(this.end.position,this.start.position);
    this.Normalised = this.asVector.normalize();
    //Get the bounding box for the line
    this.UpperLeft = createVector(Math.min(this.start.position.x, this.end.position.x), Math.min(this.start.position.y,this.end.position.y));
    this.LowerRight = createVector(Math.max(this.start.position.x, this.end.position.x), Math.max(this.start.position.y,this.end.position.y));
}

//Update the line to give a new vector and the normalised vector
Line.prototype.update = function(){
    this.asVector = p5.Vector.sub(this.end.position,this.start.position);
    this.Normalised = this.asVector.normalize();
    this.UpperLeft = createVector(Math.min(this.start.position.x, this.end.position.x), Math.min(this.start.position.y,this.end.position.y));
    this.LowerRight = createVector(Math.max(this.start.position.x, this.end.position.x), Math.max(this.start.position.y,this.end.position.y));
}

//Display the line
Line.prototype.display = function(colour){
    stroke(colour)
    line(this.start.position.x,this.start.position.y,this.end.position.x,this.end.position.y)
}

//Class for emitter
    var Emitter = function(x_position, y_position){
    this.origin = createVector(x_position,y_position)
    this.particles = []
}

//Method to add particles
Emitter.prototype.addParticle = function(){
    this.particles.push(new Particle(this.origin))
}
//Method to start emitter
Emitter.prototype.run = function(){
    for(var i = this.particles.length -1; i>=0; i--){
	var p = this.particles[i];
	p.run();
	if(p.isDead()==true){
	    this.particles.splice(i,1);
	}
    }
}

//Class for particles
var Particle = function(position){
//    this.acceleration = createVector(0,0);
    this.acceleration = createVector(-Voltage.value()/20,0);
//    this.velocity = createVector(random(-Voltage.value(),0),random(-3,3));
    this.velocity = createVector(random(0,0),random(-3,3));
    this.width = createVector(0,random(-45,45));
    this.position = p5.Vector.add(position,this.width);
    this.lifespan = 100;
    this.radius = 5
    this.colour = blue;
}

//Method to run each frame for the particle
Particle.prototype.run = function(){
    this.update();
    this.display();
}

//Method to update particles each frame
Particle.prototype.update = function(){
    this.lifespan--;
    this.possCollision()
    this.acceleration = createVector(-Voltage.value()/20,0);
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
}

//Method to draw particles
Particle.prototype.display = function(){
    fill(this.colour);
    ellipse(this.position.x, this.position.y,this.radius*2,this.radius*2)
}

//Method to kill particles
Particle.prototype.isDead = function(){
    var isDead;
    if(this.position.x > width || this.position.x < 0  || this.position.y > height || this.position.y < 0){
	isDead = true
    }
    return isDead
}

//Method to check possible collision
Particle.prototype.possCollision = function(){
    for(var i = 0; i < Lines.length; i++){
	if(this.position.x > (Lines[i].UpperLeft.x - this.radius) && this.position.x < (Lines[i].LowerRight.x + this.radius)){
	    if(this.position.y > (Lines[i].UpperLeft.y -this.radius) && this.position.y < Lines[i].LowerRight.y + this.radius){
	    this.collision(Lines[i]);
	    }
	}
    }
}

//Function to determine whether a collision has occured. Turn it into a prototype and add in the changes in velocity
Particle.prototype.collision = function(lineSegment){
    var collision;
    var Projection = calcProjection(lineSegment.Normalised,p5.Vector.sub(this.position,lineSegment.start.position))
    var closest = closestPoint(lineSegment,Projection)
    fill(255,0,0)
//    ellipse(closest.x,closest.y,5,5)
    var shortestDistance = p5.Vector.sub(this.position,closest)
    if((this.radius*this.radius) > (p5.Vector.dot(shortestDistance,shortestDistance))){
	VelocityLine = p5.Vector.mult(lineSegment.Normalised,(p5.Vector.dot(lineSegment.Normalised,this.velocity)));
	VelocityNorm = p5.Vector.mult(shortestDistance.normalize(),(p5.Vector.dot(shortestDistance.normalize(),this.velocity)));
	VelocityNorm.mult(-1)
	this.velocity = p5.Vector.add(VelocityLine,VelocityNorm)
	this.velocity.mult(1/Resistance)
	this.position.add(this.velocity)
//	this.update()
    }
}

//Calculate projection of A onto B (A needs to be normalised)
function calcProjection(AVector,BVector){
    var projection = p5.Vector.mult(AVector,(p5.Vector.dot(AVector,BVector)))
    return projection
}

//Calculate closest point on linesegment to particle
function closestPoint(lineVector,projection){
    var q = p5.Vector.add(lineVector.start.position,projection);
    if(q.x < lineVector.UpperLeft.x){
	q.x = lineVector.UpperLeft.x
    }
    else if(q.x > lineVector.LowerRight.x){
	q.x = lineVector.LowerRight.x
    }
    if(q.y < lineVector.UpperLeft.y){
	q.y = lineVector.UpperLeft.y
    }
    else if(q.y > lineVector.LowerRight.y){
	q.y = lineVector.LowerRight.y
    }
    return q
}
	
//Move Points elements to mouse x,y
function mouseDragged(){
    for (var i = 0; i < Points.length; i++){
	if(Points[i].moveable == true){
	    Points[i].position.x = mouseX;
	    Points[i].position.y = mouseY;
	}
    }
    for (var i = 0; i < Lines.length; i++){
	Lines[i].update();
    }
}

//Check if a point has been clicked on and allow the point to move
function mousePressed(){
    for (var i = 0; i < Points.length; i++){
	var point = Points[i];
	if(mouseX > (point.position.x - point.radius) && mouseX < (point.position.x + point.radius) && mouseY < (point.position.y +point.radius) && mouseY > (point.position.y - point.radius)){
	    point.moveable = true;
	}
    }
}

//Stop all points being moved when mouse is released
function mouseReleased(){
   for (var i = 0; i < Points.length; i++){
       Points[i].moveable = false;
   }
}
