from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = GridLayout(cols=4, spacing=2)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)

        equals_button = Button(text='=')
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        clear_button = Button(text='Clear')
        clear_button.bind(on_press=self.clear)
        layout.add_widget(clear_button)

        layout.add_widget(self.result)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            new_text = current + button_text
            self.result.text = new_text

    def clear(self, instance):
        self.result.text = ''

    def on_solution(self, instance):
        text = self.result.text
        try:
            # Используем функцию eval() для вычисления выражения
            solution = str(eval(self.result.text))
            self.result.text = solution
        except Exception:
            self.result.text = 'Ошибка'

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
