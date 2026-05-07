from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import sys
from io import StringIO
from matus_interpreter import MatusInterpreter

class MatusApp(App):
    def build(self):
        self.interpreter = MatusInterpreter()
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.output_label = Label(text="Matus Language Console\n", size_hint_y=None, halign='left', valign='top')
        self.output_label.bind(size=self.output_label.setter('text_size'))
        
        scroll = ScrollView(size_hint=(1, 0.7))
        scroll.add_widget(self.output_label)
        
        self.input_text = TextInput(multiline=False, size_hint_y=None, height=100, hint_text="Enter Matus code here...")
        
        run_btn = Button(text="Run Code", size_hint_y=None, height=100)
        run_btn.bind(on_press=self.run_code)
        
        layout.add_widget(scroll)
        layout.add_widget(self.input_text)
        layout.add_widget(run_btn)
        
        return layout

    def run_code(self, instance):
        code = self.input_text.text
        if not code:
            return
            
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        
        try:
            self.interpreter.execute(code)
            output = mystdout.getvalue()
        except Exception as e:
            output = f"Error: {str(e)}"
        finally:
            sys.stdout = old_stdout
            
        self.output_label.text += f"> {code}\n{output}\n"
        self.input_text.text = ""

if __name__ == '__main__':
    MatusApp().run()
