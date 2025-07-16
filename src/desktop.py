import pygame as pg
from src.utilities import *

pg.init()
dx, dy = 1366, 768
display = pg.display.set_mode((dx, dy), flags=pg.NOFRAME | pg.FULLSCREEN)
pg.display.set_caption("pyOS Desktop")

pg.event.set_grab(True)
pg.mouse.set_visible(False)

clock = pg.time.Clock()
tick = 1000 * 1000

def newln():
    newline(display)

def start_desktop():
    import time

    running = True

    # Icons
    icons = {
        "pylogo": "src/assets/python-logo.png",
        "mouse": "src/assets/mouse.png",
        "folder-icon": "src/assets/folder-icon.png",
    }

    # Load images
    mouse = pg.image.load(icons["mouse"]).convert_alpha()
    _pylogo = pg.image.load(icons["pylogo"]).convert_alpha()
    folder_icon = pg.image.load(icons["folder-icon"]).convert_alpha()

    is_clicked = False

    black(display)
    print_center(display, "pyOS", dx, dy, WHITE, 72)
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
                    case pg.MOUSEBUTTONDOWN:
                        if ev.button == 1:
                            is_clicked = True
        mouse_x, mouse_y = pg.mouse.get_pos()

        clear_screen(display)
        
        print_string(display, f"pyOS Desktop Test, FPS: {clock.get_fps() :.0f}", WHITE, 32)
        newln()
        print_string(display, "Hello World!", RED)
        print_string(display, 'b', RED)

        blit_image(display, folder_icon, (dx // 2 - 64, dy // 2 - 64))

        blit_image(display, mouse, (mouse_x - 16, mouse_y - 16))
        if is_clicked:
            is_clicked = False

        pg.display.flip()
        clock.tick(tick)
    exit_desktop(display, tick)
    pg.quit()