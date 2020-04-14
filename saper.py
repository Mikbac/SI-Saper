
import time

import pygame

from examplesOfTheDecisionTreeAndNeuralNetworks.nnExample import nn
from examplesOfTheDecisionTreeAndNeuralNetworks.treeExample import clf



graph = {'0 0': set(['0 1', '1 0']),
         '0 1': set(['0 0', '0 2', '1 1']),
         '0 2': set(['0 1', '0 3', '1 2']),
         '0 3': set(['0 2', '0 4', '1 3']),
         '0 4': set(['0 3', '0 5', '1 4']),
         '0 5': set(['0 4', '0 6', '1 5']),
         '0 6': set(['0 5', '0 7', '1 6']),
         '0 7': set(['0 6', '0 8', '1 7']),
         '0 8': set(['0 7', '0 9', '1 8']),
         '0 9': set(['0 8', '0 10', '1 9']),
         '0 10': set(['0 9', '0 11', '1 10']),
         '0 11': set(['0 10', '0 12', '1 11']),
         '0 12': set(['0 11', '0 13', '1 12']),
         '0 13': set(['0 12', '0 14', '1 13']),
         '0 14': set(['0 13', '1 14']),

         '1 0': set(['0 0', '1 1', '2 0']),
         '1 1': set(['0 1', '1 0', '2 1', '1 2']),
         '1 2': set(['0 2', '1 1', '2 2', '1 3']),
         '1 3': set(['0 3', '1 2', '2 3', '1 4']),
         '1 4': set(['0 4', '1 3', '2 4', '1 5']),
         '1 5': set(['0 5', '1 4', '2 5', '1 6']),
         '1 6': set(['0 6', '1 5', '2 6', '1 7']),
         '1 7': set(['0 7', '1 6', '2 7', '1 8']),
         '1 8': set(['0 8', '1 7', '2 8', '1 9']),
         '1 9': set(['0 9', '1 8', '2 9', '1 10']),
         '1 9': set(['0 9', '1 8', '2 9', '1 10']),
         '1 10': set(['0 10', '1 9', '2 10', '1 11']),
         '1 11': set(['0 11', '1 10', '2 11', '1 12']),
         '1 12': set(['0 12', '1 11', '2 12', '1 13']),
         '1 13': set(['0 13', '1 12', '2 13', '1 14']),
         '1 14': set(['0 14', '1 13', '2 14']),

         '2 0': set(['1 0', '2 1', '3 0']),
         '2 1': set(['1 1', '2 0', '3 1', '2 2']),
         '2 2': set(['1 2', '2 1', '3 2', '2 3']),
         '2 3': set(['1 3', '2 2', '3 3', '2 4']),
         '2 4': set(['1 4', '2 3', '3 4', '2 5']),
         '2 5': set(['1 5', '2 4', '3 5', '2 6']),
         '2 6': set(['1 6', '2 5', '3 6', '2 7']),
         '2 7': set(['1 7', '2 6', '3 7', '2 8']),
         '2 8': set(['1 8', '2 7', '3 8', '2 9']),
         '2 9': set(['1 9', '2 8', '3 9', '2 10']),
         '2 10': set(['1 10', '2 9', '3 10', '2 11']),
         '2 11': set(['1 11', '2 10', '3 11', '2 12']),
         '2 12': set(['1 12', '2 11', '3 12', '2 13']),
         '2 13': set(['1 13', '2 12', '3 13', '2 14']),
         '2 14': set(['1 14', '2 13', '3 14']),

         '3 0': set(['2 0', '3 1', '4 0']),
         '3 1': set(['2 1', '3 0', '4 1', '3 2']),
         '3 2': set(['2 2', '3 1', '4 2', '3 3']),
         '3 3': set(['2 3', '3 2', '4 3', '3 4']),
         '3 4': set(['2 4', '3 3', '4 4', '3 5']),
         '3 5': set(['2 5', '3 4', '4 5', '3 6']),
         '3 6': set(['2 6', '3 5', '4 6', '3 7']),
         '3 7': set(['2 7', '3 6', '4 7', '3 8']),
         '3 8': set(['2 8', '3 7', '4 8', '3 9']),
         '3 9': set(['2 9', '3 8', '4 9', '3 10']),
         '3 10': set(['2 10', '3 9', '4 10', '3 11']),
         '3 11': set(['2 11', '3 10', '4 11', '3 12']),
         '3 12': set(['2 12', '3 11', '4 12', '3 13']),
         '3 13': set(['2 13', '3 12', '4 13', '3 14']),
         '3 14': set(['2 14', '3 13', '4 14']),

         '4 0': set(['3 0', '4 1', '5 0']),
         '4 1': set(['3 1', '4 0', '5 1', '4 2']),
         '4 2': set(['3 2', '4 1', '5 2', '4 3']),
         '4 3': set(['3 3', '4 2', '5 3', '4 4']),
         '4 4': set(['3 4', '4 3', '5 4', '4 5']),
         '4 5': set(['3 5', '4 4', '5 5', '4 6']),
         '4 6': set(['3 6', '4 5', '5 6', '4 7']),
         '4 7': set(['3 7', '4 6', '5 7', '4 8']),
         '4 8': set(['3 8', '4 7', '5 8', '4 9']),
         '4 9': set(['3 9', '4 8', '5 9', '4 10']),
         '4 10': set(['3 10', '4 9', '5 10', '4 11']),
         '4 11': set(['3 11', '4 10', '5 11', '4 12']),
         '4 12': set(['3 12', '4 11', '5 12', '4 13']),
         '4 13': set(['3 13', '4 12', '5 13', '4 14']),
         '4 14': set(['3 14', '4 13', '5 14']),

         '5 0': set(['4 0', '5 1', '6 0']),
         '5 1': set(['4 1', '5 0', '6 1', '5 2']),
         '5 2': set(['4 2', '5 1', '6 2', '5 3']),
         '5 3': set(['4 3', '5 2', '6 3', '5 4']),
         '5 4': set(['4 4', '5 3', '6 4', '5 5']),
         '5 5': set(['4 5', '5 4', '6 5', '5 6']),
         '5 6': set(['4 6', '5 5', '6 6', '5 7']),
         '5 7': set(['4 7', '5 6', '6 7', '5 8']),
         '5 8': set(['4 8', '5 7', '6 8', '5 9']),
         '5 9': set(['4 9', '5 8', '6 9', '5 10']),
         '5 10': set(['4 10', '5 9', '6 10', '5 11']),
         '5 11': set(['4 11', '5 10', '6 11', '5 12']),
         '5 12': set(['4 12', '5 11', '6 12', '5 13']),
         '5 13': set(['4 13', '5 12', '6 13', '5 14']),
         '5 14': set(['4 14', '5 13', '6 14']),

         '6 0': set(['5 0', '6 1', '7 0']),
         '6 1': set(['5 1', '6 0', '7 1', '6 2']),
         '6 2': set(['5 2', '6 1', '7 2', '6 3']),
         '6 3': set(['5 3', '6 2', '7 3', '6 4']),
         '6 4': set(['5 4', '6 3', '7 4', '6 5']),
         '6 5': set(['5 5', '6 4', '7 5', '6 6']),
         '6 6': set(['5 6', '6 5', '7 6', '6 7']),
         '6 7': set(['5 7', '6 6', '7 7', '6 8']),
         '6 8': set(['5 8', '6 7', '7 8', '6 9']),
         '6 9': set(['5 9', '6 8', '7 9', '6 10']),
         '6 10': set(['5 10', '6 9', '7 10', '6 11']),
         '6 11': set(['5 11', '6 10', '7 11', '6 12']),
         '6 12': set(['5 12', '6 11', '7 12', '6 13']),
         '6 13': set(['5 13', '6 12', '7 13', '6 14']),
         '6 14': set(['5 14', '6 13', '7 14']),

         '7 0': set(['6 0', '7 1', '8 0']),
         '7 1': set(['6 1', '7 0', '8 1', '7 2']),
         '7 2': set(['6 2', '7 1', '8 2', '7 3']),
         '7 3': set(['6 3', '7 2', '8 3', '7 4']),
         '7 4': set(['6 4', '7 3', '8 4', '7 5']),
         '7 5': set(['6 5', '7 4', '8 5', '7 6']),
         '7 6': set(['6 6', '7 5', '8 6', '7 7']),
         '7 7': set(['6 7', '7 6', '8 7', '7 8']),
         '7 8': set(['6 8', '7 7', '8 8', '7 9']),
         '7 9': set(['6 9', '7 8', '8 9', '7 10']),
         '7 10': set(['6 10', '7 9', '8 10', '7 11']),
         '7 11': set(['6 11', '7 10', '8 11', '7 12']),
         '7 12': set(['6 12', '7 11', '8 12', '7 13']),
         '7 13': set(['6 13', '7 12', '8 13', '7 14']),
         '7 14': set(['6 14', '7 13', '8 14']),

         '8 0': set(['7 0', '8 1', '9 0']),
         '8 1': set(['7 1', '8 0', '9 1', '8 2']),
         '8 2': set(['7 2', '8 1', '9 2', '8 3']),
         '8 3': set(['7 3', '8 2', '9 3', '8 4']),
         '8 4': set(['7 4', '8 3', '9 4', '8 5']),
         '8 5': set(['7 5', '8 4', '9 5', '8 6']),
         '8 6': set(['7 6', '8 5', '2 6', '8 7']),
         '8 7': set(['7 7', '8 6', '9 7', '8 8']),
         '8 8': set(['7 8', '8 7', '9 8', '8 9']),
         '8 9': set(['7 9', '8 8', '9 9', '8 10']),
         '8 10': set(['7 10', '8 9', '9 10', '8 11']),
         '8 11': set(['7 11', '8 10', '9 11', '8 12']),
         '8 12': set(['7 12', '8 11', '9 12', '8 13']),
         '8 13': set(['7 13', '8 12', '9 13', '8 14']),
         '8 14': set(['7 14', '8 13', '9 14']),

         '9 0': set(['8 0', '9 1', '10 0']),
         '9 1': set(['8 1', '9 0', '10 1', '9 2']),
         '9 2': set(['8 2', '9 1', '10 2', '9 3']),
         '9 3': set(['8 3', '9 2', '10 3', '9 4']),
         '9 4': set(['8 4', '9 3', '10 4', '9 5']),
         '9 5': set(['8 5', '9 4', '10 5', '9 6']),
         '9 6': set(['8 6', '9 5', '10 6', '9 7']),
         '9 7': set(['8 7', '9 6', '10 7', '9 8']),
         '9 8': set(['8 8', '9 7', '10 8', '9 9']),
         '9 9': set(['8 9', '9 8', '10 9', '9 10']),
         '9 10': set(['8 10', '9 9', '10 10', '9 11']),
         '9 11': set(['8 11', '9 10', '10 11', '9 12']),
         '9 12': set(['8 12', '9 11', '10 12', '9 13']),
         '9 13': set(['8 13', '9 12', '10 13', '9 14']),
         '9 14': set(['8 14', '9 13', '10 14']),

         '10 0': set(['9 0', '10 1', '11 0']),
         '10 1': set(['9 1', '10 0', '11 1', '10 2']),
         '10 2': set(['9 2', '10 1', '11 2', '10 3']),
         '10 3': set(['9 3', '10 2', '11 3', '10 4']),
         '10 4': set(['9 4', '10 3', '11 4', '10 5']),
         '10 5': set(['9 5', '10 4', '11 5', '10 6']),
         '10 6': set(['9 6', '10 5', '11 6', '10 7']),
         '10 7': set(['9 7', '10 6', '11 7', '10 8']),
         '10 8': set(['9 8', '10 7', '11 8', '10 9']),
         '10 9': set(['9 9', '10 8', '11 9', '10 10']),
         '10 10': set(['9 10', '10 9', '11 10', '10 11']),
         '10 11': set(['9 11', '10 10', '11 11', '10 12']),
         '10 12': set(['9 12', '10 11', '11 12', '10 13']),
         '10 13': set(['9 13', '10 12', '11 13', '10 14']),
         '10 14': set(['9 14', '10 13', '11 14']),

         '11 0': set(['10 0', '11 1', '12 0']),
         '11 1': set(['10 1', '11 0', '12 1', '11 2']),
         '11 2': set(['10 2', '11 1', '12 2', '11 3']),
         '11 3': set(['10 3', '11 2', '12 3', '11 4']),
         '11 4': set(['10 4', '11 3', '12 4', '11 5']),
         '11 5': set(['10 5', '11 4', '12 5', '11 6']),
         '11 6': set(['10 6', '11 5', '12 6', '11 7']),
         '11 7': set(['10 7', '11 6', '12 7', '11 8']),
         '11 8': set(['10 8', '11 7', '12 8', '11 9']),
         '11 9': set(['10 9', '11 8', '12 9', '11 10']),
         '11 10': set(['10 10', '11 9', '12 10', '11 11']),
         '11 11': set(['10 11', '11 10', '12 11', '11 12']),
         '11 12': set(['10 12', '11 11', '12 12', '11 13']),
         '11 13': set(['10 13', '11 12', '12 13', '11 14']),
         '11 14': set(['10 14', '11 13', '12 14']),

         '12 0': set(['11 0', '12 1', '13 0']),
         '12 1': set(['11 1', '12 0', '13 1', '12 2']),
         '12 2': set(['11 2', '12 1', '13 2', '12 3']),
         '12 3': set(['11 3', '12 2', '13 3', '12 4']),
         '12 4': set(['11 4', '12 3', '13 4', '12 5']),
         '12 5': set(['11 5', '12 4', '13 5', '12 6']),
         '12 6': set(['11 6', '12 5', '13 6', '12 7']),
         '12 7': set(['11 7', '12 6', '13 7', '12 8']),
         '12 8': set(['11 8', '12 7', '13 8', '12 9']),
         '12 9': set(['11 9', '12 8', '13 9', '12 10']),
         '12 10': set(['11 10', '12 9', '13 10', '12 11']),
         '12 11': set(['11 11', '12 10', '13 11', '12 12']),
         '12 12': set(['11 12', '12 11', '13 12', '12 13']),
         '12 13': set(['11 13', '12 12', '13 13', '12 14']),
         '12 14': set(['11 14', '12 13', '13 14']),

         '13 0': set(['12 0', '13 1', '14 0']),
         '13 1': set(['12 1', '13 0', '14 1', '13 2']),
         '13 2': set(['12 2', '13 1', '14 2', '13 3']),
         '13 3': set(['12 3', '13 2', '14 3', '13 4']),
         '13 4': set(['12 4', '13 3', '14 4', '13 5']),
         '13 5': set(['12 5', '13 4', '14 5', '13 6']),
         '13 6': set(['12 6', '13 5', '14 6', '13 7']),
         '13 7': set(['12 7', '13 6', '14 7', '13 8']),
         '13 8': set(['12 8', '13 7', '14 8', '13 9']),
         '13 9': set(['12 9', '13 8', '14 9', '13 10']),
         '13 10': set(['12 10', '13 9', '14 10', '13 11']),
         '13 11': set(['12 11', '13 10', '14 11', '13 12']),
         '13 12': set(['12 12', '13 11', '14 12', '13 13']),
         '13 13': set(['12 13', '13 12', '14 13', '13 14']),
         '13 14': set(['12 14', '13 13', '14 14']),

         '14 0': set(['13 0', '14 1', ]),
         '14 1': set(['13 1', '14 0', '14 2']),
         '14 2': set(['13 2', '14 1', '14 3']),
         '14 3': set(['13 3', '14 2', '14 4']),
         '14 4': set(['13 4', '14 3', '14 5']),
         '14 5': set(['13 5', '14 4', '14 6']),
         '14 6': set(['13 6', '14 5', '14 7']),
         '14 7': set(['13 7', '14 6', '14 8']),
         '14 8': set(['13 8', '14 7', '14 9']),
         '14 9': set(['13 9', '14 8', '14 10']),
         '14 10': set(['13 10', '14 9', '14 11']),
         '14 11': set(['13 11', '14 10', '14 12']),
         '14 12': set(['13 12', '14 11', '14 13']),
         '14 13': set(['13 13', '14 12', '14 14']),
         '14 14': set(['14 13', '13 14', ])}


