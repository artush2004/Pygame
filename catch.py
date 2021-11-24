import pygame
from random import randrange

def display(size):
    pygame.init()
    sc = pygame.display.set_mode([size, size])
    return sc

def game(sc, size, sn):
    score = 0
    orange = randrange(0, size, sn), 0
    orange_im = pygame.image.load("orange.jpg")
    basket = 0, 540
    basket_im = pygame.image.load("basket.jpg")
    clock = pygame.time.Clock()
    fps = 1
    f_sc = pygame.font.SysFont("Arial", 26, bold=True)
    while True:
        sc.fill("green")
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        if orange[1] >= 540:
            end(size, sc)
        sc.blit(orange_im, orange)
        sc.blit(basket_im, basket)
        r_score = f_sc.render(f"SCORE: {score}", 1, pygame.Color("white"))
        sc.blit(r_score, (5, 5))
        basket = move(basket, size, sn)
        orange = orange_move(orange, fps)
        if orange[1] >= 510 and orange[0] == basket[0]:
            orange = randrange(0, size, sn), 0
            score += 1
            fps += 1

        clock.tick(10)
        pygame.display.flip()

def move(basket, size, sn):
    x = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and basket[0] > 0:
        x = -1
    if key[pygame.K_RIGHT] and basket[0] < size-sn:
        x = 1
    basket = basket[0] + (x*sn), 540
    return basket

def orange_move(orange, fps):
    orange = orange[0], orange[1] + fps * 5
    return orange

def end(size, sc):
    while True:
        f_end = pygame.font.SysFont("Arial", 66, bold=True)
        r_end = f_end.render("GAME OVER", 1, pygame.Color("white"))
        sc.blit(r_end, (size//2 - 200, size//3))
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

def main():
    size = 600
    sn = 100
    sc = display(size)
    game(sc, size, sn)

if __name__ == '__main__':
    main()