import pygame
import colors
from params import *
from Environment import Board
from Agent import Agent

# initialize:
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Search Game")

# setting start and end point :
start = {'x': 6, 'y': 0}
end = {'x': 12, 'y': 0}

gameBoard = Board(start, end)
agent = Agent(gameBoard)
# agent.bfs()
# agent.dfs()



def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors.black)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gameBoard.draw_world(WIN)

        pos = pygame.mouse.get_pos()  # gets the current mouse coords
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(rows):
                for j in range(cols):
                    rect = gameBoard.boardArray[i][j]
                    if rect.is_inside_me(pos):

                        if event.button == 1:
                            gameBoard.boardArray[i][j].block()
                        if event.button == 3:
                            gameBoard.boardArray[i][j].unblock()

        
        




    pygame.quit()


main()
