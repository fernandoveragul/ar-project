from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from profile_screen import ProfileScreen


class Content(BoxLayout):
    pass


class StartScreen(MDScreen):
    pass


class MainApp(MDApp):
    dialog = None
    sm = MDScreenManager()

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Indigo'
        self.sm.add_widget(StartScreen(name='start_screen'))
        self.sm.add_widget(ProfileScreen(name='profile_screen'))
        return self.sm

    def close_dialog(self):
        self.dialog.dismiss(force=True)
        self.dialog = None

    def show_alert_dialog_authorization(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Авторизация',
                type="custom",
                content_cls=Content()
            )
            self.dialog.open()

    def show_alert_error_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Error text',
                buttons=[
                    MDRaisedButton(text='Понятно')
                ]
            )
            self.dialog.open()


if __name__ == '__main__':
    Window.size = (360, 740)
    Builder.load_file('../ui/StartScreen.kv')
    Builder.load_file('../ui/ProfileScreen.kv')
    MainApp().run()
