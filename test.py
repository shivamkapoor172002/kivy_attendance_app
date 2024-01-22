import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import shutil

class FileDownloaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.file_path = "Attendance.xls"

        self.download_button = Button(text="Download File", on_press=self.download_file)
        self.layout.add_widget(self.download_button)

        return self.layout

    def download_file(self, instance):
        destination_directory = self.get_downloads_directory()
        if destination_directory:
            destination_path = os.path.join(destination_directory, 'downloaded_file.xls')
            try:
                shutil.copyfile(self.file_path, destination_path)
                print(f"File '{self.file_path}' copied to '{destination_path}' successfully!")
            except Exception as e:
                print(f"Error copying file: {e}")
        else:
            print("Error getting Downloads directory on Android")

    def get_downloads_directory(self):
        try:
            from jnius import autoclass, cast
            Environment = autoclass('android.os.Environment')
            return cast('java.lang.String', Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS).toString())
        except Exception as e:
            print(f"Error getting Downloads directory: {e}")
            return None

if __name__ == '__main__':
    FileDownloaderApp().run()
