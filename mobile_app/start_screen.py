from kivy.lang.builder import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class StartScreen(MDScreen):
    pass


class StartApp(MDApp):
    def build(self):
        return StartScreen()


if __name__ == '__main__':
    Window.size = (360, 740)
    Builder.load_file('../ui/StartScreen.kv.kv')
    StartApp().run()
