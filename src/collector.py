import kivy
from kivy.uix.button import *
from kivy.uix.label import *
from kivy.uix.gridlayout import *
from kivy.uix.textinput import *
from kivy.uix.popup import *
import src.report_handler as report_handler


class NameAgePopup(Popup):
    def __init__(self, **kwargs):
        super(NameAgePopup, self).__init__(**kwargs)
        self.layout = GridLayout(cols=1, rows=1, spacing=10, padding=50)
        self.layout.add_widget(Label(text='Please enter your name and age', font_size=30))
        self.add_widget(self.layout)
        # Once the user enters their name and age, store the information in a .csv file using report_handler.py
        self.name = TextInput(placeholder='Name')
        self.age = TextInput(placeholder='Age')
        self.layout.add_widget(self.name)
        self.layout.add_widget(self.age)
        self.layout.add_widget(Button(text='Submit', on_press=self.submit))
        self.add_widget(self.layout)

    def submit(self, instance):
        name = self.name.text.strip()
        age = self.age.text.strip()
        if not age.isnumeric():
            error_popup = Popup(title='Error', content=Label(text='Please enter a valid age'), size_hint=(0.5, 0.5))
            error_popup.open()
        elif int(age) < 0 or int(age) > 120:
            error_popup = Popup(title='Error', content=Label(text='Please enter an age between 0 and 120'), size_hint=(0.5, 0.5))
            error_popup.open()
        else:
            report_handler.add_name_age(name, age)
            success_popup = Popup(title='Success', content=Label(text='Your information has been stored'), size_hint=(0.5, 0.5))
            success_popup.open()
            self.dismiss()
