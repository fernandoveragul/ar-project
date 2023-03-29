from kivy.lang import Builder
from kivy.core.text import LabelBase

from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.3
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Indigo'

        LabelBase.register(name='Inter', fn_regular='../fonts/Inter-Bold.ttf')
        theme_font_styles.append('Inter')
        self.theme_cls.font_styles['Inter'] = [
            'Inter',
            16,
            False,
            0.15
        ]

        return Builder.load_file('../ui/learn_kivymd.kv')

    def change_theme_style(self) -> None:
        self.theme_cls.primary_palette = ('Indigo' if self.theme_cls.primary_palette == 'Green' else 'Green')
        self.theme_cls.theme_style = ('Dark' if self.theme_cls.theme_style == 'Light' else 'Light')


if __name__ == '__main__':
    LoginApp().run()
