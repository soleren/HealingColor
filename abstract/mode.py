from abc import ABC, abstractmethod
from kivy.core.window import Window

class Mode:
    def __init__(self, main):
        self.main = main
        self.screen = main.colored_fullscreen
        self.loop = main.loop


    def show(self):
        Window.fullscreen = 'auto'


    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def setup(self, opt):
        pass

    @abstractmethod
    def stop(self):
        pass