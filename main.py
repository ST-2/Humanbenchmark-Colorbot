import pyautogui
from colorama import Fore, Style
import keyboard
import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')
clear_screen()
print("\n\nRunning! Use on https//https://humanbenchmark.com/tests/reactiontime \n\n -Astaria")
pyautogui.sleep(5)
clear_screen()

def print_colored(text, color):
    colored_text = f"{color}{text}{Style.RESET_ALL}"
    print(colored_text)

def calculate_brightness(rgb):
    r, g, b = rgb
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    return brightness

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Flag to keep track of the previous color
prev_color = None

# Continuously sample the color
while True:
    # Get the current mouse cursor position
    x, y = pyautogui.position()

    # Check if the cursor is within the screen boundaries
    if 0 <= x < screen_width and 0 <= y < screen_height:
        # Capture the screen color at the cursor position
        pixel = pyautogui.pixel(x, y)

        # Extract the RGB values from the pixel color
        rgb = (pixel[0], pixel[1], pixel[2])

        # Determine the color name based on the RGB values
        color_name = ""
        brightness = calculate_brightness(rgb)
        if brightness < 128:
            text_color = Fore.WHITE
        else:
            text_color = Fore.BLACK

        color_code = f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text_color}"

        # Print the RGB values of the color at the cursor position with color styling
        print_colored(f"RGB: {rgb}    ", color_code)
        print_colored(f"Color: {color_name}", color_code)

        if rgb == (43, 135, 209):
            color_name = "Blue"
            if prev_color != color_name:
                pyautogui.sleep(1)
                pyautogui.click(button='left')
                prev_color = color_name
        elif rgb == (75, 219, 106):
            color_name = "Green"
            if prev_color != color_name:
                pyautogui.click(button='left')
                prev_color = color_name
        else:
            prev_color = None

    # Check if the 'q' key is pressed to stop the program
    if keyboard.is_pressed('q'):
        break