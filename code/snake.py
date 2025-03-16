import pygame as pg
import random

pg.init()
pg.mixer.init()

yellow = (255, 255, 102)
red = (213, 50, 80)
green = (71, 167, 106)
green_snake = (0, 69, 36)

dis_width = 600
dis_height = 500
dis = pg.display.set_mode((dis_width, dis_height))
pg.display.set_caption('Змейка!')

clock = pg.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pg.font.SysFont(None, 25)
score_font = pg.font.SysFont(None, 35)

pg.mixer.music.load('music.mp3')
pg.mixer.music.play()
 
def score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
def snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, green_snake, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 25, dis_height / 2])
 
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while game_over != True:
        while game_close == True:
            dis.fill(green)

            message("Вы проиграли. Нажмите Q чтобы выйти или C для повторной игры", red)
            score(length_snake - 1)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        gameLoop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(green)

        pg.draw.rect(dis, red, [food_x, food_y, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        score(length_snake - 1)

        pg.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            length_snake += 1
        clock.tick(snake_speed)
    pg.quit()

gameLoop()