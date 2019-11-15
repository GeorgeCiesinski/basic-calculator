from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):

        # List of operators
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # Top Level main_layout
        main_layout = BoxLayout(Orientation="Vertical")

        # Text Input settings
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=5
        )

        # Added TextInput to main_layout
        main_layout.add_widget(self.solution)

        # List of lists containing buttons of calculator
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]

        # Loop creates button widgets
        for row in buttons:
            # Creates horizontal BoxLayout
            h_layout = BoxLayout()
            # Creates individual buttons
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                # Binds buttons to on_button_press event handler
                button.bind(on_press=self.on_button_press)
                # Adds individual buttons to horizontal BoxLayout
                h_layout.add_widget(button)
            # Adds h_layout to main_layout
            main_layout.add_widget(h_layout)

        # Creates equals button
        equals_button = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        # Binds button to on_solution event handler
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout
