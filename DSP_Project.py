import pygame, sys, time ,random     
from pygame.locals import * 

#遊戲視窗
WINDOW_WIDTH  = 695  
WINDOW_HEIGHT = 480

#遊戲生命值
TOTAL_LIFE = 5

#顏色參數
BACKGROUND_COLOR = (150, 150, 150)
BALL_COLOR       = (255, 255, 255)
PADDLE_COLOR     = (128,  64,  64)
BLOCK_COLOR      = (255, 128, 128)
TEXT_COLOR       = (255, 255, 255)
BLACK            = (  0,   0,   0)

#狀態參數
INITAL      = 0
GAME_LEVEL  = 1
RUN         = 3
GAMEOVER    = 4
EXIT        = 6
FPS         = 25
#球
BALL_START_Y = (WINDOW_HEIGHT//2)
BALL_SIZE    = 6
#檔板
PADDLE_START_X = (WINDOW_WIDTH/2 - 16)
PADDLE_START_Y = (WINDOW_HEIGHT  - 32)
PADDLE_WIDTH  = 70
PADDLE_HEIGHT = 10
#磚塊
NUM_BLOCK_ROWS    = 10
NUM_BLOCK_COLUMNS = 10
BLOCK_WIDTH       = 65
BLOCK_HEIGHT      = 15
BLOCK_X           = 0
BLOCK_Y           = 0
BLOCK_XGAP        = 70
BLOCK_YGAP        = 20

#初始化磚塊
def initBlock():
    block = []
    for i in range(NUM_BLOCK_ROWS):
        block.append([i+1] * NUM_BLOCK_COLUMNS)
    return block

#文字顯示        
def text(text, font ,surface, x, y):
    text_obj = font.render(text,1,TEXT_COLOR)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj,text_rect)

#離開遊戲
def exitOut():
    pygame.quit()
    sys.exit()

#初始化遊戲
pygame.init()  
clock = pygame.time.Clock()  
ball_x  = 0
ball_y  = 0
ball_dx = 0
ball_dy = 0
paddle_move_left  = True
paddle_move_right = True
paddle = {'rection':pygame.Rect(0,0,PADDLE_WIDTH,PADDLE_HEIGHT),'color':PADDLE_COLOR}                     
game_state = INITAL
life = TOTAL_LIFE
block = []
block_hit = 0
game_over = False
score = 0
level = 1
change = 0
game_over_font  = pygame.font.SysFont(None,48)
text_font       = pygame.font.SysFont(None,30)  
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)  
pygame.display.set_caption('BRICK!BRICK!BRICK!')
pygame.display.update()

