from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import calendar
from datetime import datetime
import mysql.connector

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

        self.dismiss_button = Button(text='Dismiss', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.05})
        self.dismiss_button.bind(on_release=self.dismiss)
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
                btn = Button(text=str(day))
                btn.bind(on_release=self.select_date)
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
                        print("okay na maongca?")
                    else:
                        print("nah Id win")

                else:
                    print("it didnt work, gowd fucking damn it")

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

class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.create_account_screen2 = CreateAccountScreen2(name='create_account2')
        self.dashboard_tab = DashboardTab(name='dashboard_tab')
        self.about_center_tab = AboutCenterTab(name='about_center_tab')
        self.notification_tab = NotificationTab(name='notification_tab')
        self.messages_tab = MessagesTab(name='messages_tab')
        self.account_tab = AccountTab(name='account_tab')
        self.information_screen = InformationScreen(name='information_screen')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        self.sm.add_widget(self.create_account_screen2)
        self.sm.add_widget(self.dashboard_tab)  
        self.sm.add_widget(self.about_center_tab)
        self.sm.add_widget(self.notification_tab)
        self.sm.add_widget(self.messages_tab)
        self.sm.add_widget(self.account_tab)
        self.sm.add_widget(self.information_screen) # Add Information Screen
        return self.sm

if __name__ == '__main__':
    Builder.load_file("main.kv")
    Builder.load_file("createAccount.kv")
    Builder.load_file("createAccount2.kv")
    Builder.load_file("Notification.kv")
    Builder.load_file("Dashboard.kv")
    Builder.load_file("AboutCenter.kv")
    Builder.load_file("Message.kv")
    Builder.load_file("Notification.kv")
    
    TestApp().run()
