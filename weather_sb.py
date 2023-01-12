import requests as requests
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
    MDFloatLayout:
        size_hint_y: .3
        canvas:
            Color:
                rgb: rgba(148, 117, 255, 255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [10, 10, 0, 0]
        MDFloatLayout:
            pos_hint: {"center_x": .5, "center_y": .71}
            size_hint: .9, .32
            canvas:
                Color:
                    rgb: rgba(131, 69, 255, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
            TextInput:
                id: city_name
                hint_text: "Enter City Name"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y": .5}
                height: self.minimum_height
                multiline: False
                font_size: "20sp"
                hint_text_color: 1, 1, 1, 1
                foreground_color: 1, 1, 1, 1
                background_color: 1, 1, 1, 0
                padding: 15
                cursor_color: 1, 1, 1, 1
                cursor_widtg: "2sp"
        Button:
            text: "Get Weather"
            font_size: "20sp"
            size_hint: .9, .32
            pos_hint: {"center_x": .5, "center_y": .29}
            background_color: 1, 1, 1, 0
            rgb: rgba(148, 117, 255, 255)
            on_release: app.search_weather()
            canvas.before:
                Color:
                    rgb: 1, 1, 1, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
'''

class WeatherApp(MDApp):

    api_key = "77223c457b2a4e1bab8295684e284e0a"

    def build(self):
        return Builder.load_string(kv)

    def get_weather(self, city_name):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
            print(url)
            response = requests.get(url)
            x = response.json()
            print(x)
            if x["cod"] != "404":
                temperature = round(x["main"]["temp"] - 273.15)
                humidity = x["main"]["humidity"]
                weather = x["weather"][0]["main"]
                id = str(x["weather"][0]["id"])
                wind_speed = round(x["wind"]["speed"] * 18/5)

        except requests.ConnectionError:
            print("No Internet Connection")


    def search_weather(self):
        self.get_weather("Delhi")


if __name__ == '__main__':
    WeatherApp().run()