import pyttsx3 as pc
from win32api import GetSystemMetrics, SetCursorPos
from PIL import ImageGrab
import time
import os
import sys
import numpy as np
import cv2
import math
import random
import ctypes


def capture_screen():
    # Get screen dimensions
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)

    # Capture a portion of the screen
    screen = ImageGrab.grab(bbox=(0, 0, screen_width // 2, screen_height // 2))
    return np.array(screen)


def process_image(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a simple threshold
    _, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    return threshold_image


def move_cursor():
    # Move the cursor to a random position
    rand_x = random.randint(0, GetSystemMetrics(0) // 2)
    rand_y = random.randint(0, GetSystemMetrics(1) // 2)
    SetCursorPos((rand_x, rand_y))


def main():
    while True:
        # Capture screen
        screen = capture_screen()

        # Process the captured image
        processed_image = process_image(screen)

        # Move the cursor to a random position
        move_cursor()

        # Pause for a short duration
        time.sleep(2)


if __name__ == "__main__":
    main()
