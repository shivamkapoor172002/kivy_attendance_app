from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from plyer import filechooser

username_input = """
MDTextField:
    hint_text: "Enter class name"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

file_path="""
MDFloatLayout:
    MDRaisedButton:
        text:"Upload"
        pos_hint:{"center_x":0.5,"center_y":0.4}
        on_release:
            app.file_chooser()
"""


class DemoApp(MDApp):
    class_name=''
    filePath=''
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(username_input)

        self.file_path=Builder.load_string(file_path)
        button = MDRectangleFlatButton(text='Submit',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        screen.add_widget(self.file_path)
        return screen

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self,selection):
        self.filePath=selection[0]
        print(selection[0])
    def show_data(self,obj):
        class_name=self.username.text
        print(self.filePath,class_name)
        print()


DemoApp().run()