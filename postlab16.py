from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CounterApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=20, spacing=20)

        self.display = TextInput(text="0", font_size=40, multiline=False)
        increment_btn = Button(text="Increment", font_size=30, on_press=self.increment)

        layout.add_widget(self.display)
        layout.add_widget(increment_btn)

        return layout

    def increment(self, instance):
        current = int(self.display.text)
        current += 1
        self.display.text = str(current)

CounterApp().run()


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TextInputApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=20, spacing=20)

        self.input_box = TextInput(hint_text="Type something...", font_size=20)
        btn = Button(text="Show Text", font_size=25, on_press=self.show_text)
        self.output_box = TextInput(text="", font_size=25, multiline=False)

        layout.add_widget(self.input_box)
        layout.add_widget(btn)
        layout.add_widget(self.output_box)

        return layout

    def show_text(self, instance):
        self.output_box.text = self.input_box.text

TextInputApp().run()
