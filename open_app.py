from kivy.app import App
from kivy.uix.button import Button
from plyer.platforms.android import activity
import ase as ase

class main(App):
    def build(self):
        # btn = Button(text = 'open app'.font_size='60')
        btn = Button(text="open.app").font_size = "60"
        btn.bind(on_release=self.open)

    def opeb (self):
        pass
        a = ase.An


