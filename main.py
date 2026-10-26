from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import Scrollview
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import PushMatrix, PopMatrix, Color, Rotate, Ellipse, Rectangle
from kivy.uix.dropdown import DropDown

class SpinnerWidget(Widget):
    def __init__(self, **kwargs):
        super(CartoonSpinnerWidget, self).__init__(**kwargs)
        
        with self.canvas:
            cx, cy = 200, 200
            radius = 50
            
            Color(0.1, 0.1, 0.1, 1)
            Ellipse(pos=(cx - radius, cy - radius), size=(radius * 2, radius * 2))
            
            PushMatrix()
            self.rot = Rotate(angle=0, origin=(cx, cy))
            
            color_accent = (0.0, 0.4, 0.8, 1)
            color_contrast = (0.9, 0.9, 0.9, 1)
            
            Color(*color_accent)
            Rectangle(pos=(cx - radius + 5, cy), size=(radius - 5, radius - 5))
            Rectangle(pos=(cx, cy - radius + 5), size=(radius - 5, radius - 5))
            
            Color(*color_contrast)
            Rectangle(pos=(cx, cy), size=(radius - 5, radius - 5))
            Rectangle(pos=(cx - radius + 5, cy - radius + 5), size=(radius - 5, radius - 5))
            
            PopMatrix()
            
            PushMatrix()
            self.blur_rot = Rotate(angle=0, origin=(cx, cy))
            blur_alpha = 0.4
            
            Color(0.0, 0.4, 0.8, blur_alpha)
            Rectangle(pos=(cx - radius + 5, cy), size=(radius - 5, radius - 5))
            Rectangle(pos=(cx, cy - radius + 5), size=(radius - 5, radius - 5))
            
            Color(0.9, 0.9, 0.9, blur_alpha)
            Rectangle(pos=(cx, cy), size=(radius - 5, radius - 5))
            Rectangle(pos=(cx - radius + 5, cy - radius + 5), size=(radius - 5, radius - 5))
            
            PopMatrix()
