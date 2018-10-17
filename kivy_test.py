from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class MyWidget(Widget):

    def draw_circle(self):
        cl = Color(1, 0, 0, 1)
        cr = Ellipse(pos=(100, 100), size=(100, 100))
        self.canvas.add(cl)
        self.canvas.add(cr)


class MyApp(App):

    def build(self):
        w = MyWidget()
        w.draw_circle()
        return w


MyApp().run()
