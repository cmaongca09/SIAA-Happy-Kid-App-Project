from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from datetime import datetime

import calendar
import mysql.connector
import calendar
import os
import sys


Window.size = (380, 650)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Builder.load_file(resource_path('main.kv'))
Builder.load_file(resource_path('createAccount.kv'))
Builder.load_file(resource_path('createAccount2.kv'))
Builder.load_file(resource_path('Dashboard.kv'))
Builder.load_file(resource_path('termsandcondition.kv'))


import mysql.connector
from datetime import datetime
import calendar

Window.size = (380, 650)


class DatePicker(TextInput):
    def __init__(self, **kwargs):
        super(DatePicker, self).__init__(**kwargs)
        self.text = datetime.now().strftime('%Y-%m-%d')
        self.bind(focus=self.show_calendar)

    def show_calendar(self, instance, value):
        if value:
            self.parent.parent.disabled = True
            self.popup = DatePickerPopup(self)
            self.popup.open()
        else:
            self.parent.parent.disabled = False

class DatePickerPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(DatePickerPopup, self).__init__(**kwargs)
        self.parent_widget = parent
        self.title = 'Select a Date'
        self.size_hint = (0.9, 0.9)
        self.content = FloatLayout()

        self.layout = GridLayout(cols=7, size_hint=(1, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.content.add_widget(self.layout)

        self.update_calendar(datetime.now().year, datetime.now().month)

        self.dismiss_button = Button(text='Dismiss', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.05}, background_color=(0, 0, 0, 0))
        self.dismiss_button.bind(on_release=self.dismiss)
        self.dismiss_button.color = (1, 1, 1, 1)  # White text color
        self.content.add_widget(self.dismiss_button)

    def update_calendar(self, year, month):
        self.layout.clear_widgets()
        days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        for day in days:
            self.layout.add_widget(Label(text=day, color=(1, 1, 1, 1)))

        cal = calendar.Calendar().itermonthdays2(year, month)
        for day, weekday in cal:
            if day == 0:
                self.layout.add_widget(Label(text='', color=(1, 1, 1, 1)))
            else:
                btn = Button(text=str(day), background_color=(0, 0, 0, 0))
                btn.bind(on_release=self.select_date)
                btn.color = (1, 1, 1, 1)  # White text color
                self.layout.add_widget(btn)

    def select_date(self, instance):
        selected_date = datetime.strptime(
            f"{datetime.now().year}-{datetime.now().month}-{instance.text}", '%Y-%m-%d')
        self.parent_widget.text = selected_date.strftime('%Y-%m-%d')
        self.dismiss()

class LoginScreen(Screen):
    def create_account(self):
        self.manager.current = 'create_account'

    def LogInPress(self):
        host = 'localhost'
        port = '3306'
        user = 'root'
        password = ''
        database = 'test'

        username_input = self.ids.username.text
        password_input = self.ids.password.text

        print(f"Hello {username_input} and your password is {password_input}")

        try:
            connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                print("Connected to MySQL database")

                mycursor = connection.cursor()
                mycursor.execute("SELECT * FROM databasetablebeta WHERE Username = %s AND Password = %s", (username_input, password_input))

                row = mycursor.fetchone()

                if row:
                    AdminID = row[0]
                    AdminUser = str(row[1])
                    AdminPassword = str(row[2])

                    print(AdminID)
                    print("DB Username:", AdminUser)
                    print("DB Password:", AdminPassword)

                    print("Input Username:", username_input)
                    print("Input Password:", password_input)

                    if username_input == AdminUser and password_input == AdminPassword:
                        print("Login successful")
                    else:
                        print("Username or password incorrect")

                else:
                    print("Username or password incorrect")

        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

        finally:
            if 'connection' in locals():
                connection.close()
                print("MySQL connection closed")

class CreateAccountScreen(Screen):
    pass

class CreateAccountScreen2(Screen):
    pass

class DashboardTab(Screen):
    pass

class AboutCenterTab(Screen):
    pass

class NotificationTab(Screen):
    pass

class MessagesTab(Screen):
    pass

class AccountTab(Screen):
    pass

class InformationScreen(Screen):
    pass

class TermsAndConditionTab(Screen):
    pass

class TestApp(App):
    def build(self):
        self.sm = CustomScreenManager()  # Use custom ScreenManager
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.create_account_screen2 = CreateAccountScreen2(name='create_account2')
        self.dashboard_tab = DashboardTab(name='dashboard_tab')
        self.about_center_tab = AboutCenterTab(name='about_center_tab')
        self.notification_tab = NotificationTab(name='notification_tab')
        self.messages_tab = MessagesTab(name='messages_tab')
        self.account_tab = AccountTab(name='account_tab')
        self.information_screen = InformationScreen(name='information_screen')
        self.terms_and_condition_tab = TermsAndConditionTab(name="termsConditionTab")
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        self.sm.add_widget(self.create_account_screen2)
        self.sm.add_widget(self.dashboard_tab)  
        self.sm.add_widget(self.about_center_tab)
        self.sm.add_widget(self.notification_tab)
        self.sm.add_widget(self.messages_tab)
        self.sm.add_widget(self.account_tab)
        self.sm.add_widget(self.information_screen)  # Add Information Screen
        self.sm.add_widget(self.terms_and_condition_tab)
        self.sm.add_widget(CreateAccountScreen(name='create_account'))
        self.sm.add_widget(TermsAndConditionTab(name="termsConditionTab"))
        return self.sm

    def show_terms_popup(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        scroll = ScrollView(size_hint=(1, None), size=(Window.width * 0.9, Window.height * 0.7))
        terms_label = Label(
            text="HAPPY KID CENTER\n\n\n\n12 YEARS IN SERVICE\n\n1. STRICTLY NO WALK IN POLICY\n\n2. We accept children with:\n   • Speech delay\n  • Autism Spectrum Disorder\n  • Global Developmental Delay\n  • Slow Learner\n    • Hyperactive\n • ADHD\n    • Intellectual Disability\n\nTherapy Fees Information\nP2,000 Initial Assessment \n– This is to assess the main issue of the child’s delay that can be used for our treatment planning)\nP3,000 Deposit – Purpose of Deposit:\n    • Absences without notifying us, is considered deduction of     Therapy Fee on you Deposit\n    • Absences requires make up session\n    • Minimum of 6 Months (Unless the doctor will give you a   specific number of months of therapy then we will allow   short term therapy)\n    • Non Refundable as cash but can be consumed thru Therapy    Sessions (With min. stay of 6 Months)\n\nBEHAVIORAL INTERVENTION\n    • P500 per hour\n\nSPEECH PROGRAM\n    • P500 per hour\n\nSteps to secure a slot for Assessment\n    • Pay P500 to Reserve a slot for Assessment (Non    Refundable for any reason including Change of Schedule)\n    • Fill out the Appointment Form for the client information.\n    • Available schedule will appear as soon as you complete the     2 step.\n    • Remaining P1500 should be paid after the initial     assessment.\n\nBranches of Happy Kid Center\n    • Urdaneta, Pangasinan\n    • Lingayen, Pangasinan \n\n APPOINTMENT FORM\n\n GCash (P500 Payment for Slot Reservation) \nRowena R. – 09458509059  \n Please take screenshot of the payment for proof",
            size_hint_y=None,
            height=Window.height * 0.7,
            width=Window.width * 0.85,
            color=(0, 0, 0, 1),
            font_size=16,
            text_size=(Window.width * 0.70, None),
            valign='top'
        )
        terms_label.bind(texture_size=terms_label.setter('size'))
        scroll.add_widget(terms_label)
        content.add_widget(scroll)

        dismiss_button = Button(text='Close', size_hint=(1, None), height=40, pos_hint={'center_x': 0.5})
        dismiss_button.bind(on_release=lambda x: popup.dismiss())
        content.add_widget(dismiss_button)

        popup = Popup(
            title='KLARINS DEYB "ALYAS HEB DABE" MAONGSHORT HAHAHA ',
            content=content,
            size_hint=(0.9, 0.9),
            background='try.jpg',
            background_color=(1, 1, 1, 1),
            title_color=(0, 0, 0, 1),
        )
        popup.open()

class CustomScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(CustomScreenManager, self).__init__(**kwargs)
        self.transition = FadeTransition()  # Change the transition to FadeTransition for a fade effect
        Clock.schedule_once(self.enable_transition, 5)  # Schedule enabling transition after 1 second

    def enable_transition(self, dt):
        self.transition = FadeTransition()  # Change to the desired transition after delay

if __name__ == '__main__':
    Builder.load_file("main.kv")
    Builder.load_file("createAccount.kv")
    Builder.load_file("createAccount2.kv")
    Builder.load_file("Dashboard.kv")
    Builder.load_file("termsandcondition.kv")
    

    TestApp().run()
