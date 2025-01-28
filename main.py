import pygame
from constants import *
from player import *
from circleshape import *
from asteroids import *
from asteroidfield import *

print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    field = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    SCORE = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for spirit in drawable:
            spirit.draw(screen)
        for spirit in updatable:
            spirit.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid) == True:
                print(f"Game over! You scored {SCORE} points!")
                return
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    SCORE += 1
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()