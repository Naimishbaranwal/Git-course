import numpy

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder
from filesharer import FileSharer

import time

Builder.load_file('frontend2.kv')

class CameraScreen(Screen):
    def start(self):
        "start camera and changes button text"
        self.ids.camera.play=True
        self.ids.camera_button.text="Stop Camera"
        self.ids.camera.texture=self.ids.camera._camera.texture


    def stop(self):
        "stop camera and changes button text"
        self.ids.camera.play=False
        self.ids.camera_button.text="Start Camera"
        self.ids.camera.texture=None

    def capture(self):
        "Creates a filename with current time and captures and save image under that filename."
        current_time=time.strftime('%Y%m%d-%H%M%S')
        self.filepath=f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current='image_screen'
        self.manager.current_screen.ids.img.source=self.filepath



class ImageScreen(Screen):
    link_message="Create A Link First"

    def create_link(self):
        file_path=App.get_running_app().root.ids.camera_screen.filepath
        fileSharer=FileSharer(filepath=file_path)
        self.url=fileSharer.share()
        self.ids.link.text=self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text="Create a link first"

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text=self.link_message


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
    

MainApp().run()


