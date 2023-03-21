from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class CameraClick(BoxLayout):
    def on_play(self):
        camera = self.ids['camera']
        toggle_button = self.ids['toggle_button']
        camera.play = not camera.play
        toggle_button.text = 'Выключить' if camera.play else 'Включить'


class TestCamera(App):
    def build(self):
        return CameraClick()


if __name__ == '__main__':
    Builder.load_file('ui.kv')
    TestCamera().run()