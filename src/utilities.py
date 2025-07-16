import pygame as pg

pg.init()

BLACK = pg.Color(0,0,0)
GREEN = pg.Color(0,255,0)
RED = pg.Color(255,0,0)
YELLOW = pg.Color(255,255,0)
WHITE = pg.Color(255,255,255)
GRAY = pg.Color(128,128,128)

current_color = BLACK

def clear_screen(screen: pg.Surface):
    screen.fill(current_color)
    reset_prev_rects()

def reset_prev_rects():
    global previous_rects
    previous_rects = []

def print_string(screen: pg.Surface, string: str, color: pg.Color, tsize: int = 24, pos=(6, 6)):
    global previous_rects
    font = pg.font.SysFont(None, tsize)

    text = font.render(string, True, color)
    rect = text.get_rect(topleft=pos)
    while any(rect.colliderect(prev) for prev in previous_rects):
        rect.y += tsize
    previous_rects.append(rect)
    screen.blit(text, rect)

def print_to_pos(screen: pg.Surface, string: str, color: pg.Color, pos=(6, 6), tsize: int = 24):
    font = pg.font.SysFont(None, tsize)

    text = font.render(string, True, color)
    rect = text.get_rect(topleft=pos)
    screen.blit(text, rect)

def print_center(screen: pg.Surface, string: str, color: pg.Color, screen_x, screen_y, tsize: int = 42):
    font = pg.font.SysFont(None, tsize)

    text = font.render(string, True, color)
    rect = text.get_rect(center=(screen_x//2, screen_y//2))
    screen.blit(text, rect)

def blit_image(screen: pg.Surface, image_file_or_surface, pos=(0, 0)):
    image = (
        pg.image.load(image_file_or_surface).convert_alpha()
        if isinstance(image_file_or_surface, str)
        else image_file_or_surface
    )
    rect = image.get_rect(topleft=pos)
    screen.blit(image, rect)
    return rect

def blit_center(screen: pg.Surface, image_file_or_surface, screen_x, screen_y):
    image = (
        pg.image.load(image_file_or_surface).convert_alpha()
        if isinstance(image_file_or_surface, str)
        else image_file_or_surface
    )
    rect = image.get_rect(center=(screen_x // 2, screen_y // 2))
    screen.blit(image, rect)
    return rect


def newline(screen: pg.Surface):
    print_string(screen, "NEWLINE", current_color)


def black(screen: pg.Surface):
    global current_color
    screen.fill(BLACK)
    current_color = BLACK

def green(screen: pg.Surface):
    global current_color
    screen.fill(GREEN)
    current_color = GREEN

def white(screen: pg.Surface):
    global current_color
    screen.fill(WHITE)
    current_color = WHITE

def red(screen: pg.Surface):
    global current_color
    screen.fill(RED)
    current_color = RED

def yellow(screen: pg.Surface):
    global current_color
    screen.fill(YELLOW)
    current_color = YELLOW

def gray(screen: pg.Surface):
    global current_color
    screen.fill(GRAY)
    current_color = GRAY

def setbg(screen: pg.Surface, bg_file):
    bg = pg.image.load(bg_file).convert()
    bg = pg.transform.scale(bg, (1366, 768))
    screen.blit(bg, (0,0))

def exit_desktop(screen: pg.Surface, tick: int):
    import time as t

    for _ in range(tick//100):
        for dots in [".", "..", "..."]:
            black(screen)
            print_center(screen, f"Exiting Desktop{dots}", WHITE, screen.get_width(), screen.get_height(), 48)
            pg.display.flip()
            t.sleep(0.4)

class DrawShape():
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.previous_rects = []

    def clear(self):
        self.screen.fill(current_color)
        self.previous_rects.clear()

    def circle(self, pos, radius, color):
        pg.draw.circle(self.screen, color, pos, radius)
        self.previous_rects.append(pg.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2))
    
    def triangle(self, pos1, pos2, pos3, color):
        pg.draw.polygon(self.screen, color, [pos1, pos2, pos3])
        self.previous_rects.append(pg.Rect(min(pos1[0], pos2[0], pos3[0]), min(pos1[1], pos2[1], pos3[1]),
                                            max(pos1[0], pos2[0], pos3[0]) - min(pos1[0], pos2[0], pos3[0]),
                                            max(pos1[1], pos2[1], pos3[1]) - min(pos1[1], pos2[1], pos3[1])))