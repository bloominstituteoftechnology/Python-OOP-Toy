class Rect:
    """
    base class for making rectangles
    """
    def __init__(self, bounds, color, rect):
        self.bounds = bounds
        self.color = color
        self.rect = rect

    def update(self):
        pass
    
    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rect)
