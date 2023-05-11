from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager

from start_screen import StartScreen
from profile_screen import ProfileScreen
from authorization_screen import AuthorizationScreen, AccessContent, ErrorContent
from route_display_screen import RouteDisplayScreen


class MainApp(MDApp):
    screen_manager = MDScreenManager()
    dialog = None

    def __init__(self):
        super().__init__()
        self.start_screen = None

    def close_dialog(self):
        self.dialog.dismiss()
        self.dialog = None

    def show_alert_access_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Access text',
                type='custom',
                content_cls=AccessContent()
            )
            self.dialog.open()

    def show_alert_error_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Error text',
                type='custom',
                content_cls=ErrorContent()
            )
            self.dialog.open()

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Indigo'
        self.start_screen = StartScreen(name='start_screen')
        self.screen_manager.add_widget(self.start_screen)
        self.screen_manager.add_widget(AuthorizationScreen(name='authorization_screen'))
        self.screen_manager.add_widget(ProfileScreen(name='profile_screen'))
        self.screen_manager.add_widget(RouteDisplayScreen(name='route_display_screen'))
        return self.screen_manager

    def on_start(self):
        Clock.schedule_interval(lambda x: self.start_screen.change_img(), 0.3)


if __name__ == '__main__':
    Window.size = (360, 740)
    Builder.load_file('../ui/StartScreen.kv')
    Builder.load_file('../ui/ProfileScreen.kv')
    Builder.load_file('../ui/AuthorizationScreen.kv')
    Builder.load_file('../ui/RouteDisplayScreen.kv')
    MainApp().run()
