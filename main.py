import pygame

WINDOW_SIZE = [800, 800]

pygame.init()
font = pygame.font.SysFont('arial', 15, True)
X = font.render('X', True, (226, 0, 0))
Y = font.render('O', True, (0, 0, 0))
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
clock.tick(60)
width, height = 50, 50


def init():
    tab = [[0 for _ in range(width)] for _ in range(height)]
    tab[25][25] = 1
    return tab


drawTab = init()


def getNeighbors(y, x):
    dy = [0, 0, 1, -1]
    dx = [-1, 1, 0, 0]
    counter: int = 0
    for i in range(len(dx)):
        ix = (x + dx[i]) % width
        iy = (y + dy[i]) % height
        counter = counter + drawTab[iy][ix]
    return counter


def getTabNeighbors():
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            grid[y][x] = getNeighbors(y, x)
    return grid


def spread(grid):
    counter: int = 0
    neighbors = getTabNeighbors()
    for y in range(height):
        counter += 1
        for x in range(width):
            if grid[y][x] == 0:
                if neighbors[y][x] == 1:
                    grid[x][y] = 1
            if grid[y][x] == 1:
                grid[y - 1][x - 1] = 1
        if (x + 1) < width:
            grid[y - 1][x + 1] = 1


def draw():
    while True:
        spread(drawTab)
        screen.fill((225, 225, 225))
        for row in range(50):
            for column in range(50):
                if drawTab[row][column] == 1:
                    screen.blit(X, [column * 17, row * 19])
                else:
                    screen.blit(Y, [column * 17, row * 19])
        clock.tick(5)
        pygame.display.flip()
    pygame.quit()


draw()
