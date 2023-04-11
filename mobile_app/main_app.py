from kivy.lang.builder import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager

from start_screen import StartScreen
from profile_screen import ProfileScreen
from authorization_screen import AuthorizationScreen, AccessContent, ErrorContent


class MainApp(MDApp):
    screen_manager = MDScreenManager()
    dialog = None

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
        self.screen_manager.add_widget(StartScreen(name='start_screen'))
        self.screen_manager.add_widget(ProfileScreen(name='profile_screen'))
        self.screen_manager.add_widget(AuthorizationScreen(name='authorization_screen'))
        return self.screen_manager


if __name__ == '__main__':
    Window.size = (360, 740)
    Builder.load_file('../ui/StartScreen.kv')
    Builder.load_file('../ui/ProfileScreen.kv')
    Builder.load_file('../ui/AuthorizationScreen.kv')
    MainApp().run()
