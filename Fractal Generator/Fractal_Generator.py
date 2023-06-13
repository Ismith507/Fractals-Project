import pygame, sys
from pygame.locals import *

#initializing pygame
pygame.init()

#Create window with given dimensions
width = 480
height = 480
screen = pygame.display.set_mode((width, height))
Black = [0, 0, 0]
White = [255, 255, 255]
screen.fill(White)
pygame.display.set_caption("Mandelbrot Set")
pygame.display.flip()


def main():
    generate(-2.0, 1.0, -1.6)

def generate(minReal, maxReal, minImaginary):
    # Defining complex plane coordinates
    minReal = minReal
    maxReal = maxReal
    minImaginary = minImaginary
    maxImaginary = minImaginary+(maxReal-minReal)*height/width
    realFactor = (maxReal - minReal)/(width-1)
    ImaginaryFactor = (maxImaginary - minImaginary)/(height-1)
    maxIterations = 100

    # Computing Mandelbrot set
    for y in range(0, height - 1):
        c_Imaginary = maxImaginary - y*ImaginaryFactor
        for x in range(0, width - 1):
            c_Real = minReal + x*realFactor

            Z_Real = c_Real
            Z_Imaginary = c_Imaginary
            isInside = True

            for n in range(0, maxIterations - 1):
                Z_RealSquared = Z_Real*Z_Real
                Z_ImaginarySquared = Z_Imaginary*Z_Imaginary

                if(Z_RealSquared + Z_ImaginarySquared > 4):
                    isInside = False
                    if(n < maxIterations/2-1):
                        screen.set_at((x,y), [((255/(maxIterations/2))*n), 0, 0])
                    if(n > maxIterations/2-1):
                        screen.set_at((x,y), [255, (255/maxIterations)*(n-maxIterations/2), (255/maxIterations)*(n-maxIterations/2)])

            
                Z_Imaginary = 2*Z_Real*Z_Imaginary + c_Imaginary
                Z_Real = Z_RealSquared - Z_ImaginarySquared + c_Real

            if(isInside):
                screen.set_at((x,y), Black)

        pygame.display.update()

    # Window controls
    """
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                generate(minReal, maxReal, (minImaginary + (minImaginary/10)
            if keys[K_DOWN]:
            minImaginary -= minImaginary/10
            if keys[K_LEFT]:
            minReal -= (maxReal-minReal)/10
            maxReal -= (maxReal-minReal)/10
            if keys[K_RIGHT]:
            minReal += (maxReal-minReal)/10
            maxReal += (maxReal-minReal)/10
            if keys[K_PAGEUP]:
            minReal = minReal*.9
            maxreal = maxreal*.9
            minImaginary = minImaginary*.9
            if keys[K_PAGEDOWN]:
            minReal = minReal/.9
            maxreal = maxreal/.9
            minImaginary = minImaginary/.9
    """
main()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

