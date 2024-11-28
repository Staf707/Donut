import os
import pygame
from math import cos, sin, tan, radians, pi, sqrt
from numpy import matrix
WHITE = (255,255,255)
BLACK = (0,0,0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60

pixel_width = 20
pixel_height = 20

x_pixel = 0
y_pixel = 0

screen_width = WIDTH // pixel_width # 40
screen_height = HEIGHT // pixel_height # 40
screen_size = screen_width * screen_height

FOV = 5
FOV_rad = radians(FOV)

K2 = 70
spacing = 1

A = 0
B = 0
C = 0
pygame.init()
pause = True
chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption('Cube')
font = pygame.font.SysFont('Arial', 20, bold=True)


def text_display(char, x, y):
    text = font.render(str(char), True, WHITE)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
k = 0
def calculate_luminance(vx, vy, vz):
    # Light direction L(0, 1, -1)
    L = (0, 1, -1)
    L_magnitude = sqrt(L[0]**2 + L[1]**2 + L[2]**2)
    L_normalized = (L[0] / L_magnitude, L[1] / L_magnitude, L[2] / L_magnitude)

    # Normal vector v(x, y, z)
    v_magnitude = sqrt(vx**2 + vy**2 + vz**2)
    if v_magnitude == 0:
        return 0  # Avoid division by zero

    v_normalized = (vx / v_magnitude, vy / v_magnitude, vz / v_magnitude)

    # Dot product
    dot_product = (L_normalized[0] * v_normalized[0] +
                   L_normalized[1] * v_normalized[1] +
                   L_normalized[2] * v_normalized[2])

    # Clamp to [0, 1]
    luminance = max(0, dot_product)

    return luminance


running = True
while running:
    clock.tick(FPS)
    scale = 1 / (tan(FOV*pi / 180)/ 2)
    screen.fill(BLACK)

    # code
    
    output = [' '] * screen_size
    zbuffer = [0] * screen_size
    for x in range(-20, 21):
        for y in range(-20, 21):
            for z in range(-20,21):
                if x == -20 or x == 20 or y == -20 or y == 20 or z == -20 or z == 20:
                    cosA = cos(A)
                    sinA = sin(A)
                    cosB = cos(B)
                    sinB = sin(B)
                    cosC = cos(C)
                    sinC = sin(C)
                    xr = cosA * x + sinA * z 
                    yr = y * cosB - (-sinA * x + cosA * z) * sinB
                    zr = y * sinB + (-sinA * x + cosA * z) * cosB

                    xt = xr * cosC - sinC * yr
                    yt = xr * sinC + cosC * yr
                    zt = zr

                    # other point in plane
                    x2 = x
                    y2 = y
                    if z == -20 or z== 20: x2 += 1
                    elif y == -20 or y ==20: x2 += 1
                    else: y2 += 1
                    xt2 = cosA * x2 + sinA * z
                    yt2 = y2 * cosB - (-sinA * x2 + cosA * z) * sinB
                    zt2 = y2 * sinB + (-sinA * x2 + cosA * z) * cosB
                    ooz = 1 / (zt + K2)
                    Np = (xt2-xt, yt2 - yt, zt2 - zt)
                    # x and y projection
                    xp = int(screen_width / 2 + (xt/(zt + K2)) * scale)
                    yp = int(screen_height / 2 - (yt/(zt + K2)) * scale)
                    # dot product    
                    position = xp + screen_width * yp
                    if len(output) > abs(position) and xp < screen_width and yp < screen_height:
                        if ooz > zbuffer[position]:
                            
                            if z == -20: output[position] = chars[5]
                            elif z == 20: output[position] = chars[6]
                            elif y == -20: output[position] = chars[7]
                            elif y == 20: output[position] = chars[9]
                            elif x == -20: output[position] = chars[8]
                            elif x == 20: output[position] = chars[10]

                            zbuffer[position] = ooz


    for i in range(screen_height):
        y_pixel += pixel_height
        for i in range(screen_width):
            x_pixel += pixel_width
            text_display(output[k], x_pixel, y_pixel)
            k += 1
        x_pixel = 0
    y_pixel = 0
    k = 0

    if not pause:
        A += 0.05
        B += 0.05
        C -= 0.02
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            pause = not pause

    
