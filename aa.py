
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyLayout(GridLayout):
    def __init__(self):
        super().__init__()

        self.cols = 2

        self.slider = Slider(min = 0, max = 100)
        self.add_widget(self.slider)
        self.slider.bind(value = self.on_value_change)

        self.label = Label(text = "0")
        self.add_widget(self.label)

    def on_value_change(self, instance, value):
        self.label.text = "Value Is : {} ".format(int(value))


class SliderWindowEx(App):
    def build(self):
        print(MyLayout().label.text)
        return MyLayout()



if __name__ == "__main__":
    window = SliderWindowEx()
    window.run()