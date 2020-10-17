# -*- coding: utf-8 -*-

from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.image import Image as kvImage
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder


Builder.load_file('kv/simple.kv')
Builder.load_file('kv/pulse.kv')
Builder.load_file('kv/sequence.kv')
Builder.load_file('kv/sequence1.kv')
Builder.load_file('kv/timer.kv')
Builder.load_file('kv/container.kv')



class Container(Screen):
    pass


class SimpleMode(GridLayout):
    pass

class ColoredLabel(Label):
    pass

class SimpleCheckbox(CheckBox):
    pass

class SequenceMode(GridLayout):
    pass

class Sequence1Mode(GridLayout):
    pass

class Timer(GridLayout):
    pass

class PulseMode(GridLayout):
    pass

class ColoredFullScreen(Screen):
    rgb = ListProperty()


