print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP6,
                board.GP7,
                board.GP8,
                board.GP9,
                board.GP10,
                board.GP11,
                board.GP12,
                board.GP13,
                board.GP14,
                board.GP15,
                board.GP16,
                board.GP17,
                board.GP18,
                board.GP19,
                board.GP20,
                board.GP21,
                board.GP22,
                board.GP26)
keyboard.row_pins = (board.GP0,
                board.GP1,
                board.GP2,
                board.GP3,
                board.GP4,
                board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

CHANGE = KC.NO

keyboard.keymap = [
    [KC.ESC, KC.NO, KC.F1, KC.F2, KC.F3, KC.F4, KC.NO, KC.F5, KC.F6, KC.F7, CHANGE, KC.NO, CHANGE, CHANGE, KC.F11, CHANGE, KC.NO, KC.NO, 
     KC.TILDA, KC.N1, KC.N2, KC.N3, CHANGE, CHANGE, CHANGE, CHANGE, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQL, KC.BSPC, KC.NO, CHANGE, CHANGE, CHANGE, 
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.NO, CHANGE, CHANGE, CHANGE, 
     KC.CAPSLOCK, KC.NO, KC.A, CHANGE, CHANGE, CHANGE, CHANGE, CHANGE, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NO, KC.ENTER, KC.NO, KC.NO, KC.NO, 
     CHANGE, KC.NO, CHANGE, CHANGE, CHANGE, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.RSHIFT, KC.NO, KC.NO, CHANGE, KC.NO, 
     CHANGE, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, CHANGE, CHANGE, KC.A, KC.RCTRL, KC.NO, KC.LEFT, CHANGE, CHANGE, ]
]                                            
if __name__ == '__main__':
    keyboard.go()