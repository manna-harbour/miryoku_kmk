# Copyright 2022 Manna Harbour
# github.com/manna-harbour/miryoku
# generated
       
       
       
       
       
from kb import KMKKeyboard; keyboard = KMKKeyboard()
from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())


keyboard.keymap = [
# BASE
[
KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT,
KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.R, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.T, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.M, KC.MT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.E, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.I, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),
KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200)
],
# EXTRA
[
KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.H, KC.MT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),
KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),
KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200)
],
# TAP
[
KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT,
KC.A, KC.R, KC.S, KC.T, KC.G, KC.M, KC.N, KC.E, KC.I, KC.O,
KC.Z, KC.X, KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.DOT, KC.SLSH,
KC.ESC, KC.SPC, KC.TAB, KC.ENT, KC.BSPC, KC.DEL
],
# BUTTON
[
KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INS), KC.LSFT(KC.INS), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INS), KC.LSFT(KC.INS), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO,
KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB
],
# NAV
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.TD(KC.CW, KC.CAPS, tap_time=200), KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.NO, KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL
],
# MOUSE
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT,
KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.NO, KC.NO, KC.NO, KC.MW_DN, KC.MW_UP, KC.NO,
KC.NO, KC.NO, KC.NO, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB
],
# MEDIA
[
KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.PS_TOG, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT,
KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.NO, KC.HID, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.MSTP, KC.MPLY, KC.MUTE
],
# NUM
[
KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.RALT, KC.NO,
KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO
],
# SYM
[
KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, KC.NO, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.RALT, KC.NO,
KC.LPRN, KC.RPRN, KC.UNDS, KC.NO, KC.NO, KC.NO
],
# FUN
[
KC.F12, KC.F7, KC.F8, KC.F9, KC.PSCR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
KC.F11, KC.F4, KC.F5, KC.F6, KC.SLCK, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
KC.F10, KC.F1, KC.F2, KC.F3, KC.PAUS, KC.NO, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.RALT, KC.NO,
KC.APP, KC.SPC, KC.TAB, KC.NO, KC.NO, KC.NO
],

]

layer_names_list = [
"Base", "Extra", "Tap", "Button", "Nav", "Mouse", "Media", "Num", "Sym", "Fun",
]

if __name__ == '__main__':
     print('starting Miryoku KMK')
     keyboard.go()
