from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class BasicCalculatorApp(App):
    # ToDo: Create __init__

    def build(self):

        # List of operators
        self.operators = ["/", "*", "+", "-"]

        # Indicates if last pressed button was operator
        self.last_was_operator = None

        # Last pressed button
        self.last_button = None

        # Top Level main_layout
        main_layout = BoxLayout(orientation="vertical")

        # Text Input settings
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=60
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

    # Takes instance argument so it can access which widget called this method
    def on_button_press(self, instance):

        # Stores value of solution.text in current
        current = self.solution.text

        # Stores value of instance.text in button_text
        button_text = instance.text

        # Checks which button was pressed
        if button_text == "C":
            # Clears solution widget if C is pressed
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Avoids adding two operators beside each other
                return
            elif current == "" and button_text in self.operators:
                # Avoids adding operator as first character
                return
            else:
                # If none of the previous conditions are met, updates solution with the button press
                new_text = current + button_text
                self.solution.text = new_text

        # Sets the last button pressed
        self.last_button = button_text

        # Sets value to True or False depending on whether the last button is an operator
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            # Todo: Change self.solution.text to text if works
            solution = str(eval(self.solution.text))
            self.solution.text = solution


"""
Initializes main and starts app
"""
app = BasicCalculatorApp()
app.run()