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
    MDFloatLayout:
        pos_hint: {"center_x": .25, "center_y": .4}
        size_hint: .22, .1
        Image:
            source: "assets/humidity.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: humidity
            text: "80%"
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "14sp"
        MDLabel:
            text: "Humidity"
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "14sp"
    MDFloatLayout:
        pos_hint: {"center_x": .7, "center_y": .4}
        size_hint: .22, .1
        Image:
            source: "assets/wind.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: wind_speed
            text: "80 km/h"
            pos_hint: {"center_x": 1.1, "center_y": .7}
            font_size: "16sp"
        MDLabel:
            text: "Wind"
            pos_hint: {"center_x": 1.1, "center_y": .3}
            font_size: "14sp"
'''

class WeatherApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    WeatherApp().run()