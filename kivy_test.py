from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class MyWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyWidget()
        btn = Button(text="Clear")
        btn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(btn)
        return parent

    def clear_canvas(self):
        self.painter.canvas.clear()


if __name__ == "__main__":
    MyApp().run()
