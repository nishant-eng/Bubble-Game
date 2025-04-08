# medicine_alarm_app.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.popup import Popup
from datetime import datetime
import time

class MedicineAlarm(BoxLayout):
    def __init__(self, **kwargs):
        super(MedicineAlarm, self).__init__(orientation='vertical', **kwargs)
        
        self.medicine_label = Label(text='Enter Medicine Name:')
        self.add_widget(self.medicine_label)
        self.medicine_input = TextInput(multiline=False)
        self.add_widget(self.medicine_input)

        self.time_label = Label(text='Enter Alarm Time (HH:MM, 24-hour):')
        self.add_widget(self.time_label)
        self.time_input = TextInput(multiline=False)
        self.add_widget(self.time_input)

        self.set_alarm_btn = Button(text='Set Alarm')
        self.set_alarm_btn.bind(on_press=self.set_alarm)
        self.add_widget(self.set_alarm_btn)

    def set_alarm(self, instance):
        self.medicine = self.medicine_input.text
        self.alarm_time = self.time_input.text
        Clock.schedule_interval(self.check_alarm, 30)  # check every 30 seconds

        popup = Popup(title='Alarm Set',
                      content=Label(text=f'Alarm set for {self.alarm_time}'),
                      size_hint=(0.6, 0.4))
        popup.open()

    def check_alarm(self, dt):
        now = datetime.now().strftime('%H:%M')
        if now == self.alarm_time:
            self.show_alarm()
            return False  # stop checking after triggering

    def show_alarm(self):
        popup = Popup(title='Medicine Time!',
                      content=Label(text=f'Take your medicine: {self.medicine}'),
                      size_hint=(0.6, 0.4))
        popup.open()

class MedicineApp(App):
    def build(self):
        return MedicineAlarm()

if __name__ == '__main__':
    MedicineApp().run()
