from kivy.lang.builder import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class StartScreen(MDScreen):
    num_photo = 1

    def change_img(self):
        self.num_photo = self.num_photo % 3 + 1
        self.ids.photos.source = f'../img/{self.num_photo}.jpg'


class StartApp(MDApp):
    def build(self):
        return StartScreen()


if __name__ == '__main__':
    Window.size = (360, 740)
    Builder.load_file('../ui/StartScreen.kv')
    StartApp().run()
