from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRectangleFlatButton
import pandas as pd
import os

class_name = """
MDTextField:
    hint_text: "Enter class name"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    size_hint_x:None
    width:300
"""


class Example(MDApp):
    def build(self):
        self.className = Builder.load_string(class_name)
        button = MDRectangleFlatButton(text='Submit',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.8},
                                       on_release=self.submit_btn)
        DATA = pd.read_excel("Attendance.xls")
        DATA = DATA.iloc[:, 0:]
        cols = DATA.columns.values
        values = DATA.values

        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)

        layout = MDFloatLayout()
        layout.add_widget(self.data_tables)
        layout.add_widget(self.className)
        layout.add_widget(button)
        return layout

    def open_table(self, instance):
        self.data_tables.open()

    def submit_btn(self, instance):
        # Get the class name from the MDTextField
        class_name1 = self.className.text

        # Construct the file path
        file_path = os.path.join("database", f"{class_name1}", "Attendance.xls")

        try:
            # Read the Excel file
            DATA = pd.read_excel(file_path)
            DATA = DATA.iloc[:, 0:]
            cols = DATA.columns.values
            values = DATA.values

            self.data_tables.column_data = [(col, dp(30)) for col in cols]
            self.data_tables.row_data = values

        except FileNotFoundError:
            print(f"File {file_path} not found. Please check the file path.")

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)


Example().run()
