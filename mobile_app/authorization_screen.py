from kivy.lang.builder import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout


class AccessContent(MDBoxLayout):
    pass


class ErrorContent(MDBoxLayout):
    pass


class AuthorizationScreen(MDScreen):
    pass


class AuthorizationApp(MDApp):
    def build(self):
        return AuthorizationScreen()


if __name__ == '__main__':
    Window.size = (360, 740)
    Builder.load_file('../ui/AuthorizationScreen.kv')
    AuthorizationApp().run()
