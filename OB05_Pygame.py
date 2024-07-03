import pygame
import random

    # Константы
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
FPS = 10

    # Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + CELL_SIZE)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - CELL_SIZE, head_y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (head_x + CELL_SIZE, head_y)

        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, direction):
            # Избегаем изменения направления на противоположное
        if (direction == pygame.K_UP and self.direction != pygame.K_DOWN) or \
            (direction == pygame.K_DOWN and self.direction != pygame.K_UP) or \
            (direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or \
            (direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT):
            self.direction = direction

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or \
            head[0] < 0 or head[0] >= SCREEN_WIDTH or \
            head[1] < 0 or head[1] >= SCREEN_HEIGHT


class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE, random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def respawn(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE, random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.snake.change_direction(event.key)

            self.snake.move()
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.respawn()

            if self.snake.check_collision():
                running = False

            self.screen.fill(BLACK)
            for segment in self.snake.body:
                    pygame.draw.rect(self.screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.food.position[0], self.food.position[1], CELL_SIZE, CELL_SIZE))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()