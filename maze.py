import turtle
import math
import random
wn=turtle.Screen()
wn.bgcolor("white")
wn.title("A maze game")
wn.setup(700,700)
wn.tracer(0)
#Create pen 
class Pen(turtle.Turtle):
	def __init__(self):
			turtle.Turtle.__init__(self)
			self.shape("square")
			self.color("gray")
			self.penup()
			self.speed(0)
			
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("black")
		self.penup()
		self.speed(10)
		self.gold =0
	def go_up(self):
		#self.goto(self.xcor(),self.ycor() + 24)
		#calculate the spot to move to
		move_to_x = player.xcor()
		move_to_y = player.ycor() + 24
		
		if(move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
			
	def go_down(self):
		#self.goto(self.xcor(),self.ycor() - 24)
		#calculate the spot to move to
		move_to_x = player.xcor()
		move_to_y = player.ycor() - 24
		
		if(move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
	def go_left(self):
		#self.goto(self.xcor() - 24,self.ycor())
		#calculate the spot to move to
		move_to_x = player.xcor() - 24
		move_to_y = player.ycor() 
		
		if(move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
	
	def go_right(self):
		#self.goto(self.xcor() + 24,self.ycor())
		#calculate the spot to move to
		move_to_x = player.xcor() + 24
		move_to_y = player.ycor() 
		
		if(move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
	
	def is_collision(self,other):
		a=self.xcor()-other.xcor()
		b=self.ycor()-other.ycor()
		distance=math.sqrt((a**2)+(b**2))
		if distance<5:
			return True
		else:
			return False

class Treasure(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("triangle")
		self.color("yellow")
		self.penup()
		self.speed(0)
		self.gold=100
		self.goto(x,y)
		
	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()

class Enemy(turtle.Turtle):
		def __init__(self,x,y):
			turtle.Turtle.__init__(self)
			self.shape("circle")
			self.color("red")
			self.penup()
			self.speed(0)
			self.gold = 25
			self.goto(x,y)
			self.direction = random.choice(["up","down","left","right"])
		
		def move(self):
			if self.direction=="up":
				dx=0
				dy=24
			elif self.direction=="down":
				dx=0
				dy=-24
			elif self.direction=="left":
				dx=-24
				dy=0
				self.shape("circle")
			elif self.direction=="right":
				dx=24
				dy=0
				self.shape("circle")
			else:
				dx=0
				dy=0
			#calculate the spot to move to
			move_to_x=self.xcor()+dx
			move_to_y=self.ycor()+dy
			
			#check if the space has a wall
			if(move_to_x,move_to_y) not in walls:
				self.goto(move_to_x,move_to_y)
			else:
				#choose a different direction
				self.direction=random.choice(["up","down","left","right"])
			#set timer to move next time
			turtle.ontimer(self.move,t=random.randint(100,300))	
		def destroy(self):
			self.goto(2000,2000)
			self.hideturtle()
			
#set score
score=50
#draw score
ps=turtle.Turtle()
ps.speed(0)
ps.color("black")
ps.penup()
ps.setposition(-200,300)
s="Player Gold: %s" %score
ps.write(s,False,align="center",font=("Verdana",15,"bold"))
ps.hideturtle()
#create levels list
levels=[""]
 
#define first levels
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XX             XX   TX",
"X  XX   XXXXXXX   XX  XXX",
"X  XX   XX        XX    X",
"X  XX   XXE       XX    X",
"X       XX              X",
"XXXXXX  XXXXXXXXXXXXXXXXX",
"X       XX              X",
"XXXXXX  XX  EXX        EX",
"X            XX   XX    X",
"X            XX   XX  XXX",
"XET          XX   XX   TX",
"XXXXXXXXXXXX  XXXXXXXXXXX",
"XETXXE           XX    TX",
"X  XX            XX     X",
"X  XX            XX     X",
"X  XX                   X",
"X               XXXXXXXXX",
"XXXXXXXXXXXXX   XXXXXXXXX",
"XT XX                  TX",
"X  XX                  EX",
"X  XX               XX  X",
"X                   XX  X",
"X                  EXX TX",
"XXXXXXXXXXXXXXXXXXXXXXXXX", 
]
#Add a treasures list
treasures=[]

#Add a enemies list
enemies=[]

#Add maze to mazes list
levels.append(level_1)

#Create level setup Function

def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			#get the character at each x,y coordinate
			#note the order of y and x in the next lin
			character=level[y][x]
			#calculate the screen x,y coordinates
			screen_x=-288+(x*24)
			screen_y=288-(y*24)
			
			#Check if it is an X (representing a wall)
			if character =="X":
				pen.goto(screen_x,screen_y)
				pen.stamp()
				#Add coordinates to wall list
				walls.append((screen_x,screen_y))
			#check if it is a P(representing the player)
			if character=="P":
				player.goto(screen_x,screen_y)
			if character=="T":
				treasures.append(Treasure(screen_x,screen_y))
			if character=="E":
				enemies.append(Enemy(screen_x,screen_y))
			
#create class instances
pen=Pen()
player=Player()

#create wall coordinate list
walls = []

#set up the level
setup_maze(levels[1])

#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")


#Turn off screen updates
wn.tracer(0)

#start moving enemies
for enemy in enemies:
	turtle.ontimer(enemy.move,t=250)

#main game loop
while True:
	pass
	for treasure in treasures:
		if player.is_collision(treasure):
			score=score+treasure.gold
			s="Player Gold: %s"%score
			ps.clear()
			ps.write(s,False,align="center" ,font=("Verdana",15,"bold"))
			print("Player Gold: ",format(player.gold))
			treasure.destroy()
			treasures.remove(treasure)
	for enemy in enemies:
		if player.is_collision(enemy):
			score=treasure.gold-100
			s="Player Gold:%s"%score
			ps.clear()
			ps.write(s,False,align="center",font=("Verdana",15,"bold"))
			print("Player Gold:",format(player.gold))
			#print("You are die!!")
	
	
	#update screen
	wn.update()
	
