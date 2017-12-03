import pygame

class Screen2:
    width = 0
    height = 0
    screen = None

    list = []
    def __init__(self,screen,width,height):
        self.width=width
        self.screen=screen
        self.height=height

    def Start(self):
        finished=0
        while not finished:
            position = pygame.mouse.get_pos()   #마우스 위치 불러오기

            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for lists in self.list:
                        if lists == self.list[0]:
                            if lists.collidepoint(event.pos):   #Start를 눌렀을 때

                                finished=1                  #while문 종료
                                break

            self.screen.fill((0, 0, 0))     #검정색으로 칠하기

            pygame.font.init()              #폰트 초기화
            font = pygame.font.Font("resources/font/consola.ttf", 40)   #폰트 불러오기


            Startfont = pygame.font.Font("resources/font/consola.ttf", 40)  #폰트 불러오기
            Starttext = Startfont.render("Start", True, (225, 225, 225))        #Start객체 생성
            StarttextRect = Starttext.get_rect()
            StarttextRect.center = (600, 400)
            self.screen.blit(Starttext, StarttextRect)

            self.list = [StarttextRect]


            pygame.display.flip()   #화면 전체 업데이트