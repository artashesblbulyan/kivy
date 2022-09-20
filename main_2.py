import json
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.uix.carousel import Carousel
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.modalview import ModalView
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from datetime import date
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.lang import Builder
from kivy.core.window import Window
from PIL import Image
from plyer import vibrator, email,camera


# first argument of createOneShot is the time in ms
# second argument is the amplitude (range from 1 to 255), -1 is device standard amplitude


Window.clearcolor = (98 / 225, 98 / 225, 98 / 225, 1)


if platform == 'android':
    from android.storage import primary_external_storage_path
    # from jnius import autoclass, cast
    #
    # PythonActivity = autoclass('org.kivy.android.PythonActivity')
    # activity = PythonActivity.mActivity
    # Context = autoclass('android.content.Context')
    #
    # vibrator_service = activity.getSystemService(Context.VIBRATOR_SERVICE)
    # vibrator = cast("android.os.Vibrator", vibrator_service)
    #
    # vibration_effect = autoclass("android.os.VibrationEffect")
    # vibrator.vibrate(vibration_effect.createOneShot(2000, 150))

    dir = primary_external_storage_path()
    if not os.path.exists(os.path.join(dir, 'Download/' + str(date.today()) + '/')): os.makedirs(
        os.path.join(dir, 'Download/' + str(date.today()) + '/'))
    if not os.path.exists(os.path.join(dir, 'Download/pahest/')): os.makedirs(os.path.join(dir, 'Download/pahest/'))
    download_dir_path = os.path.join(dir, 'Download/' + str(date.today()) + '/')
    image_dir_path = os.path.join(dir, 'Download/pahest/')
    partners_dir_path = os.path.join(dir, 'Download/')

else:
    if not os.path.exists(str(date.today())): os.makedirs(str(date.today()))
    download_dir_path = os.getcwd() + '\\' + str(date.today()) + '\\'
    image_dir_path = 'img_1'
    partners_dir_path = ''


def add_one_product(instance):
    instance.k.text = str(float(instance.k.text) + 1)


def send_mesage(instance):
    with open(download_dir_path+'PartnerName2022-09-16.json', "r") as xt_js_file:
        a = json.load(xt_js_file)
    recipient = 'abc@gmail.com'
    subject = 'Hi'
    text = a
    create_chooser = False
    email.send(recipient=recipient, subject=subject, text=text,
                    create_chooser=create_chooser)
    # instance.k.text = str(float(instance.k.text) + 1)



def reduce_one_product(instance):
    instance.k.text = str(float(instance.k.text) - 1)


Builder.load_file('editor.kv')


class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.filechooser.path = download_dir_path
            with open(filename[0], "r") as xt_js_file:
                a = json.load(xt_js_file)
                self.ids.my_image.text = json.dumps(a, indent=4, sort_keys=True)
        except:
            pass


class CustomWidget(Widget):

    def reposition_widgets(self):
        pass

    on_size = reposition_widgets


class BoxApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_Partners = ''
        self.textinput_1 = TextInput(text=str(date.today()), font_size=27)
        self.textinput = TextInput(text='PartnerName', font_size=27)
        self.filename = str(self.textinput.text + self.textinput_1.text + '.json')
        self.label = ''
        self.button2 = ''
        self.button1 = ''
        self.button5 = ''
        self.button6 = ''

    def image_zoom(self, instance):
        modal = ModalView()
        carousel = Carousel(direction='right', loop=True)
        for filename in os.listdir(image_dir_path):
            button = AsyncImage(source=image_dir_path + '/' + filename, allow_stretch=True, keep_ratio=True)
            img = GridLayout(cols=1, spacing=1)
            img.add_widget(button)

            bl = GridLayout(cols=6, spacing=1, size_hint_y=None, height=80)
            btpluss = GridLayout(cols=2, spacing=1, size_hint_y=None, height=80)

            self.button2 = TextInput(text='0', font_size=40, multiline=False)

            self.button1 = Slider(min=0, max=100, step=1)

            self.button1.k = self.button2
            bl.add_widget(self.button1)

            self.button1.bind(value=self.on_value_change)

            bl.add_widget(self.button2)
            self.label = Button(text=filename[:-4], on_press=self.add_number, font_size=30,
                                background_color=(1.0, 0.0, 0.0, 1.0))
            self.label.k = self.button2
            button4 = Button(text='X', font_size=30, background_color=(1.0, 0.0, 0.0, 1.0))
            button4.bind(on_press=modal.dismiss)
            button4.id = filename

            self.button5 = Button(text='+1', on_press=add_one_product, font_size=30)
            self.button5.instance = self.label
            self.button5.k = self.button2
            btpluss.add_widget(self.button5)

            self.button6 = Button(text='-1', on_press=reduce_one_product, font_size=30)
            self.button6.instance = self.label
            self.button6.k = self.button2
            btpluss.add_widget(self.button6)

            bl.add_widget(btpluss)
            bl.add_widget(self.label)

            bl.add_widget(button4)
            layout = GridLayout(cols=1, spacing=1)

            layout.add_widget(img)
            layout.add_widget(bl)
            carousel.add_widget(layout)
        modal.size_hint = (.99, .99)
        modal.add_widget(carousel)
        modal.open()

    def sumA(self, sumd):
        print('aaaaaa', sumd)
        return str(sumd)

    def add_number(self, instance):
        # vibrator.vibrate(time=4)
        self.filename = str(self.textinput.text + self.textinput_1.text + '.json')
        try:
            with open(download_dir_path + self.filename, "r") as xt_js_file:
                a = json.load(xt_js_file)
        except:
            self.add_file(instance)
            with open(download_dir_path + self.filename, "r") as xt_js_file:
                a = json.load(xt_js_file)
        with open(partners_dir_path + 'HAHA.json', "r") as ha_js_file:
            prices = json.load(ha_js_file)
            pri = 0
            for i in prices:
                if i['KOD'] == instance.text:
                    pri = i['purchaseprice']
        if a != []:
            sum = 0
            inx = 0
            for j in a:
                sum += j["sum"]
                if instance.text == j['kod']:
                    j["quantity"] = float(instance.k.text)
                    j["sum"] = float(instance.k.text) * j["price"]
                    inx += 1
            if inx == 0:
                data = {"kod": instance.text,
                        "quantity": float(instance.k.text),
                        "price": pri,
                        "sum": float(instance.k.text) * pri
                        }
                a.append(data)
        else:
            data = {"kod": instance.text,
                    "quantity": float(instance.k.text),
                    "price": pri,
                    "sum": float(instance.k.text) * pri
                    }
            a.append(data)
            sum = float(instance.k.text) * pri
        self.sumLabel.text = str(sum)
        with open(download_dir_path + self.filename, "w") as text_js_file:
            json.dump(a, text_js_file, indent=4, )
        try:
            with open(download_dir_path + "sum.json", "r") as sum_js_r_file:
                data_sum = json.load(sum_js_r_file)
        except:
            data_sum = {}
        with open(download_dir_path + "sum.json", "w") as sum_js_file:
            # data_sum =json.load(sum_js_file)
            data_sum[self.textinput.text] = sum
            json.dump(data_sum, sum_js_file, indent=4)

    def add_file(self, instance):
        self.filename = str(self.textinput.text + self.textinput_1.text + '.json')
        if self.filename in os.listdir(download_dir_path):
            with open(download_dir_path + self.filename, "r") as xt_js_file:
                a = json.load(xt_js_file)
                for j in self.bs:
                    if a != []:
                        for h in a:
                            if j == h['kod']:
                                print(j, h['kod'], h['quantity'])
                                self.bs[j].text = str(h['quantity'])
                                break
                            else:
                                self.bs[j].text = str(0)
                                break
                    else:
                        self.bs[j].text = str(0)
        if self.filename not in os.listdir(download_dir_path):
            with open(download_dir_path + self.filename, "a") as text_js_file:
                text = []
                json.dump(text, text_js_file, indent=4)
        return self.filename

    def save_partners_name(self, instance):

        partner_name = self.name_Partners.text
        text = []
        try:
            with open(partners_dir_path + 'partners.json', "r") as partner_js_file:
                partnersList = json.load(partner_js_file)
            if partner_name not in partnersList:
                with open(partners_dir_path + 'partners.json', "w") as text_js_file:
                    partnersList.append(partner_name)
                    json.dump(partnersList, text_js_file, indent=4)
        except:
            with open(partners_dir_path + 'partners.json', "w") as text_js_file:
                text.append(partner_name)
                json.dump(text, text_js_file, indent=4)

    def partners_name_input(self, instance):
        try:
            with open(download_dir_path + "sum.json", "r") as sum_js_r_file:
                data_sum = json.load(sum_js_r_file)
                self.sumLabel.text = str(data_sum[instance.text])
        except:
            self.sumLabel.text = str(0)

        self.textinput.text = instance.text

    def list_partners(self, instance):
        modal = ModalView(auto_dismiss=True, size_hint_y=None)
        Partners_Save_Gl = GridLayout(cols=2, spacing=1, height=90, size_hint_y=None)
        Partners_list_Gl = GridLayout(cols=1, spacing=1, size_hint_y=None, height=500)
        Partners_list_Gl.bind(minimum_height=Partners_list_Gl.setter('height'))
        Partners_sum_Gl = GridLayout(cols=2, spacing=1, size_hint_y=None)
        self.name_Partners = TextInput(text='NamePartners', font_size=30)
        ok_Name_Partners = Button(text='Save Partners', on_press=self.save_partners_name)
        Partners_Save_Gl.add_widget(self.name_Partners)
        Partners_Save_Gl.add_widget(ok_Name_Partners)
        Partners_list_Gl.add_widget(Partners_Save_Gl)
        Partners_list_Gl.add_widget(Partners_sum_Gl)
        try:
            with open(partners_dir_path + 'partners.json', "r") as partner_js_file:
                partnersList = json.load(partner_js_file)
            try:
                with open(download_dir_path + "sum.json", "r") as sum_js_r_file:
                    data_sum = json.load(sum_js_r_file)
            except:
                data_sum = ""
            for buttonPartners in partnersList:
                Part_list_button = Button(text=buttonPartners, on_press=self.partners_name_input, size_hint_y=None,
                                          height=50)
                if buttonPartners in data_sum:
                    label_sum = Label(text=str(data_sum[buttonPartners]), font_size=30)
                else:
                    label_sum = Label(text="0", font_size=30)
                Partners_sum_Gl.add_widget(Part_list_button)
                Partners_sum_Gl.add_widget(label_sum)
                Part_list_button.bind(on_press=modal.dismiss)
        except:
            with open(partners_dir_path + 'partners.json', "w"):
                pass
        k = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        k.add_widget(Partners_list_Gl)
        modal.size_hint = (.9, .9)
        modal.add_widget(k)
        modal.open()
        return k

    def on_value_change(self, instance, value):
        instance.k.text = str(value)

    def load(self, path):
        modal = ModalView(auto_dismiss=True, )
        a = MyLayout()
        modal.size_hint = (.9, .9)
        modal.add_widget(a)
        modal.open()
        return a

    def list_order(self, instance):
        modal = ModalView(auto_dismiss=True, size_hint_y=None)
        Partners_Save_Gl = GridLayout(cols=2, spacing=1, height=80, size_hint_y=None)
        Partners_list_Gl = GridLayout(cols=2, spacing=1, size_hint_y=None, height=500)
        Partners_list_Gl.bind(minimum_height=Partners_list_Gl.setter('height'))
        self.name_Partners = TextInput(text='NamePartners', font_size=30)
        ok_Name_Partners = Button(text='Save Partners', on_press=self.save_partners_name)
        Partners_Save_Gl.add_widget(self.name_Partners)
        Partners_Save_Gl.add_widget(ok_Name_Partners)
        Partners_list_Gl.add_widget(Partners_Save_Gl)

        if os.path.exists('partners.txt'):
            with open(partners_dir_path + 'partners.txt', "r") as partner_js_file:
                partnersList = partner_js_file.readlines()
                for buttonPartners in partnersList:
                    Part_list_button = Button(text=buttonPartners[:-1], on_press=self.partners_name_input,
                                              size_hint_y=None,
                                              height=40)
                    Part_list_button.bind(minimum_height=Part_list_button.setter)
                    Partners_list_Gl.add_widget(Part_list_button)
                    Part_list_button.bind(on_press=modal.dismiss)
        else:
            with open(partners_dir_path + 'partners.txt', "a"):
                pass
        k = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        k.add_widget(Partners_list_Gl)
        modal.size_hint = (.9, .9)
        modal.add_widget(k)
        modal.open()
        return k

    def on_value_change(self, instance, value):
        instance.k.text = str(value)

    def load(self, path):
        modal = ModalView(auto_dismiss=True, )
        a = MyLayout()
        modal.size_hint = (.9, .9)
        modal.add_widget(a)
        modal.open()
        return a

    def build(self):
        btn = Button(text='File', on_press=self.load,
                     font_size=35,
                     bold=True,
                     background_color=(0.0, 0.0, 0.0, 1.0),
                     background_down="atlas://data/images/defaulttheme/button_pressed"
                     )
        message = Button(text='mess', on_press=send_mesage,
                     font_size=35,
                     bold=True,
                     background_color=(0.0, 0.0, 0.0, 1.0),
                     background_down="atlas://data/images/defaulttheme/button_pressed"
                     )
        carousel = Carousel()
        gl = GridLayout(cols=1, spacing=1, size_hint_y=None)
        al = GridLayout(cols=1, spacing=2)
        gltext = GridLayout(cols=5, spacing=1, size_hint_y=None, height=100)
        file = GridLayout(cols=2, spacing=1, size_hint_y=None, height=100)
        text_name = GridLayout(cols=1, spacing=2, size_hint_y=None, height=100)
        textbutton = Button(text='OK', on_press=self.add_file,
                            font_size=35,
                            bold=True,
                            background_color=(0.0, 0.0, 0.0, 1.0),
                            background_down="True",
                            border=(20, 20, 20, 20),
                            )
        self.sumLabel = Label(text='SUM', font_size=35,
                              color=(0.0, 0.0, 0.0, 1.0),
                              bold=True,
                              )
        partnerlistbut = Button(text='List', on_press=self.list_partners,
                                font_size=35,
                                bold=True,
                                background_color=(0.0, 0.0, 0.0, 1.0),
                                background_down="True"
                                )
        file.add_widget(partnerlistbut)
        gltext.add_widget(self.sumLabel)
        gltext.add_widget(text_name)
        text_name.add_widget(self.textinput)
        text_name.add_widget(self.textinput_1)
        gltext.add_widget(textbutton)
        gltext.add_widget(file)
        file.add_widget(btn)
        file.add_widget(message)
        al.add_widget(gltext)
        glimg = GridLayout(cols=1, spacing=1, size_hint_y=None)
        glimg.bind(minimum_height=gl.setter('height'))
        gl.add_widget(glimg)
        self.bs = {}
        for filename in os.listdir(image_dir_path):
            button = AsyncImage(source=image_dir_path + '/' + filename, allow_stretch=True, keep_ratio=True,
                                on_press=self.image_zoom)
            width, height = Image.open(image_dir_path + '/' + filename).size
            height = Window.width * height / width
            img = GridLayout(cols=1, spacing=1, size_hint_y=None, height=height)
            img.add_widget(button)
            bl = GridLayout(cols=6, spacing=1, size_hint_y=None, height=100)
            btpluss = GridLayout(cols=2, spacing=1, size_hint_y=None, height=100)
            self.button2 = TextInput(text='0', font_size=45, multiline=False)
            self.button1 = Slider(min=0, max=100, step=1,
                                  )
            self.button1.k = self.button2
            bl.add_widget(self.button1)
            self.button1.bind(value=self.on_value_change)
            self.bs[filename[:-4]] = self.button2
            bl.add_widget(self.button2)
            self.label = Button(text=filename[:-4], on_press=self.add_number,
                                font_size=35,
                                bold=True,
                                background_color=(0.0, 0.0, 0.0, 1.0),
                                background_down="True"
                                )
            self.label.k = self.button2
            self.button1.d = self.label.text
            rl = RelativeLayout(size_hint_y=None, height=height + 100)
            button4 = Button(text='Zoom', on_press=self.image_zoom,
                             font_size=35,
                             bold=True,
                             background_color=(0.0, 0.0, 0.0, 1.0),
                             )
            button4.id = filename
            self.button5 = Button(text='+1', on_press=add_one_product,
                                  font_size=35,
                                  bold=True,
                                  background_color=(0.0, 0.0, 0.0, 1.0),
                                  background_normal=""
                                  )
            self.button5.instance = self.label
            self.button5.k = self.button2
            btpluss.add_widget(self.button5)
            self.button6 = Button(text='-1', on_press=reduce_one_product,
                                  font_size=35,
                                  bold=True,
                                  background_color=(0.0, 0.0, 0.0, 1.0),
                                  background_down="True"
                                  )
            self.button6.instance = self.label
            self.button6.k = self.button2
            btpluss.add_widget(self.button6)
            bl.add_widget(btpluss)
            bl.add_widget(self.label)

            bl.add_widget(button4)
            layout = GridLayout(cols=1, spacing=1, size_hint_y=None, height=height + 100)
            layout.add_widget(img)
            layout.add_widget(bl)
            rl.add_widget(layout)
            glimg.add_widget(rl)
        root = ScrollView(size_hint_y=None, size=(Window.width, Window.height))
        root.add_widget(gl)
        al.add_widget(root)
        return al


if __name__ == "__main__":
    BoxApp().run()