# 1 - grass - green
# 2 - bomb - red
# 3 - dynamite - orange
# 4 - disarmed bomb - blue

def paint_picture():
	for row in range(15):
		pygame.event.get()
		for column in range(15):
			color = WHITE
			if grid[row][column] == 1:
				color = GREEN
			elif grid[row][column] == 2:
				color = RED
			elif grid[row][column] == 3:
				color = ORANGE
			elif grid[row][column] == 4:
				color = BLUE
			pygame.draw.rect(screen,
			                 color,
			                 [(MARGIN + WIDTH) * column + MARGIN,
			                  (MARGIN + HEIGHT) * row + MARGIN,
			                  WIDTH,
			                  HEIGHT])
	pygame.display.flip()


def bfs(graph, start):
	visited, queue = set(), [start]
	global grid
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			answer = nn.detection(nn, ((int(vertex.split(' ', 1)[1]) + 1) + (int(vertex.split(' ', 1)[0]) * 15)))
			paint_picture()
			if (answer == 1) or (answer == 2):
				if answer == 1:
					grid[int(vertex.split(' ', 1)[0])][int(vertex.split(' ', 1)[1])] = 2
				elif answer == 2:
					grid[int(vertex.split(' ', 1)[0])][int(vertex.split(' ', 1)[1])] = 3
				if clf.test() == 1:
					visited.add(vertex)
					grid[int(vertex.split(' ', 1)[0])][int(vertex.split(' ', 1)[1])] = 4
				else:
					queue.append(vertex)
			elif answer == 0:
				visited.add(vertex)
				grid[int(vertex.split(' ', 1)[0])][int(vertex.split(' ', 1)[1])] = 1
			print(vertex)
			queue.extend(graph[vertex] - visited)
			time.sleep(.100)
	return visited


vec = pygame.math.Vector2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 128)

WIDTH = 20
HEIGHT = 20

MARGIN = 5

grid = []
for row in range(15):
	grid.append([])
	for column in range(15):
		grid[row].append(0)

grid[0][0] = 1

pygame.init()

WINDOW_SIZE = [382, 382]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Array Backed Grid")

done = False

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(15):
				for j in range(15):
					grid[i][j] = 0
			# User clicks the mouse. Get the position
			pos = pygame.mouse.get_pos()
			bfs(graph, '0 0')
			# Change the x/y screen coordinates to grid coordinates
			column = pos[0] // (WIDTH + MARGIN)
			row = pos[1] // (HEIGHT + MARGIN)
			# Set that location to one
			grid[row][column] = 1
			print("Click ", pos, "Grid coordinates: ", row, column)
			matrix = [[]]

	screen.fill(BLACK)

	paint_picture()

	clock.tick(10)

# pygame.quit()
