import pygame
import sys
import random
import time


class Snake():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
		

def changeDirTo(self,dir):
	if dir=="RIGHT" and not self.direction=="LEFT":
		self.direction=="RIGHT"
	if dir=="LEFT" and not self.direction=="RIGHT":
		self.direction=="LEFT"
	if dir=="UP" and not self.direction=="DOWN":
		self.direction=="RIGHT"
	if dir=="DOWN" and not self.direction=="UP":
		self.direction=="RIGHT"
def move(self,food):
 	if self.direction=="RIGHT":
 		self.position[0]=self.position[0]+10
 	if self.direction=="LEFT":
 		self.position[0]=self.position[0]-10
 	if self.direction=="UP":
 		self.position[1]=self.position[1]-10

 	if self.direction=="DOWN":
 		self.position[1]=self.position[1]+10
 	self.body.insert(0,list(self.position))
 	if self.position==food:
 		return 1
 	else
 		self.body.pop()
 		return 0

 def checkCollision(self):
 	if self.position[0]>490 or self.position[0]<0:
 	return 1
 elif self.position[1]>500 or self.position[1]<0:
 	return 1
 for bodyPart in self.body[1:]:
 	if self.position==bodyPart:
 		return 1
 	return 0

 def getHead Pos(self):
 	return self.position
 def getBody(self):
 	return self.body

 class FoodSpawer():
 def__init__(self):
 	self.position=[random.randrange[(1,50)*10,random.randrange(1,50)*10]
 	self.isfoodonscreen=True

 def spawnFood(self):
 	if self.isfoodonscreen==False:
 		self.position=random.randrange[(1,50)*10,random.randrange(1,50)*10]
 		self.isfoodonscreen=True
 	return self.position

 def setfoodonscreen(self,b):
 	self.isfoodonscreen=b

 window=pygame.display.set_mode((500,500))
 pygame.display,set_caption("The old days of snakes")
 fps=pygame.time.Clock()

 score=0

 snake=Snake()
 foodSpawner=FoodSpawer()

def gameOver():
	pygame.quit()
	sys.exit()

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT():
			gameOver();
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				snake.changeDirTo('RIGHT')
			if event.key==pygame.K_LEFT:
				snake.changeDirTo('LEFT')
			if event.key==pygame.K_UP:
				snake.changeDirTo('UP')
			if event.key==pygame.K_DOWN:
				snake.changeDirTo('DOWN')
		food=FoodSpawer.spawnFood()
		if(snake.move(food)==1):
			score=score+1
			foodSpawner.setfoodonscreen(False)

		window.fill(pygame.Color(225,225,225))
	for pos in snake.getBody():
		pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10)
		pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(food[0],food[1],10,10)
if (snake.checkCollision()==1):
	gameOver()
	pygame.display.set_caption("score:"+str(score))
	pygame.display.flip()
	fps.tick(24)


