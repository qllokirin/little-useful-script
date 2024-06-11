import pyautogui
import time
import json


# 读取JSON文件中的经纬度信息
def read_coordinates_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["coordinates"]


# 模拟键盘操作函数
def simulate_keyboard_input(coordinates):
    for coordinate in coordinates:
        pyautogui.click()
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyUp('ctrl')
        pyautogui.typewrite(f'{coordinate["longitude"]},{coordinate["latitude"]}', interval=0.01)
        pyautogui.press('enter')
        pyautogui.click()
        time.sleep(4)


if __name__ == "__main__":

    time.sleep(2)
    print("Running...")

    # JSON文件路径
    json_file_path = '3跑步打卡.json'

    count = 0

    while count < 7:
        # 读取经纬度信息
        coordinates = read_coordinates_from_json(json_file_path)

        # 模拟键盘操作
        simulate_keyboard_input(coordinates)

        count += 1

        print(f"{count+1} laps")
