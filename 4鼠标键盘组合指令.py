import csv
import pyautogui
import time

# 模拟鼠标点击
def simulate_mouse_click(x, y, button='left', clicks=1):
    if button == 'left':
        pyautogui.click(x, y, clicks=clicks)
    elif button == 'right':
        pyautogui.click(x, y, button='right', clicks=clicks)

# 模拟输入
def simulate_typing(text):
    pyautogui.typewrite(text)

# 模拟组合键
def simulate_key_combination(key):
    pyautogui.hotkey('ctrl', key)

# 等待一段时间
def wait(seconds):
    time.sleep(seconds/1000)

# 读取指令并执行
with open('4commands.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        command = row[0]
        if command == 'mouse':
            x, y = map(int, row[1:3])
            print(f"鼠标点击{x},{y}")
            if len(row) > 3:
                button = row[3]
                clicks = int(row[4]) if len(row) > 4 else 1
                simulate_mouse_click(x, y, button, clicks)
            else:
                simulate_mouse_click(x, y)
        elif command == 'wait':
            wait_time = int(row[1])
            print(f"等待{wait_time/1000}秒")
            wait(wait_time)
        elif command == 'text':
            text_to_type = row[1]
            print(f"输入文本{text_to_type}")
            simulate_typing(text_to_type)
        elif command == 'key':
            key = row[1]
            print(f"组合键 Ctrl + {key}")
            simulate_key_combination(key)
