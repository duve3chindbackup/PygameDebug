import time
import pygame.freetype
import threading

from pygame.display import update

from .downloadFont import retrieve_font


class Text:
    def __init__(self, text: str, font: str, color = (255, 255, 255), size = 20):
        self.text = text
        self.base_text = text
        self.font = pygame.freetype.Font(font, size=size)
        self.color = color
        
    def render(self, display, loc):
        self.font.render_to(display, loc, self.text, self.color)

    def update_text(self, x: str):
        self.text = self.base_text + str(x)
        # WARN: might error who knows?

    
class DebugWindow:
    def __init__(self, size=(800, 600), font_size=20):
        self.window = pygame.display.set_mode(size=size)
        self.callables_dict = {}
        self.font = retrieve_font()
        self.font_size = font_size

    def add_text(self, default_text, call):
        """
        The way this function works is that you provide a callable that returns the up-to date data
        """
        obj = Text(default_text, self.font, size=self.font_size)

        self.callables_dict[call] = obj

    def start(self, delay=0.1):
        thre = threading.Thread(target=self.main_debug_thread, args=(delay,), daemon=True)
        thre.start()

    def main_debug_thread(self, update_delay):
        while True:
            self.window.fill((0, 0, 0))
            y = 10
            for call, text in self.callables_dict.items():
                newdata = call()
                text.update_text(newdata)

                text.render(self.window, (10, y))
                y += (self.font_size + 5)

            time.sleep(update_delay)

            pygame.display.flip()

