import os
import pygame
from math import cos, sin, tan, radians, pi, sqrt, acos, degrees
import time
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

natural_light = False
colour = True
def text_display(char, x, y):
    if colour:
        t = time.time()

        red = int((sin(t) + 1) / 2 * 255)
        green = int((sin(t + 2) + 1) / 2 * 255)
        blue = int((sin(t + 4) + 1) / 2 * 255)

        text = font.render(str(char), True, (red, green, blue))
    else: text = font.render(str(char), True, WHITE)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
k = 0

def angle_to_value(u, v):
    # Calculate the dot product and magnitudes of the vectors
    dot_product = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
    magnitude_u = sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    magnitude_v = sqrt(v[0]**2 + v[1]**2 + v[2]**2)

    # Calculate the cosine of the angle
    cos_theta = dot_product / (magnitude_u * magnitude_v)

    # Clip the cosine value to avoid numerical errors outside the range [-1, 1]
    cos_theta = max(-1, min(1, cos_theta))

    # Calculate the angle in radians and convert to degrees
    angle_rad = acos(cos_theta)
    angle_deg = degrees(angle_rad)

    # Normalize the angle to a range between 0 and 12
    value = 11 * (angle_deg / 90)

    # Ensure the value is between 0 and 12
    value = max(0, min(12, value))
    
    return value
def plane_vector(x,y,z,xt, yt, zt):
    x2 = x
    y2 = y
    if z == -20 or z== 20: x2 += 0.01
    elif y == -20 or y ==20: x2 += 0.01
    else: y2 += 0.01
    xr2 = cosA * x2 + sinA * z
    yr2 = y2 * cosB - (-sinA * x2 + cosA * z) * sinB
    zr2 = y2 * sinB + (-sinA * x2 + cosA * z) * cosB

    xt2 = xr2 * cosC - sinC * yr2
    yt2 = xr2 * sinC + cosC * yr2
    zt2 = zr2

    return (xt - xt2,yt - yt2,zt - zt2)
    
running = True
while running:
    clock.tick(FPS)
    scale = 1 / (tan(FOV*pi / 180)/ 2)
    screen.fill(BLACK)

    # code
    cosA = cos(A)
    sinA = sin(A)
    cosB = cos(B)
    sinB = sin(B)
    cosC = cos(C)
    sinC = sin(C)
    output = [' '] * screen_size
    zbuffer = [0] * screen_size
    for x in range(-20, 21, spacing):
        for y in range(-20, 21, spacing):
            for z in range(-20,21, spacing):
                if x == -20 or x == 20 or y == -20 or y == 20 or z == -20 or z == 20:
                    
                    xr = cosA * x + sinA * z 
                    yr = y * cosB - (-sinA * x + cosA * z) * sinB
                    zr = y * sinB + (-sinA * x + cosA * z) * cosB

                    xt = xr * cosC - sinC * yr
                    yt = xr * sinC + cosC * yr
                    zt = zr

                    # other point in plane
                    ooz = 1 / (zt + K2)
                    # x and y projection
                    xp = int(screen_width / 2 + (xt/(zt + K2)) * scale)
                    yp = int(screen_height / 2 - (yt/(zt + K2)) * scale)
                    # dot product    
                    position = xp + screen_width * yp

                    if len(output) > abs(position) and xp < screen_width and yp < screen_height:
                        if ooz > zbuffer[position]:

                            zbuffer[position] = ooz

                            if natural_light:
                                L_dir = (0,1,-1)
                                v = plane_vector(x,y,z, xt, yt, zt)
                                luminance = int(angle_to_value(v,L_dir) -1)
                                output[position] = chars[luminance if luminance> 0 else 0]
                            
                            else:
                                if x == -20:output[position] = chars[0]
                                elif x == 20:output[position] = chars[2]
                                elif y == 20: output[position] = chars[6]
                                elif y == -20:output[position] = chars[9]
                                elif z == 20:output[position] = chars[11]
                                elif z == -20:output[position] = chars[4]



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

    
