import os
import sys
import ctypes
from ctypes import wintypes
import threading
import time
import pystray
import pyperclip
from PIL import Image as PILImage  

# 获取路径
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# 图片映射
CHAR_IMG_MAP = {
    ' ': ' .png',
    '0': '0.png',
    '1': '1.png',
    '2': '2.png',
    '3': '3.png',
    '4': '4.png',
    '5': '5.png',
    '6': '6.png',
    '7': '7.png',
    '8': '8.png',
    '9': '9.png',
    'A': 'A.png',
    'B': 'B.png',
    'C': 'C.png',
    'D': 'D.png',
    'E': 'E.png',
    'F': 'F.png',
    '#': '#.png'
}

current_icons = []
is_first_click = True # 首次点击标记

user32 = ctypes.WinDLL("user32", use_last_error=True)
gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_mouse_pos():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def get_pixel_hex_reversed():
    x, y = get_mouse_pos()
    hdc = user32.GetDC(None)
    col = gdi32.GetPixel(hdc, x, y)
    user32.ReleaseDC(None, hdc)

    r = col & 0xFF
    g = (col >> 8) & 0xFF
    b = (col >> 16) & 0xFF

    hex_str = f"{r:02X}{g:02X}{b:02X}"
    pyperclip.copy("#" + hex_str)  
    return "#" + hex_str[::-1]  #反转

def load_char_icon(char):
    char = char.upper()
    img_name = CHAR_IMG_MAP.get(char)
    if not img_name:
        return PILImage.new("RGB", (256, 256), "#ffffff")
    
    img_path = get_resource_path(img_name)
    if not os.path.exists(img_path):
        return PILImage.new("RGB", (256, 256), "#ffffff")
    
    try:
        img = PILImage.open(img_path)
        img = img.resize((256, 256))
        return img
    except Exception as e:
        return PILImage.new("RGB", (256, 256), "#ffffff")

def clear_all_icons():
    global current_icons
    for icon in current_icons:
        try:
            icon.stop()
        except:
            pass
    current_icons = []

def show_hex_on_taskbar(hex_str):
    clear_all_icons()
    chars = list(hex_str)
    
    for idx, char in enumerate(chars):
        icon_img = load_char_icon(char)
        icon = pystray.Icon(
            name=f"color_icon_{idx:04d}",
            icon=icon_img,
            title=char
        )
        current_icons.append(icon)
        threading.Thread(target=icon.run, daemon=True).start()
        time.sleep(0.05)

def listen_middle_mouse():
    global is_first_click
    MIDDLE_MOUSE_KEY = 0x04  # 鼠标中键
    
    while True:
        if user32.GetAsyncKeyState(MIDDLE_MOUSE_KEY) & 0x8000:
                hex_color = get_pixel_hex_reversed()
                show_hex_on_taskbar(hex_color)
                while user32.GetAsyncKeyState(MIDDLE_MOUSE_KEY) & 0x8000:
                    time.sleep(0.1)
        if is_first_click:
            show_hex_on_taskbar("       ")
            is_first_click = False          
        time.sleep(0.01)

if __name__ == "__main__":
    threading.Thread(target=listen_middle_mouse, daemon=True).start()
    # 常驻运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clear_all_icons()