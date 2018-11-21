import pygame
import sys
import random

pygame.init()


class Game:
    SIZE = WIDTH, HEIGHT = 600, 450
    TITLE = "Snake Machine Learning"

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(self.TITLE)
        self.snake = Snake()
        self.entity_width = 10
        self.apple = self.apple_x, self.apple_y = (random.randint(0, self.WIDTH - self.entity_width), random.randint(0, self.HEIGHT - self.entity_width))
        self.apple_color = (255, 6, 81)

    def draw_snake(self):
        self.snake.x_position += game.snake.x_direction
        self.snake.y_position += game.snake.y_direction
        self.snake.body.insert(0, [game.snake.x_position, game.snake.y_position])
        if len(self.snake.body) > self.snake.length:
            del(self.snake.body[-1])
        for i in self.snake.body:
            pygame.draw.rect(self.screen, self.snake.color, pygame.Rect(i[0], i[1], self.entity_width, self.entity_width))

    def crash_wall(self):
        if self.snake.body[0][0] < 0 or self.snake.body[0][0] > self.WIDTH - 10:
            return True
        elif self.snake.body[0][1] < 0 or self.snake.body[0][1] > self.HEIGHT - 10:
            return True
        else:
            return False

    def draw_apples(self):
        x = self.apple_x
        y = self.apple_y
        pygame.draw.rect(self.screen, self.apple_color, pygame.Rect(x, y, self.entity_width, self.entity_width))

    def eats_apple(self):
        if self.snake.body[0][0] <= self.apple_x + self.entity_width and self.snake.body[0][0] + self.entity_width >= self.apple_x:
            if self.snake.body[0][1] <= self.apple_y + self.entity_width and self.snake.body[0][1] + self.entity_width >= self.apple_y:
                self.apple_x = random.randint(0, self.WIDTH - self.entity_width)
                self.apple_y = random.randint(0, self.HEIGHT - self.entity_width)
                return True
        else:
            return False


class Snake:

    def __init__(self):
        self.head = [self.x_position, self.y_position] = [300, 220]
        self.speed = 10
        self.color = (121, 200, 239)
        self.x_direction = self.speed
        self.y_direction = 0
        self.length = 1
        self.body = []
        self.body.append(self.head)


class Population(object):
    def __init__(self):
        self.mutation_chance = .5


class GenAlgorithm(object):
    def __init__(self):
        self.fitness = 0


game = Game()

running = True


def main():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        game.screen.fill((45, 45, 45))
        game.draw_snake()
        game.draw_apples()
        pygame.display.flip()
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.snake.y_direction = 0
            game.snake.x_direction = -game.snake.speed
        elif keys[pygame.K_RIGHT]:
            game.snake.y_direction = 0
            game.snake.x_direction = game.snake.speed
        elif keys[pygame.K_UP]:
            game.snake.y_direction = -game.snake.speed
            game.snake.x_direction = 0
        elif keys[pygame.K_DOWN]:
            game.snake.y_direction = game.snake.speed
            game.snake.x_direction = 0

        if game.eats_apple():
            game.snake.length += 1
            game.snake.body.append([game.snake.x_position - game.snake.x_direction , game.snake.y_position - game.snake.y_direction])
        if game.crash_wall():
            print("score = ", game.snake.length)
            sys.exit()

        pygame.time.wait(45)


if __name__ == '__main__':
    main()
