import random
import string
import pyperclip
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class PasswordGeneratorApp(App):
    def generate_password(self, length):
        random_password = '@'
        random_password += ''.join(random.choice(string.ascii_uppercase))
        password_length = length
        random_password += ''.join(random.choices(string.ascii_lowercase + string.digits, k=password_length))
        return random_password

    def copy_to_clipboard(self, password):
        pyperclip.copy(password)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        length_label = Label(text='Enter password length:')
        layout.add_widget(length_label)

        self.length_input = TextInput(multiline=False)
        layout.add_widget(self.length_input)

        generate_button = Button(text='Generate Password')
        generate_button.bind(on_press=self.on_generate)
        layout.add_widget(generate_button)

        self.password_label = Label(text='')
        layout.add_widget(self.password_label)

        return layout

    def on_generate(self, instance):
        length = int(self.length_input.text)
        password = self.generate_password(length)
        self.password_label.text = password
        self.copy_to_clipboard(password)


if __name__ == '__main__':
    PasswordGeneratorApp().run()
