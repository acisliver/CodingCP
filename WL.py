#게임 종료시 나타나는 win or fail문구
import pygame

class WL:
    exitcode=0
    screen=None

    def __init__(self,screen):
        self.screen=screen

    def print(self):
        pygame.font.init()              #폰트 초기화
        font=pygame.font.Font("resources/font/consola.ttf",100)     #폰트 불러오기
        text=font.render("Game Over",True,(255, 0, 0))                 #빨간색 폰트 객체 생성
        textRect=text.get_rect()                                        #폰트 위치 불러오기
        textRect.center=(600,400)                                       #폰트 위치 지정
        self.screen.blit(text,textRect)                                 #폰트 블릿



        finisher = True
        while finisher:


            for event in pygame.event.get():            #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            pygame.display.flip()