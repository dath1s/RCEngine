from lib.RCEngine.BasicClasses.Entity import Entity
from lib.RCEngine.BasicClasses.EntityList import EntityList
from lib.RCEngine.BasicClasses.Game import Game
from lib.RCEngine.BasicClasses.Ray import Ray
import keyboard


if __name__ == '__main__':
    def on_press(key):
        print(key.name)

    def esc_press():
        exit()

    keyboard.add_hotkey('esc', esc_press)
    keyboard.on_press(on_press)
    while True:
        pass