#import math
from math import sin,cos,radians
from time import sleep
import os

GRAVITY = 9.81
DISTANCE = 40
RADIUS = 0.3
ROWS = 24
COLS = 80

def calculate_impact(velocity, angle):
    #z = (velocity**2 * math.sin(2* math.radians(angle))) / GRAVITY
    return (velocity**2 * sin(2* radians(angle))) / GRAVITY

def get_input():
    velocity = float(input("Podaj predkość"))
    #print(velocity)
    #angle = float(input("Podaj kąt"))


    """
    if 0 <= angle <= 90:
        print("Kąt jest dopuszczalny")
    else:
        print("Kąt nie jest dopuszczalny")
    """

    angle = None
    while not angle or not 0 <= angle <= 90:
        angle = float(input("Podaj kąt"))
    return velocity, angle

def shoot(position, velocity, angle):
    impact_position = calculate_impact(velocity, angle)
    print(impact_position)
    return abs(impact_position-position) < RADIUS

def draw_scene(x, y):
    for _ in range(y-1):
        print()
    for _ in range(x-1):
        print(" ", end="")
    print("o")
    for _ in range(y+1, ROWS-1):
        print()
    for _ in range(COLS):
        print("_", end="")

def draw_scene_adjusted(x, y):
    aspect_ratio = COLS/DISTANCE
    new_x = x*aspect_ratio
    new_y = ROWS- (y*aspect_ratio)/2

    draw_scene(int(new_x), int(new_y))

def clear():
    os.system("clear")

def animated_shot(velocity, angle):
    t=0
    t_max = 2 * velocity * sin(radians(angle)) / GRAVITY
    dt=0.05
    v_x = cos(radians(angle))*velocity
    v_y = sin(radians(angle)) * velocity
    while t < t_max:
        x=v_x*t
        y=v_y*t - (GRAVITY* t**2)/2
        clear()
        draw_scene_adjusted(int(x), int(y))
        t+=dt
        sleep(dt)



def main():
    player = 1
    while True:
        print(f"GRACZ {player}")
        velocity, angle = get_input()
        animated_shot(velocity, angle)
        shot = shoot(DISTANCE, velocity, angle)
        """
        if(player == 1):
            shot = shoot(DISTANCE, velocity, angle)
        else:
            shot = shoot(0, velocity, angle-180)

        if shot:
            print(f"GRACZ {player} wygrał")
            break
        player = 3-player
        """

if __name__ == '__main__':
    main()
    #animated_shot(20,45)

