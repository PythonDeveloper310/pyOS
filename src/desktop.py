import pygame as pg
from src.utilities import *

pg.init()
dx, dy = 1366, 768
display = pg.display.set_mode((dx, dy), flags=pg.NOFRAME | pg.FULLSCREEN)
pg.display.set_caption("pyOS Desktop")

pg.event.set_grab(True)
pg.mouse.set_visible(False)

clock = pg.time.Clock()
tick = 60

def start_desktop():
    import time

    running = True
    pylogo = "src/assets/python-logo.png"
    mouse = "src/assets/mouse.png"

    mouse = pg.image.load(mouse).convert_alpha()
    pylogo = pg.image.load(pylogo).convert_alpha()

    is_circle = False
    is_triangle = False
    is_clicked = False

    black(display)
    print_center(display, "pyOS", WHITE, dx, dy, 72)
    pg.display.flip()
    time.sleep(1.5)

    while running:
        for ev in pg.event.get():
                match ev.type:
                    case pg.QUIT:
                        running = False
                    case pg.KEYDOWN:
                        if ev.key == pg.K_ESCAPE:
                            running = False
                        elif ev.key == pg.K_1:
                            black(display)
                        elif ev.key == pg.K_2:
                            red(display)
                        elif ev.key == pg.K_3:
                            green(display)
                        elif ev.key == pg.K_4:
                            yellow(display)
                        elif ev.key == pg.K_5:
                            white(display)
                        elif ev.key == pg.K_6:
                            gray(display)
                        elif ev.key == pg.K_e:
                            is_circle = True
                            is_triangle = False
                        elif ev.key == pg.K_w:
                            is_circle = False
                            is_triangle = True
                        elif ev.key == pg.K_q:
                            is_circle = False
                            is_triangle = False
                    case pg.MOUSEBUTTONDOWN:
                        if ev.button == 1:
                            is_clicked = True
        mouse_x, mouse_y = pg.mouse.get_pos()

        clear_screen(display)
        if is_circle and not is_triangle:
            DrawShape(display).clear()
            DrawShape(display).circle((dx//2, dy//2), 100, WHITE)
        elif not is_circle and is_triangle:
            DrawShape(display).clear()
            DrawShape(display).triangle((dx//2, dy//2 - 50), (dx//2 - 50, dy//2 + 50), (dx//2 + 50, dy//2 + 50), WHITE)
        else:
            blit_center(display, pylogo, dx, dy)
        
        print_string(display, f"pyOS Desktop Test, FPS: {clock.get_fps() :.0f}", WHITE, 32)
        print_string(display, "Press 'ESC' to exit.", WHITE)
        newline(display)
        print_string(display, "Hello world!", BLACK)
        print_string(display, "Hello world!", GREEN)
        print_string(display, "Hello world!", RED)
        print_string(display, "Hello world!", YELLOW)
        print_string(display, "Hello world!", WHITE)
        print_string(display, "Hello world!", GRAY)
        newline(display)
        print_string(display, "Press '1' to '6' to change background color.", WHITE)
        print_string(display, "Press 'Q' to DrawShape the Python logo, 'W' to DrawShape the a triangle, 'E' to DrawShape a circle.", WHITE)

        blit_image(display, mouse, (mouse_x - 16, mouse_y - 16))
        if is_clicked:
            print_string(display, "Mouse clicked", WHITE, 24)
            is_clicked = False

        pg.display.flip()
        clock.tick(tick)
    exit_desktop(display, tick)
    pg.quit()