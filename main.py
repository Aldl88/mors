from pynput.mouse import Button, Controller
import time
import tkinter as tk

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '!': '-.-.--', '@': '.--.-.'
}

# Function to convert text to morse code
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT[char] for char in text.upper() if char in MORSE_CODE_DICT)

# Function to click Morse code
import pyautogui
import time

def click_morse_code(morse_code, x, y):
    mouse = Controller()
    mouse.position = (x, y)

    for symbol in morse_code:
        if symbol is None:
            raise ValueError("Invalid symbol: {}".format(symbol))
        elif symbol == ' ':
            time.sleep(1.5)
        elif symbol == '.':
            time.sleep(0.25)
            mouse.click(Button.left)
            time.sleep(0.25)
        elif symbol == '-':
            mouse.press(Button.left)
            time.sleep(1)  # Longer delay for dash, adjust as necessary
            mouse.release(Button.left)
            

# Example usage
# click_morse_code(['.', '-', '.', '.', '-'], 100, 200)


# Function to handle the button click
def on_press(event, root, text):
    # Get the coordinates of the click
    x, y = event.x_root, event.y_root

    # Close the Tkinter window
    root.destroy()

    # Convert the text to Morse code
    morse_code = text_to_morse(text)

    print(morse_code)

    # Click the Morse code at the selected point
    click_morse_code(morse_code, x, y)

# Main function
def main():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Morse Code Typer")

    # Create an entry widget to enter the text
    entry = tk.Entry(root, width=50)
    entry.pack(pady=20)

    # Create a button to submit the text
    submit_button = tk.Button(root, text="Submit", command=lambda: get_point(root, entry.get()))
    submit_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

def get_point(root, text):
    # Close the Tkinter window
    root.destroy()

    # Create a new Tkinter window to capture the click
    point_window = tk.Tk()
    point_window.title("Select Point")

    # Instruction label
    label = tk.Label(point_window, text="Click anywhere on the screen to select the point.")
    label.pack(pady=20)

    # Bind the click event to the on_click function
    point_window.bind('<Key>', lambda event: on_press(event, point_window, text))

    

    # Start the Tkinter event loop
    point_window.mainloop()

if __name__ == "__main__":
    main()
