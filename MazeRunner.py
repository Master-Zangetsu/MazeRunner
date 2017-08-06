import Maze
from turtle import Turtle, Screen

def initialiseMaze():
    
    mazeWidth = 300;
    mazeXStart = 0 - (mazeWidth/2) + 5;
    mazeYStart = 0 - (mazeWidth/2) + 11;

    print(Maze.Maze.collectTurtle(mazeWidth));

    turtle = Turtle();
    turtle.hideturtle();
    turtle.penup();
    turtle.goto(mazeXStart, mazeYStart);
    turtle.left(90);
    turtle.showturtle();

initialiseMaze();


