var SliderR;
var SliderB;
var SliderG;
var R = 120;
var B = 120;
var G = 120;

function setup(){
    
    createCanvas(200, 250);
    // create a slider (min, max, default value)
    SliderR = createSlider(0, 255, 255);
    SliderG = createSlider(0, 255, 255);
    SliderB = createSlider(0, 255, 255);
    SliderR.position(25, 25);
    SliderG.position(25, 50);
    SliderB.position(25, 75);

}

function draw(){
    background(R,G,B);
    R = SliderR.value();
    B = SliderB.value();
    G = SliderG.value();
    textAlign(CENTER);
    textFont("Arial");
    textSize(16);
    fill(100)
    text("R : " + SliderR.value(),width/2,125);
    text("G : " + SliderG.value(),width/2,150); 
    text("B : " + SliderB.value(),width/2,175); 
}
