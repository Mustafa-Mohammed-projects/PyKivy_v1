"""PyKivy - a Kivy starter app: 3-second splash + mini Python editor/runner."""
import contextlib
import io
import traceback

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#0E1018")

DEFAULT_CODE = """import sys
print("Hello from Kivy!")
print("Python", sys.version.split()[0])
for i in range(1, 6):
    print(i, "squared =", i * i)
"""

KV = """
<SplashScreen>:
    name: "splash"
    canvas.before:
        Color:
            rgba: 0.055, 0.063, 0.094, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        source: "data/presplash.png"
        size_hint: None, None
        size: min(root.width, root.height) * .6, min(root.width, root.height) * .6
        pos_hint: {"center_x": .5, "center_y": .5}

<EditorScreen>:
    name: "editor"
    BoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(10)
        Label:
            text: "PyKivy"
            size_hint_y: None
            height: dp(44)
            font_size: sp(20)
            bold: True
            halign: "left"
            text_size: self.size
            color: 0.9, 0.91, 0.95, 1
        TextInput:
            id: code
            background_color: 0.082, 0.094, 0.149, 1
            foreground_color: 0.9, 0.91, 0.95, 1
            cursor_color: 0.545, 0.486, 1, 1
            font_size: sp(14)
            padding: dp(12)
        Button:
            text: "Run"
            size_hint_y: None
            height: dp(52)
            background_normal: ""
            background_color: 0.545, 0.486, 1, 1
            color: 0.04, 0.04, 0.1, 1
            bold: True
            on_release: root.run_code()
        ScrollView:
            size_hint_y: .4
            Label:
                id: out
                size_hint_y: None
                height: max(self.texture_size[1], dp(40))
                text_size: self.width, None
                halign: "left"
                valign: "top"
                color: 0.2, 0.83, 0.6, 1
"""


class SplashScreen(Screen):
    pass


class EditorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: setattr(self.ids.code, "text", DEFAULT_CODE))

    def run_code(self):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                exec(compile(self.ids.code.text, "<editor>", "exec"), {"__name__": "__main__"})
        except Exception:
            buf.write(traceback.format_exc())
        self.ids.out.text = buf.getvalue() or "(no output)"


class PyKivyApp(App):
    title = "PyKivy"

    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager(transition=FadeTransition(duration=0.4))
        sm.add_widget(SplashScreen())
        sm.add_widget(EditorScreen())
        Clock.schedule_once(lambda dt: setattr(sm, "current", "editor"), 3)
        return sm


if __name__ == "__main__":
    PyKivyApp().run()
