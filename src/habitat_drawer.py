import pygame

class habitat_drawer:

    CELLS_COLORS = [(102, 141, 60), (96, 96, 96), (255, 255, 255), (143, 59, 27)]

    def __init__(self, target, cell_size, iterations_per_draw):
        self.target = target
        self.cell_size = cell_size
        self.iterations_per_draw = iterations_per_draw

        pygame.init()

        self.gameDisplay = pygame.display.set_mode((target.grid_size_x * cell_size, target.grid_size_y * cell_size))
        pygame.display.set_caption('Victims predators visualizer')

        self.clock = pygame.time.Clock()

    def run_loop(self, callback):
        do_loop = True
        while do_loop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    do_loop = False

            self.update()

            iteration = self.iterations_per_draw
            while iteration:
                callback()
                iteration -= 1

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        self.gameDisplay.fill(habitat_drawer.CELLS_COLORS[0])
        for i in range(self.target.grid_size_y):
            for j in range(self.target.grid_size_x):
                if self.target.grid[i][j]:
                    self.gameDisplay.fill(habitat_drawer.CELLS_COLORS[self.target.grid[i][j] % 4], (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))
