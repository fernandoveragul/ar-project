from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton


class Content(BoxLayout):
    pass


class StartWindow(MDApp):
    dialog = None

    # access_dialog = MDDialog(
    #     title='Access text',
    #     buttons=[
    #         MDFlatButton(
    #             text='Перейти к маршруту'
    #         )
    #     ]
    # )

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Indigo'
        return Builder.load_file('../ui/StartWindow.kv')

    def dialog_close(self):
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
    StartWindow().run()
