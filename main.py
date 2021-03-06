import math
import pygame

width = 1000
height = 1000
hheight = height/2
step = 10
xStep = step
yStep = step

def field_func(x, y, count, scale) -> int:
    # if the return is 1 the coords are "inside"
    # if the return is 0 the coords are "outside"

    # this is just some silly function

    # x = angle
    alpha = (x*(count/100)) % 360

    sinY = scale*4*math.sin(math.radians(alpha))+hheight

    if abs(y-sinY) < 25: return 1

    return 0


# fix color for drawing
color = (10, 120, 20)
bg_color = (0, 0, 0)


class MCube2D:
    def __init__(self, posX, posY, xStep, yStep) -> None:
        self.x = posX
        self.y = posY
        self.xStep = xStep
        self.yStep = yStep

    def draw(self, screen, count, scale) -> None:
        x = self.x
        y = self.y
        xh = x+self.xStep/2
        yh = y+self.yStep/2
        xf = x+self.xStep
        yf = y+self.yStep

        x0y0 = field_func(x, y, count, scale)
        x1y0 = field_func(xf, y, count, scale)
        x1y1 = field_func(xf, yf, count, scale)
        x0y1 = field_func(x, yf, count, scale)

        case = x0y0 * 1
        case += x1y0 * 2
        case += x1y1 * 4
        case += x0y1 * 8

        # 0 0
        # 0 0
        if case == 0:
            return
        # 1 0
        # 0 0
        if case == 1:
            pygame.draw.polygon(screen, color, [(x, y), (xh, y), (x, yh)])
        # 0 1
        # 0 0
        if case == 2:
            pygame.draw.polygon(screen, color, [(xh, y), (xf, y), (xf, yh)])
        # 1 1
        # 0 0
        if case == 3:
            pygame.draw.polygon(
                screen, color, [(x, y), (xf, y), (xf, yh), (x, yh)])
        # 0 0
        # 0 1
        if case == 4:
            pygame.draw.polygon(screen, color, [(xf, yh), (xf, yf), (xh, yf)])
        # 1 0
        # 0 1
        if case == 5:
            pygame.draw.polygon(
                screen, color, [(x, y), (xh, y), (xf, yh), (xf, yf), (xh, yf), (x, yh)])
        # 0 1
        # 0 1
        if case == 6:
            pygame.draw.polygon(
                screen, color, [(xh, y), (xf, y), (xf, yf), (xh, yf)])
        # 1 1
        # 0 1
        if case == 7:
            pygame.draw.polygon(
                screen, color, [(x, y), (xf, y), (xf, yf), (xh, yf), (x, yh)])
        # 0 0
        # 1 0
        if case == 8:
            pygame.draw.polygon(screen, color, [(x, yh), (xh, yf), (x, yf)])
        # 1 0
        # 1 0
        if case == 9:
            pygame.draw.polygon(
                screen, color, [(x, y), (xh, y), (xh, yf), (x, yf)])
        # 0 1
        # 1 0
        if case == 10:
            pygame.draw.polygon(
                screen, color, [(xh, y), (xf, y), (xf, yh), (xh, yf), (x, yf), (x, yh)])
        # 1 1
        # 1 0
        if case == 11:
            pygame.draw.polygon(
                screen, color, [(x, y), (xf, y), (xf, yh), (xh, yf), (x, yf)])
        # 0 0
        # 1 1
        if case == 12:
            pygame.draw.polygon(
                screen, color, [(x, yh), (xf, yh), (xf, yf), (x, yf)])
        # 1 0
        # 1 1
        if case == 13:
            pygame.draw.polygon(
                screen, color, [(x, y), (xh, y), (xf, yh), (xf, yf), (x, yf)])
        # 0 1
        # 1 1
        if case == 14:
            pygame.draw.polygon(
                screen, color, [(xh, y), (xf, y), (xf, yf), (x, yf), (x, yh)])
        # 1 1
        # 1 1
        if case == 15:
            pygame.draw.polygon(
                screen, color, [(x, y), (xf, y), (xf, yf), (x, yf)])


cubes = []
# initiate all cubes
for x in range(0, width, xStep):
    for y in range(0, height, yStep):
        cube = MCube2D(x, y, xStep, yStep)
        cubes.append(cube)

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode([width, height])

count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick()
    fps = clock.get_fps()

    count += 1
    # Fill the background
    screen.fill(bg_color)

    # draw all cubes
    for cube in cubes:
        # pass in some "random" value
        cube.draw(screen, count, fps)

    # Flip the display
    pygame.display.flip()


pygame.quit()
