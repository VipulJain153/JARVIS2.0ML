from nlp import TakeCommand,speak
from Commands import Operator
import pygame,threading,cv
from sys import exit as close
pygame.init()
SCREEN = pygame.display.set_mode((1280,720))
pygame.display.set_caption('JARVIS')
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()
thread = threading.Thread(target=cv.run)
kit = "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"
if __name__ == "__main__":
    speak('Hello, I am Jarvis Sir, How can I Serve You.')
    while True:
        SCREEN.blit(pygame.image.load('bg.jpg').convert_alpha(),(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
        print('Listening...')
        query = TakeCommand()
        print(f"\n\nUser: {query}" if 'error@44324324' not in query else "")
        if 'error@44324324' in query:
            pass
        else:
            Operator(query)
        thread.run()
        clock.tick(60)
