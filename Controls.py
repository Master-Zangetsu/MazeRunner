from turtle import Screen, Turtle

class Controls():
    
    turtle;
    screen;

    def u():
        print("Up");
        turtle.forward(1);

    def createControls(turtle, screen):
        
        screen.onkey(u, "Up");
        screen.listen();
    
    