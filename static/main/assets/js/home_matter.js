var Engine = Matter.Engine,
    Render = Matter.Render,
    World = Matter.World,
    Bodies = Matter.Bodies;
    
var element = document.getElementById("about");
var world = {height: screen.height, width: screen.width, x: element.offsetLeft, y: element.offsetHeight}

console.log(world)
var engine = Engine.create();


 
var render = Render.create({
                engine: engine,
                canvas: document.getElementById("about-back"),
                options: {
                    width: world.width,
                    height: world.height,
                    wireframes: false,
                    background: 'transparent',
                }
             });

var vertices_ground = [{ x: 0, y: 100 }, { x: world.width, y: 100 }, { x: world.width , y: 10 }, { x: 0, y: 80 }];

var gnd = Matter.Vertices.create(vertices_ground);
var gnd_center = Matter.Vertices.centre(vertices_ground);

console.log(gnd)
console.log(gnd_center)



var DROP_LEFT = {path: "0 0 20 0 70 100 20 150 0 150 0 0"};

              
var boxA = Bodies.rectangle(400, 200, 80, 80);
var ballA = Bodies.circle(600, 100, 40, 10);
var ballB = Bodies.circle(600, 10, 40, 10);
var ground = path(world.x+gnd_center.x,  world.y-100+gnd_center.y);
 
World.add(engine.world, [ballA, ballB, ground]);
Engine.run(engine);
Render.run(render);

function path(x, y) {
    return Matter.Bodies.fromVertices(x, y, gnd, {
        isStatic: true,
    });
}