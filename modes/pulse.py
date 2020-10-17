from abstract.mode import Mode
from kivy.core.window import Window
from const import Const

import asyncio
import math


class Pulse(Mode):
    def __init__(self, main):
        super().__init__(main)
        self.task = None
        self.interval = None
        self.init_from = None
        self.init_to = None
        self.step = None


    def action(self):
        if self.interval and self.init_to:
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

        if choice == Const.RGB:
            self.screen.rgb = opt[1]
            self.init_from = opt[1]


        if choice == Const.INTERVAL:
            self.interval = opt[1]

        if choice == Const.PULSE_COLOR:
            self.init_to = opt[1]



    async def pulsation(self):
        step_count = 1
        frames_per_sec = 60
        frames = int(frames_per_sec * self.interval)
        frame = 1 / frames_per_sec
        current_frame = 0
        to_rgb = None

        while self.running:
            if current_frame == 0:
                to_rgb = self.init_to
                step_count = 1
                self.step = []
                for i in range(3):
                    self.step.append(math.fabs((to_rgb[i] - self.screen.rgb[i]) / frames))

            if current_frame == frames:
                to_rgb = self.init_from
                step_count = -1
                self.step = []
                for i in range(3):
                    self.step.append(math.fabs((to_rgb[i] - self.screen.rgb[i]) / frames))

            self.change_rgb(self.screen.rgb, to_rgb)
            current_frame += step_count

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


