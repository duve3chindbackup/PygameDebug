import pygame.freetype
import threading


class Text:
    def __init__(self, text: str, font: str, color = (255, 255, 255)):
        self.text = text
        self.font = pygame.freetype.Font(font, size=20)
        
    
class DebugWindow:
    def __init__(self, size=(800, 600)):
        self.window = pygame.display.set_mode(size=size)
        self.textList = []
        
    def add_text(self, default_text, callable):
        """
        The way this function works is that you provide a callable that returns the up-to date data
        """
        # TODO: add the actual text object
        self.textList.append()
        """
        Archecture planned:
            - all data refs have some kind of 'callable' that they use to reference updated data
            - add_text funcs maybe?
        """
        
    
    def main_debug_thread(self):
        while True:
        