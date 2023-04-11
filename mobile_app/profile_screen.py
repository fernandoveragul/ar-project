from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen


class ProfileScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Маршрут {i+1}",
                "height": 50,
                "on_release": lambda x=f"Маршрут {i+1}": self.set_item(x),
            } for i in range(5)
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
            max_height=155
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self.menu.dismiss()


class ProfileApp(MDApp):
    def build(self):
        return ProfileScreen()


if __name__ == '__main__':
    Builder.load_file('../ui/ProfileScreen.kv')
    Window.size = (360, 740)
    ProfileApp().run()
