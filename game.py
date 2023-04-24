# Importar os módulos necessários
import pygame
import random

# Inicializar o pygame
pygame.init()

# Definir as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definir o tamanho da tela
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir o título da janela
pygame.display.set_caption("Jogo da Cobrinha")

# Definir a velocidade do relógio
clock = pygame.time.Clock()

# Definir a velocidade da cobrinha
snake_speed = 10

# Definir o tamanho da cobrinha e da maçã
snake_size = 10
apple_size = 10

# Criar uma classe para representar a cobrinha

class Snake:
    # Inicializar os atributos da cobrinha
    def __init__(self):
        # Criar uma lista para armazenar os segmentos da cobrinha
        self.segments = []
        # Criar o segmento inicial da cobrinha na posição central da tela
        self.head = pygame.Rect(
            screen_width // 2, screen_height // 2, snake_size, snake_size)
        # Adicionar o segmento inicial à lista de segmentos
        self.segments.append(self.head)
        # Definir a direção inicial da cobrinha como parada
        self.direction = "stop"

    # Atualizar a posição da cobrinha de acordo com a direção
    def update(self):
        # Verificar se a cobrinha está se movendo
        if self.direction != "stop":
            # Remover o último segmento da lista de segmentos
            self.segments.pop()
            # Criar um novo segmento na posição da cabeça da cobrinha
            new_segment = pygame.Rect(
                self.head.x, self.head.y, snake_size, snake_size)
            # Inserir o novo segmento no início da lista de segmentos
            self.segments.insert(0, new_segment)
            # Atualizar a posição da cabeça da cobrinha de acordo com a direção
            if self.direction == "up":
                self.head.y -= snake_size
            elif self.direction == "down":
                self.head.y += snake_size
            elif self.direction == "left":
                self.head.x -= snake_size
            elif self.direction == "right":
                self.head.x += snake_size

    # Desenhar a cobrinha na tela
    def draw(self):
        # Percorrer os segmentos da cobrinha
        for segment in self.segments:
            # Desenhar cada segmento na cor verde
            pygame.draw.rect(screen, GREEN, segment)

    # Verificar se a cobrinha colidiu com as bordas da tela ou com ela mesma
    def check_collision(self):
        # Verificar se a cabeça da cobrinha saiu dos limites da tela
        if self.head.x < 0 or self.head.x > screen_width - snake_size or \
           self.head.y < 0 or self.head.y > screen_height - snake_size:
            # Retornar verdadeiro para indicar que houve colisão
            return True

        # Percorrer os segmentos da cobrinha a partir do segundo
        for segment in self.segments[1:]:
            # Verificar se a cabeça da cobrinha colidiu com algum segmento
            if self.head.colliderect(segment):
                # Retornar verdadeiro para indicar que houve colisão
                return True

        # Retornar falso para indicar que não houve colisão
        return False

    # Aumentar o tamanho da cobrinha ao comer uma maçã
    def grow(self):
        # Criar um novo segmento na posição do último segmento da cobrinha
        last_segment = self.segments[-1]
        new_segment = pygame.Rect(
            last_segment.x, last_segment.y, snake_size, snake_size)
        # Adicionar o novo segmento à lista de segmentos
        self.segments.append(new_segment)

# Criar uma classe para representar a maçã


class Apple:
    # Inicializar os atributos da maçã
    def __init__(self):
        # Criar um retângulo para representar a maçã em uma posição aleatória na tela
        self.rect = pygame.Rect(random.randint(0, screen_width - apple_size),
                                random.randint(0, screen_height - apple_size), apple_size, apple_size)

    # Desenhar a maçã na tela
    def draw(self):
        # Desenhar o retângulo da maçã na cor vermelha
        pygame.draw.rect(screen, RED, self.rect)


# Criar um objeto da classe Snake
snake = Snake()

# Criar um objeto da classe Apple
apple = Apple()

# Criar uma variável para controlar o loop principal
running = True

# Iniciar o loop principal
while running:
    # Limitar a taxa de quadros a 10 FPS
    clock.tick(10)

    # Processar os eventos do pygame
    for event in pygame.event.get():
        # Verificar se o usuário clicou no botão de fechar a janela
        if event.type == pygame.QUIT:
            # Encerrar o loop principal
            running = False

        # Verificar se o usuário pressionou alguma tecla
        elif event.type == pygame.KEYDOWN:
            # Verificar qual tecla foi pressionada e mudar a direção da cobrinha de acordo
            if event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"

    # Atualizar a posição da cobrinha
    snake.update()

    # Verificar se a cobrinha colidiu com a maçã
    if snake.head.colliderect(apple.rect):
        # Aumentar o tamanho da cobrinha
        snake.grow()
        # Criar uma nova maçã em uma posição aleatória na tela
        apple = Apple()

    # Verificar se a cobrinha colidiu com as bordas da tela ou com ela mesma
    if snake.check_collision():
        # Encerrar o loop principal
        running = False

    # Preencher o fundo da tela com a cor preta
    screen.fill(BLACK)

    # Desenhar a cobrinha na tela
    snake.draw()

    # Desenhar a maçã na tela
    apple.draw()

    # Atualizar a tela do pygame
    pygame.display.flip()

# Finalizar o jogo
pygame.quit()
