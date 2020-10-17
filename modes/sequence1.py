from abstract.mode import Mode
from kivy.core.window import Window
from const import Const
from container import ColoredLabel
import asyncio
import math


class Sequence1(Mode):
    def __init__(self, main):
        super().__init__(main)
        self.task = None
        self.interval = None
        self.step = None
        self.sequence = []
        self.labels = []
        self.layout = self.main.container.ids.sequence_mode1.ids.color_grid


    def action(self):
        if self.interval and self.sequence:
            self.main.container.add_widget(self.screen)
            self.show()
            self.task = asyncio.Task(self.pulsation())
            self.running = True



    def stop(self):
        self.task.cancel()
        self.main.container.remove_widget(self.screen)
        Window.fullscreen = False
        self.running = False



    def setup(self, opt):
        choice = opt[0]

        if choice == Const.ADD_COLOR1:
            if opt[1] == 'down':
                self.sequence.append(opt[2])
                label = ColoredLabel(size_hint=(None, 1), width ='39dp')
                label.color = opt[2]
                self.layout.add_widget(label)
                self.labels.append(label)
            else:
                label = self.find_label(opt[2])
                self.layout.remove_widget(label)
                self.sequence.remove(opt[2])
                self.labels.remove(label)


        if choice == Const.INTERVAL:
            self.interval = opt[1]

        if choice == Const.DEL_COLORS:
            self.del_colors()

    def del_colors(self):
        copy = self.layout.children[:]
        for child in copy:
            self.layout.remove_widget(child)
        self.sequence = []
        self.labels = []

    def find_label(self, opt):
        for label in self.labels:
            if label.color == opt:
                return label


    async def pulsation(self):
        step_count = 1
        current_frame = 0
        sequence_size = len(self.sequence)
        count = 0
        while self.running:
            if count > sequence_size - 1:
                count = 0
            self.screen.rgb = self.sequence[count]

            current_frame += step_count
            count += 1
            await asyncio.sleep(self.interval)





