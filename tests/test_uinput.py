import unittest

import uinput

MOUSE_KEYS = [uinput.REL_X, uinput.REL_Y, uinput.BTN_LEFT, uinput.BTN_RIGHT]

class DeviceTest(unittest.TestCase):
    def test_device_empty(self):
        with uinput.Device([]) as device:
            pass

    def test_keyboard_click(self):
        test_key = uinput.KEY_LEFTCTRL
        with uinput.Device([test_key]) as device:
            device.emit_click(test_key)

    def test_mouse_move(self):
        with uinput.Device(MOUSE_KEYS) as device:
            device.emit(uinput.REL_X, 1)


if __name__ == "__main__":
    unittest.main()
