import os

from kivy.uix.modalview import ModalView

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.image import Image
from datetime import date


class BoxApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        print(instance.text,self.button2)
        self.filename = str(self.textinput.text + self.textinput_1.text)
        with open(self.filename, "a") as text_js_file:
            text = instance.text +" "+ self.button2 +"\n"
            data = text_js_file.write(text)
            print(data)
    def add_operation(self, instance):
         self.formula += str(instance.text)
         self.update_label()

    def add_file(self,instance):
        self.filename = str(self.textinput.text+self.textinput_1.text)
        if self.filename in os.listdir():
            with open(self.filename, "a") as text_js_file:
                text = self.textinput.text + " " + self.textinput_1.text + "\n"
                data = text_js_file.write(text)
        else:
            with open(self.filename, "w") as text_js_file:
                text = self.textinput.text + " " + self.textinput_1.text + "\n"
                data = text_js_file.write(text)

    def image_zoom(self, instance):
        modal = ModalView(size_hint=(.9, .9))
        button = Image(source='img/' + instance.id, allow_stretch=True, keep_ratio=False)
        modal.add_widget(button)
        print(button)
        print(instance.id)
        modal.open()

    def on_value_change(self, instance, value):
        self.button2 = instance.instance.text = str(value)
        print(self.button2)
        print(instance, value)
        print(instance.instance)
        return instance.instance.text
    def build(self):
        gl = GridLayout(cols=1, spacing=1, size_hint_y=None,height=220)
        gltext = GridLayout(cols=3, spacing=1, size_hint_y=None,height=40)
        glimg = GridLayout(cols=2, spacing=1, size_hint_y=None,height=220)
        gl.bind(minimum_height=gl.setter('height'))
        self.textinput = TextInput(text='Hello world')
        self.textinput_1 = TextInput(text=str(date.today()))
        textbutton = Button(text='Hello world',on_press=self.add_file)
        gltext.add_widget(self.textinput)
        gltext.add_widget(self.textinput_1)
        gltext.add_widget(textbutton)
        gl.add_widget(gltext)
        gl.add_widget(glimg)
        for filename in os.listdir('img'):
            print(filename)

            button = Image(source='img/'+filename, allow_stretch=True, keep_ratio=False,on_press=self.image_zoom)
            # button = Button(text=filename[:-4], on_press=self.add_number, font_size=13, size_hint=(.1, 2))
            img = GridLayout(cols=1, spacing=1)
            img.add_widget(button)
            # button1 = Button(text=filename[:-4], on_press=self.add_number, font_size=13, )
            self.button2 = Label(text='0')

            bl = GridLayout(cols=4, spacing=1, size_hint_y=None, height=20)
            button1 = Slider(min=0, max=100, step=1)
            button1.instance = self.button2
            print(button1.instance)
            print(button1)
            bl.add_widget(button1)
            button1.bind(value=self.on_value_change)


            button2 = self.button2
            bl.add_widget(button2)
            button3 = Button(text=filename[:-4], on_press=self.add_number, font_size=13, )
            button4 = Button(text='Zoom', on_press=self.image_zoom)
            button4.id = filename



            bl.add_widget(button3)
            bl.add_widget(button4)
            layout = GridLayout(cols=1, spacing=1, size_hint_y=None,height=220)

            # button.add_widget(button1)
            layout.add_widget(img)
            layout.add_widget(bl)
            glimg.add_widget(layout)


        root = ScrollView(size_hint=(1, 1), size=(1000,1000))
        root.add_widget(gl)
        return root


if __name__ == "__main__":
    BoxApp().run()

