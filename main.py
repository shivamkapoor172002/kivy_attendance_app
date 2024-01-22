from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.lang import Builder
from plyer import filechooser
import os

kv = """
ScreenManager:
    LoginScreen:
    DashboardScreen:
    DatabaseScreen:

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(48)
        spacing: dp(16)

        MDTextField:
            id: user_id
            hint_text: "User ID"
            helper_text: "Default: admin"
            helper_text_mode: "on_focus"
            pos_hint: {"center_x": 0.5}
            size_hint_x: None
            width: "250dp"

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            helper_text: "Default: dei2020"
            helper_text_mode: "on_focus"
            pos_hint: {"center_x": 0.5}
            size_hint_x: None
            width: "250dp"

        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5}
            on_release: root.check_credentials()

<DashboardScreen>:
    name: 'dashboard'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(48)
        spacing: dp(16)

        MDRaisedButton:
            text: "Database"
            on_release: root.manager.current = 'database'

        MDRaisedButton:
            text: "Attendance Marker"
            on_release: root.show_attendance_marker()

        MDRaisedButton:
            text: "Previous Attendance"
            on_release: root.show_previous_attendance()

        MDRaisedButton:
            text: "Download Excel"
            on_release: root.download_excel()

        MDRaisedButton:
            text: "Back"
            on_release: root.manager.current = 'login'

<DatabaseScreen>:
    name: 'database'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(48)
        spacing: dp(16)

        MDRaisedButton:
            text: "Iot"
            on_release: root.show_student_list()

        MDRaisedButton:
            text: "Back"
            on_release: root.manager.current = 'dashboard'

"""


class LoginScreen(Screen):
    def check_credentials(self):
        user_id = self.ids.user_id.text
        password = self.ids.password.text

        if user_id == "admin" and password == "dei2020":
            self.manager.current = 'dashboard'
        else:
            self.show_invalid_credentials()

    def show_invalid_credentials(self):
        dialog = MDDialog(
            title="Invalid Credentials",
            text="Please enter correct user ID and password.",
            buttons=[MDRaisedButton(text="OK", on_release=lambda *x: dialog.dismiss())],
        )
        dialog.open()



class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None  # Declare the dialog variable here

    def show_attendance_marker(self):
        def on_enter(instance, value):
            print('User pressed enter in', instance)
        # Create a dialog with a text input and an "Upload" button
        text_input = TextInput(text='Enter class name')
        text_input.bind(on_text_validate=on_enter)

        # Create a box layout to contain the text input and the button
        content = MDBoxLayout(orientation='vertical', spacing=10)
        content.add_widget(text_input)

        # Create a box layout for buttons
        button_box = MDBoxLayout(orientation='horizontal', spacing=10)

        # Create an "Upload" button
        upload_button = MDRaisedButton(text="Upload", on_release=lambda x: self.upload_file(text_input.text))
        button_box.add_widget(upload_button)

        # Create a "Cancel" button
        cancel_button = MDRaisedButton(text="Cancel", on_release=lambda *x: self.dialog.dismiss())
        button_box.add_widget(cancel_button)

        content.add_widget(button_box)

        # Create a dialog with the box layout as content
        self.dialog = MDDialog(
            title="Enter Class Name",
            content_cls=content,
        )
        self.dialog.open()

    def upload_file(self, class_name):
        database_dir = "database/"
        class_dir = os.path.join(database_dir, class_name)

        if os.path.exists(class_dir) and os.path.isdir(class_dir):
            filechooser.open_file(on_selection=lambda x: self.selected_file(class_name, x))
        else:
            self.show_error("Database Not Found", f"The database for class '{class_name}' does not exist.")

    def selected_file(self, class_name, selection):
        print(f"Selected Class: {class_name}, File: {selection}")

    def show_previous_attendance(self):
        print("Show Previous Attendance")

    def download_excel(self):
        print("Download Excel")

    def show_error(self, title, text):
        dialog = MDDialog(title=title, text=text, buttons=[MDRaisedButton(text="OK")])
        dialog.open()

class DatabaseScreen(Screen):
    def show_student_list(self):
        print("Show Student List")

class AttendityApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    AttendityApp().run()
