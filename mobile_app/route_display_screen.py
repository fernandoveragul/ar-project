from kivy.lang.builder import Builder
from kivy.core.window import Window

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


class RouteDisplayScreen(MDScreen):
    pass


class RouteDisplayApp(MDApp):
    def build(self):
        return RouteDisplayScreen()


if __name__ == '__main__':
    Builder.load_file('../ui/RouteDisplayScreen.kv')
    Window.size = (360, 740)
    RouteDisplayApp().run()
