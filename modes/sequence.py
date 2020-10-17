from abstract.mode import Mode
from kivy.core.window import Window
from const import Const
from container import ColoredLabel
import asyncio
import math


class Sequence(Mode):
    def __init__(self, main):
        super().__init__(main)
        self.task = None
        self.interval = None
        self.step = None
        self.sequence = []
        self.labels = []
        self.layout = self.main.container.ids.sequence_mode.ids.color_grid
        self.mode = self.main.container.ids.sequence_mode.ids.sequence_checkbox


    def action(self):
        if self.interval and self.sequence:
            self.main.container.add_widget(self.screen)
            self.show()
            self.task = asyncio.Task(self.pulsation())
            self.running = True
            self.max_rgb_value = 0


    def stop(self):
        self.task.cancel()
        self.main.container.remove_widget(self.screen)
        Window.fullscreen = False
        self.running = False


    def setup(self, opt):
        choice = opt[0]
        if choice == Const.ADD_COLOR:
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

        if choice == Const.DEL_COLORS:
            self.del_colors()

        if choice == Const.INTERVAL:
            self.interval = opt[1]

        if choice == Const.PULSE_COLOR:
            self.init_to = opt[1]


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
        frames_per_sec = 60
        frames = int(frames_per_sec * self.interval)
        frame = 1 / frames_per_sec
        current_frame = 0
        to_rgb = None
        sequence_size = len(self.sequence)
        self.screen.rgb = self.sequence[0]
        count = 0
        while self.running:
            if current_frame == 0:
                count += 1
                if count > sequence_size - 1:
                    count = 0
                to_rgb = self.sequence[count]
                self.step = []
                for i in range(3):
                    self.step.append(math.fabs((to_rgb[i] - self.screen.rgb[i]) / frames))


            self.change_rgb(self.screen.rgb, to_rgb)
            current_frame += step_count
            if current_frame == frames:
                current_frame = 0
            await asyncio.sleep(frame)


    def change_rgb(self, from_color, to_color):
        from_color = from_color[:]
        to_color = to_color[:]
        for i in range(3):
            if from_color[i] < to_color[i]:
                from_color[i] += self.step[i]
            else:
                from_color[i] -= self.step[i]
        self.screen.rgb = from_color


