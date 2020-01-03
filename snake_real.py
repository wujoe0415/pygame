import pygame, sys, time, random


#settings(global variables)

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Window size
frame_size_x = 720
frame_size_y = 480
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("snake")

score = 0
    

#snake
snake_pos = [300, 300]
snake_body = [[300, 300], [290, 300], [280, 300]]
direction = 'UP'
change_to = direction

#food
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()



#score
def show_Score(choice, color, font, size):
        global score
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x/10, 15)
        else:
            score_rect.midtop = (frame_size_x/2, frame_size_y/2)
        game_window.blit(score_surface, score_rect)
#restart
def restart(color, font, size):
        restart_font = pygame.font.SysFont(font, size)
        restart_surface = restart_font.render('press SPACE to restart', True, color)
        restart_rect = restart_surface.get_rect()
        restart_rect.midtop = (frame_size_x/2, frame_size_y/1.4)
        game_window.blit(restart_surface, restart_rect)
    
#gameover
def gameover():
        global score
        global red
        gameoverFont = pygame.font.SysFont('arial.ttf',54)
        gameoverSurf = gameoverFont.render('Game Over!',True,red)
        gameoverRect = gameoverSurf.get_rect()
        gameoverRect.midtop = (frame_size_x/2, frame_size_y/4)
        game_window.fill(black)
        game_window.blit(gameoverSurf, gameoverRect)
        show_Score(0,red,'times',20)
        restart(blue,'times',30)
        pygame.display.flip() #renew surface
        while True:
            keys=pygame.key.get_pressed()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    time.sleep(1) #stay 1 seconds
                    pygame.quit()
                

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        
                        global snake_pos
                        global snake_body
                        global direction
                        global change_to
                        score = 0
                        #snake
                        snake_pos = [300, 300]
                        snake_body = [[300, 300], [290, 300], [280, 300]]
                        direction = 'UP'
                        change_to = direction
                        main.running = True
                        pygame.display.update()
                        main()
                        break
            
   
#snake 
class Snake:
    def __init__(self):
        pass
        

    def make_sure():
        global direction 
        global change_to 
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

    def growing():
        global snake_body
        global score
        global food_spawn
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
           score += 1
           food_spawn = False
        else:
           snake_body.pop()

    def moving():
        global direction
        global snack_pos
        if direction == 'UP':
           snake_pos[1] -= 10
        if direction == 'DOWN':
           snake_pos[1] += 10
        if direction == 'LEFT':
           snake_pos[0] -= 10
        if direction == 'RIGHT':
           snake_pos[0] += 10


 
#food
class Food:

    def __init__(self):
        pass

    def spawing():
        global food_spawn
        global food_pos
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True
        

#main
def main():
    pygame.init()
    global change_to
    global snake_body
    global snake_pos
    running = True
    while running:
        game_window.fill(black)
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                
                
                

            elif event.type == pygame.KEYDOWN:
                # quit game
                if event.key == pygame.K_ESCAPE: 
                   pygame.quit()
                   exit(0)
                #w s a d
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'

        #oppisite way
        Snake.make_sure()
        Snake.moving()
        Snake.growing()
        Food.spawing()

        
        for pos in snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # food
        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))


        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
            gameover()
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            gameover()
        # Touching  body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                gameover()
            show_Score(1, white, 'consolas', 20)

        # Refresh game screen
        pygame.display.update()

        fps_controller.tick(30)

        


if __name__ == '__main__':
    main()
    pygame.quit()
   
   