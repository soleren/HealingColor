# -*- coding: utf-8 -*-
import asyncio

from kivy.app import App
from main_controller import Main
from kivy.config import Config
from kivy.utils import platform


if platform == 'win':
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '800')
    Config.write()

class HealingColorApp(App):
    def __init__(self, loop):
        super().__init__()
        self.main = None
        self.other_task = None
        self.loop = loop


    def build_config(self, config):
        self.config.setdefaults('settings', {
})


    def build(self):
        self.icon = 'wheel_vk.ico'
        self.main = Main(self, self.loop)
        return self.main.container



    def app_func(self):
        '''This will run both methods asynchronously and then block until they
        are finished
        '''
        self.other_task = asyncio.ensure_future(self.waste_time_freely())

        async def run_wrapper():
            # we don't actually need to set asyncio as the lib because it is
            # the default, but it doesn't hurt to be explicit
            await self.async_run(async_lib='asyncio')
            self.other_task.cancel()

        return asyncio.gather(run_wrapper(), self.other_task)

    async def waste_time_freely(self):
        '''This method is also run by the asyncio loop and periodically prints
        something.
        '''
        # await self.s.start_server()

if __name__ == "__main__":
    # Config.get_config(True)
    loop = asyncio.get_event_loop()
    anynote = HealingColorApp(loop)
    loop.run_until_complete(anynote.app_func())
    loop.close()
