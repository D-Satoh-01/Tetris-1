import pygame, sys
from game import Game
from colors import Colors

pygame.init()

font_1 = pygame.font.Font(None, 40)
score_surface = font_1.render("Score", True, Colors.white)
next_surface = font_1.render("Next", True, Colors.white)
game_over_surface = font_1.render("Game Over", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

# nミリ秒ごとにGAME_UPDATEイベントをトリガーするタイマー
GAME_UPDATE = pygame.USEREVENT
update_time = 600


while True:
    for event in pygame.event.get():
        pygame.time.set_timer(GAME_UPDATE, update_time)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        # GAME_UPDATEイベントがトリガーされたときの処理
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
            if update_time >= 70:
                update_time -= 1
            
    # 描画
    score_value_surface = font_1.render(str(game.score), True, Colors.white)
    
    screen.fill((45,50,55))
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
        
    pygame.draw.rect(screen, Colors.light_grey, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_grey, next_rect, 0, 10)
    game.draw(screen)
            
    pygame.display.update()
    clock.tick(60)