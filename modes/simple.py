from abstract.mode import Mode
from kivy.core.window import Window
from const import Const

class Simple(Mode):
    def __init__(self, main):
        super().__init__(main)


    def action(self):
        self.main.container.add_widget(self.screen)
        self.show()


    def setup(self, opt):
        choice = opt[0]
        if choice == Const.RGB:
            self.screen.rgb = opt[1]


    def stop(self):
        self.main.container.remove_widget(self.screen)
        Window.fullscreen = False