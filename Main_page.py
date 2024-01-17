from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import window

window.size = (350,580)

kv = '''
MDFloatLayout:
    md_bg_color: 1,1,1,1
    Image: