from turtle import Turtle, Screen

class Maze():
    
    xWalls = {};
    yWalls = {};

    def generateMazeBoundries(mazeWidth):
    
        turtle = Turtle();
        screen = Screen();
        
        turtle.hideturtle();
        turtle.penup();
        turtle.forward(mazeWidth/2);
        turtle.right(90);
        turtle.forward(mazeWidth/2);
        turtle.right(90);
        turtle.forward(mazeWidth);
        turtle.right(90);
        turtle.pendown();
        
        for i in range(4):
            turtle.forward(mazeWidth);
            turtle.right(90);
    
        return Maze.generateMazePath(turtle, mazeWidth);
        
    def generateMazePath(turtle, mazeWidth):
        
        currentx = 0 - (mazeWidth/2);
        currenty = 0 - (mazeWidth/2);
        
        currenty = Maze.drawYLine(50, currentx, currenty, turtle);
        currentx = Maze.drawXLine(100, currentx, currenty, turtle);
        currenty = Maze.drawYLine(100, currentx, currenty, turtle);
        currentx = Maze.drawXLine(50, currentx, currenty, turtle);        
        currenty = Maze.drawYLine(75, currentx, currenty, turtle);
        currentx = Maze.drawXLine(100, currentx, currenty, turtle);
        currenty = Maze.drawYLine(50, currentx, currenty, turtle);
        currentx = Maze.drawXLine(40, currentx, currenty, turtle);
        currenty = Maze.drawYLine(25, currentx, currenty, turtle);
        
        currentx = Maze.drawXLine(10, currentx, currenty, turtle);
        
        currenty = Maze.drawYLine(-35, currentx, currenty, turtle);
        currentx = Maze.drawXLine(-40, currentx, currenty, turtle);
        currenty = Maze.drawYLine(-50, currentx, currenty, turtle);
        currentx = Maze.drawXLine(-100, currentx, currenty, turtle);
        currenty = Maze.drawYLine(-75, currentx, currenty, turtle);
        currentx = Maze.drawXLine(-50, currentx, currenty, turtle);
        currenty = Maze.drawYLine(-100, currentx, currenty, turtle);
        currentx = Maze.drawXLine(-100, currentx, currenty, turtle);
        currenty = Maze.drawYLine(-40, currentx, currenty, turtle);
        
        return turtle;
    
    def drawXLine(xProgression, currentX, currentY, turtle):
        
        newXCord = xProgression + currentX;
        turtle.goto(newXCord, currentY);
        
        fromCords = str(currentX) + '|' + str(currentY);
        toCords = str(newXCord) + '|' + str(currentY);
        
        Maze.xWalls[fromCords] = toCords;
        
        return newXCord;
    
    def drawYLine(yProgression, currentX, currentY, turtle):
        
        newYCord = yProgression + currentY;
        turtle.goto(currentX, newYCord);
        
        fromCords = str(currentX) + '|' + str(currentY);
        toCords = str(currentX) + '|' + str(newYCord);
        
        Maze.yWalls[fromCords] = toCords;
        
        return newYCord;

    def collectTurtle(mazeWidth):
        
        turtle = Maze.generateMazeBoundries(mazeWidth);
        mazeWalls = {'xWalls' : Maze.xWalls, 'yWalls' : Maze.yWalls};
        
        return mazeWalls;