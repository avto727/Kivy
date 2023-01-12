from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
Window.size = (350, 600)

kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "assets/location.png"
        size_hint: .1, .1
        pos_hint: {"center_x": .5, "center_y": .95}
    MDLabel:
        id: location
        text: "Moscow, RU"
        pos_hint: {"center_x": .5, "center_y": .89}
        halign: "center"
        font_size: "20sp"
    Image:
        id: weather_image
        source: "assets/sun.png"
        pos_hint: {"center_x": .5, "center_y": .77}
    MDLabel:
        id: temperature
        text: "[b]23°[/b]"
        markup: True
        pos_hint: {"center_x": .5, "center_y": .62}
        halign: "center"
        font_size: "60sp"
    MDLabel:
        id: weather
        text: "Partly Cloudy"
        markup: True
        pos_hint: {"center_x": .5, "center_y": .54}
        halign: "center"
        font_size: "20sp"
'''

class WeatherApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    WeatherApp().run()