#鍵盤的事件類型作出反應
while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:    
            exitOut()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_move_left = True
            if event.key == pygame.K_RIGHT:
                paddle_move_right = True
            if event.key == pygame.K_ESCAPE:
                exitOut()
            if event.key == pygame.K_SPACE:
                game_state = INITAL
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle_move_left = False
            if event.key == pygame.K_RIGHT:
                paddle_move_right = False
    #遊戲的流程以及初始化遊戲
    if game_state == INITAL:
        ball_x = random.randint(8 , WINDOW_WIDTH-8)
        ball_y = BALL_START_Y
        ball_dx = random.randint(-4, 4)
        ball_dy = random.randint( 6, 8)
        paddle['rection'].left = PADDLE_START_X
        paddle['rection'].top  = PADDLE_START_Y
        paddle_move_left = False
        paddle_move_right = False
        life = TOTAL_LIFE
        game_over = False
        blocks_hit = 0
        score = 0
        level = 1
        time = 20
        change = 0
        game_state = GAME_LEVEL
    #遊戲當前的level
    elif game_state == GAME_LEVEL:
        block = initBlock()
        target_x = 10-level
        target_y = random.randint(0,9)
        block[target_x][target_y] = -1
        target_hit = 0
        game_state = RUN
    #遊戲的運作
    elif game_state == RUN:
        time -= 1/FPS
        if (block_hit == 5*level 
            and block[target_x][target_y] != 0 
            and change != 1):
            block[target_x][target_y] = 1
            if(target_x == 0):
                target_x = 0
            target_x = (10-level)-1
            target_y = random.randint(0,9)
            block[target_x][target_y] = -1
            change = 1
            
        if time <= 0:
            time = 0
            game_state = GAMEOVER
        #球的運動    
        ball_x += ball_dx
        ball_y += ball_dy
        if ball_x > (WINDOW_WIDTH-BALL_SIZE) or ball_x < BALL_SIZE:
            ball_dx = -ball_dx
            ball_x += ball_dx
        elif ball_y < BALL_SIZE:
            ball_dy = -ball_dy
            ball_y += ball_dy
        elif ball_y > WINDOW_HEIGHT-BALL_SIZE:
            life -= 1
            if life == 0:
                game_state = GAMEOVER
            else:
                #再次初始化遊戲
                ball_x = paddle['rection'].left + PADDLE_WIDTH // 2
                ball_y = BALL_START_Y
                ball_dx = random.randint(-4,5)
                ball_dy = random.randint( 6,9)
        #球與檔板的碰撞
        if ball_y > WINDOW_HEIGHT // 2:
            if (ball_x+BALL_SIZE >= paddle['rection'].left 
                and ball_x-BALL_SIZE <= paddle['rection'].left+PADDLE_WIDTH 
                and ball_y+BALL_SIZE >= paddle['rection'].top 
                and ball_y-BALL_SIZE <= paddle['rection'].top+PADDLE_HEIGHT):  
                ball_dy = - ball_dy  
                ball_y += ball_dy
                if paddle_move_left:  
                    ball_dx -= random.randint(0, 3)  
                elif paddle_move_right:  
                    ball_dx += random.randint(0, 3)  
                else:  
                    ball_dx += random.randint(-1, 2) 
        #球與磚塊的碰撞
        cur_x = BLOCK_X
        cur_y = BLOCK_Y
        for row in range(NUM_BLOCK_ROWS):
            cur_x = BLOCK_X
            for col in range(NUM_BLOCK_COLUMNS):
                if block[row][col] != 0:  
                    if (ball_x+BALL_SIZE >= cur_x 
                        and ball_x-BALL_SIZE <= cur_x+BLOCK_WIDTH 
                        and ball_y+BALL_SIZE >= cur_y 
                        and ball_y-BALL_SIZE <= cur_y+BLOCK_HEIGHT):
                        #擊中黑色磚塊
                        if(block[row][col] == -1):
                            level       += 1  
                            block_hit   = 0  
                            score       += 1000
                            FPS         += 5
                            PADDLE_WIDTH+= 5
                            time        = 30-(5*(level-1))
                            game_state  = GAME_LEVEL
                        #擊中普通磚塊
                        block[row][col] = 0  
                        block_hit += 1
                        ball_dy = -ball_dy  
                        ball_dx += random.randint(-1, 2)  
                        score += 5 * (level + abs(ball_dx)) 
                        time  += 1
                            
                cur_x += BLOCK_XGAP  
            cur_y += BLOCK_YGAP  
        #檔板左右運動             
        if paddle_move_left:  
            paddle['rection'].left -= 15  
            if paddle['rection'].left < 0:  
                paddle['rection'].left = 0  
        if paddle_move_right:  
            paddle['rection'].left += 15  
            if paddle['rection'].left > WINDOW_WIDTH-PADDLE_WIDTH:  
                paddle['rection'].left = WINDOW_WIDTH-PADDLE_WIDTH  
        #畫背景、球、檔板   
        windowSurface.fill(BACKGROUND_COLOR)   
        pygame.draw.rect(windowSurface, paddle['color'], paddle['rection'])  
        pygame.draw.circle(windowSurface, BALL_COLOR, (ball_x, ball_y), BALL_SIZE, 0)
        #畫磚塊
        cur_x = BLOCK_X  
        cur_y = BLOCK_Y
        for row in range(NUM_BLOCK_ROWS):  
            cur_x = BLOCK_X   
            for col in range(NUM_BLOCK_COLUMNS):  
                if block[row][col] != 0 :
                    if(block[row][col] == -1):
                        pygame.draw.rect(windowSurface, BLACK,(cur_x, cur_y, BLOCK_WIDTH, BLOCK_HEIGHT))
                    else:
                        pygame.draw.rect(windowSurface, BLOCK_COLOR,(cur_x, cur_y, BLOCK_WIDTH, BLOCK_HEIGHT))
                cur_x += BLOCK_XGAP  
            cur_y += BLOCK_YGAP  
        #顯示Level、生命值、得分、時間
        message = 'Level: ' + str(level) + '    Life: ' + str(life) + '    Score: ' + str(score) + '       Time:' + str(time)
        text(message, text_font, windowSurface, 8, (WINDOW_HEIGHT - 16)) 
    #遊戲結束
    elif game_state == GAMEOVER:  
        text('GAME OVER', game_over_font, windowSurface,(WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))  
        text('Level: ' + str(level), game_over_font, windowSurface, (WINDOW_WIDTH / 3)+20, (WINDOW_HEIGHT / 3) + 50)  
        text('Score: ' + str(score), game_over_font, windowSurface, (WINDOW_WIDTH / 3)+20, (WINDOW_HEIGHT / 3) + 100)
        text('Press SPACE/ESC to PLAY/EXIT.', game_over_font, windowSurface,(WINDOW_WIDTH / 3)-150, (WINDOW_HEIGHT / 3) + 150)
        FPS = 25
        pygame.display.update()

    pygame.display.update()  
    clock.tick(FPS+level*1.5)   