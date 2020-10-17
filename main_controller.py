# -*- coding: utf-8 -*-
from container import Container
from container import ColoredFullScreen
from const import Const
from kivy.core.window import Window
from modes.simple import Simple
from modes.pulse import Pulse
from modes.sequence import Sequence
from modes.sequence1 import Sequence1
import asyncio
import webbrowser


class Main:
    def __init__(self, app, loop):
        self.app = app
        self.loop = loop
        self.container = Container()
        self.colored_fullscreen = ColoredFullScreen()
        self.mode = None
        self.duration = 0
        self.task = None
        Window.bind(on_key_down=self._on_keyboard_down)


    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40 and self.mode:
            self.mode.stop()
            if self.task:
                self.task.cancel()


    def action_button_callback(self, action, opt=None):
        if action == Const.SETUP:
            if self.mode:
                self.mode.setup(opt)

        if action == Const.CHANGE_MODE:
            if opt == Const.SIMPLE_MODE:
                self.mode = Simple(self)

            if opt == Const.PULSE_MODE:
                self.mode = Pulse(self)

            if opt == Const.SEQUENCE_MODE:
                self.mode = Sequence(self)

            if opt == Const.SEQUENCE_MODE1:
                self.mode = Sequence1(self)




        if action == Const.DURATION:
            self.duration = opt

        if action == Const.RUN:
            if self.mode:
                self.mode.action()
                self.task = asyncio.Task(self.seance())


    async def seance(self):
        if not self.duration:
            self.duration = 1
        await asyncio.sleep(self.duration * 60)
        if self.mode:
            self.mode.stop()


    def vk(self):
        webbrowser.open('https://vk.com/pchromotherapy')

    def telegramm(self):
        webbrowser.open('https://t.me/pchromotherapy')