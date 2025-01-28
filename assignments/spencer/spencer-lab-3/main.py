# importing libraries
import pygame
import asyncio

# importing project modules
import game
import snake
import fruit
import wall

async def main():
	# Initialising game
	game_window = game.init()

	# setting default snake direction towards right
	direction = 'RIGHT'
	change_to = direction

	# Setup fruit
	fruit.init()
	
	# Main Function
	while True:
		
		# handling key events
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					change_to = 'UP'
				if event.key == pygame.K_s:
					change_to = 'DOWN'
				if event.key == pygame.K_a:
					change_to = 'LEFT'
				if event.key == pygame.K_d:
					change_to = 'RIGHT'

		# We don't want the new direction to be the
		# opposite of the current one
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'

		# Moving the snake
		if direction == 'UP':
			snake.position[1] -= 10
		if direction == 'DOWN':
			snake.position[1] += 10
		if direction == 'LEFT':
			snake.position[0] -= 10
		if direction == 'RIGHT':
			snake.position[0] += 10

		# Check if the fruit was eaten #TODO
		snake.move()
#spawn a fruit if a fruit is not present It also adds a new wall and ensures the walls are not overlapping with the fruits
		if fruit.spawn == False:
			fruit.spawn = True
			fruit.position = fruit.locate()
			wall.add_wall()	
			for block in wall.walls_on_screen:
				while fruit.position == block:
					fruit.position = fruit.locate()

		# Fill the game background
		game.fill(game_window)
		
		# Move the snake body
		snake.draw(game_window)

		# Spawn the fruit randomly
		fruit.draw(game_window)

		#spawn walls randomly on the screen
		wall.draw(game_window)
	


	
		
		#adding some stuff to try to make the snake pop out the other side. WOrks but there is an interesting edge case at the top that is hard to make happen but the graphics go wonky and you randomly die.
		if snake.position[0] <= 0:
			snake.position[0] = game.window_x 
		elif snake.position[0] >= game.window_x:
			snake.position[0] = 0
		if snake.position[1]<= 0:
			snake.position[1] = game.window_y 
		elif snake.position[1] >= game.window_y:
			snake.position[1] = 0

		# Touching the snake body
		# Implement game over conditions if the snake touches itself #TODO
		for block in snake.body[1:]:
			if snake.position == block:
				game.game_over(game_window)
		
	
		#mostly working wall collision
		for walls in wall.walls_on_screen:
			if snake.position == walls:
				game.game_over(game_window)
			

		# Refresh game
		game.update(game_window)
		await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())