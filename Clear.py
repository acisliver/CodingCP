import pygame

class Clear:
    width = 0
    height = 0
    screen = None
    clearimg = pygame.image.load("resources/images/clear.png")

    def __init__(self,screen,width,height):
        self.width=width
        self.screen=screen
        self.height=height

    def Start(self):
        finisher = True
        while finisher:
            position = pygame.mouse.get_pos()  # 마우스 위치 불러오기

            for event in pygame.event.get():  # 종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                self.screen.fill((125, 254, 116))
                self.screen.blit(self.clearimg, (200, 100))

            pygame.display.flip()

