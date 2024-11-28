import os
import pygame
from math import cos, sin
WHITE = (255,255,255)
BLACK = (0,0,0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60

pixel_width = 20
pixel_height = 20

x_pixel = 0
y_pixel = 0

screen_width = WIDTH // pixel_width
screen_height = HEIGHT // pixel_height
screen_size = screen_width * screen_height

A, B = 0, 0 


theta_spacing = 10
phi_spacing = 3



R1 = 10
R2 = 20
K2 = 200
K1 = screen_height * K2 * 3 / (8 * (R1+R2))
print(K1)
pygame.init()

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 20, bold=True)


def text_display(char, x, y):
    text = font.render(str(char), True, WHITE)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
k = 0
running = True
while running:
    clock.tick(FPS)

    screen.fill(BLACK)

    # code

    output = [' '] * screen_size
    zbuffer = [0] * screen_size

    for theta in range(0,628, theta_spacing):
        for phi in range(0,628, phi_spacing):
            costheta = cos(theta)
            sintheta = sin(theta)
            cosphi = cos(phi)
            sinphi = sin(phi)
            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)
            # x, y coordinates before rotating
            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z
            print(x, y, z)
            # x, y projection
            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 -K1 * ooz * y)

            position = xp + screen_width * yp

         
            L  = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (cosA * sintheta - costheta * sinA * sinphi)

            if ooz > zbuffer[position]:
                zbuffer[position] == ooz
                luminance_index = int(L * 8)
                output[position] = chars[luminance_index if luminance_index> 0 else 0]


    for i in range(screen_height):
        y_pixel += pixel_height
        for i in range(screen_width):
            x_pixel += pixel_width
            text_display(output[k], x_pixel, y_pixel)
            k += 1
        x_pixel = 0
    y_pixel = 0
    k = 0

    A += 0.15
    B += 0.035
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
