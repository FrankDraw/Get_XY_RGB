# 根据鼠标移动，动态输出当前坐标和该坐标对应的RGB值；

from win32api import GetCursorPos, SetConsoleTitle, Sleep
from win32gui import GetDesktopWindow, GetWindowDC, GetPixel
from os import system


def get_xy_rgb():
    """ Print current cursor's position and RGB value."""
    SetConsoleTitle("Get_XY_RGB V3.0")
    system("MODE CON: COLS=51 LINES=16")
    system("COLOR 0A")

    print(" ***********************************************")
    print(" *     Get Cursor Position and RGB value.      *")
    print(" *                                             *")
    print(" *                 v3.0  Frank Draw 2024-03-14 *")
    print(" ***********************************************")
    print(" Please Move your mouse to target point.\n")

    desktop_window_id = GetDesktopWindow()
    desktop_window_dc = GetWindowDC(desktop_window_id)

    while True:
        try:
            # Get mouse position.
            mouse_pos = GetCursorPos()

            # Delay 500ms before get next position.
            Sleep(500)

            # Get mouse position again.
            new_mouse_pos = GetCursorPos()

            # If mouse moved, print position and RGB.
            if mouse_pos != new_mouse_pos:
                # Get mouse position.
                x, y = str(new_mouse_pos[0]).rjust(4), str(new_mouse_pos[1]).rjust(4)
                pos_info = "Position: ({}, {})".format(x, y).ljust(25)

                # Get RGB value.
                color = int(GetPixel(desktop_window_dc, new_mouse_pos[0], new_mouse_pos[1]))
                r, g, b = (color & 0xff), ((color >> 8) & 0xff), ((color >> 16) & 0xff)
                r, g, b = str(r).rjust(4), str(g).rjust(4), str(b).rjust(4)
                rgb = "RGB: ({},{},{})".format(r, g, b).ljust(20)

                # Output position and RGB information.
                print(" {} {}".format(pos_info, rgb))

        except KeyboardInterrupt as e:
            print("\nKeyboard Interrupt.")
            break


if __name__ == "__main__":
    get_xy_rgb()
