from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import mysql.connector


Window.size = (410, 680)

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
        
        #self.ids.username.text = ""
        #self.ids.password.text = ""
        
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

                mycursor.execute("SELECT * FROM databasetablebeta WHERE Username = '" + username_input + "' and Password = '"+password_input +"'")
                #mycursor.execute("SELECT * FROM databasetablebeta WHERE Username = %s AND Password = %s", (username_input, password_input))

                AdminUser = ""
                AdminPassword = ""
                
                row = mycursor.fetchone()
                
                if row:
                    AdminID = row[0]
                    AdminUser = str(row[1])
                    AdminPassword = str(row[2])
                    
                    print(AdminID)
                    print("DB Username:",AdminUser)
                    print("DB Password:",AdminPassword)
                    
                    print("Input Username:",username_input)
                    print("Input Password:",password_input)
                    

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

class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.create_account_screen = CreateAccountScreen(name='create_account')
        self.create_account_screen2 = CreateAccountScreen2(name='create_account2')
        self.dashboard_tab = DashboardTab(name='dashboard_tab')
        self.about_center_tab = AboutCenterTab(name='about_center_tab')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.create_account_screen)
        self.sm.add_widget(self.create_account_screen2)
        self.sm.add_widget(self.dashboard_tab)
        self.sm.add_widget(self.about_center_tab)    
        return self.sm

if __name__ == '__main__':
    Builder.load_file("main.kv")
    TestApp().run()
