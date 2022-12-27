U_HASH Copyright 2022 Manna Harbour
U_HASH github.com/manna-harbour/miryoku
U_HASH generated

#include "miryoku.h"

from kb import KMKKeyboard; keyboard = KMKKeyboard(KMK_KCP)
from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord()) // must come after modtap

#if defined (KMK_RGB_RGB)
U_HASH from kmk.extensions.RGB import RGB; keyboard.extensions.append(RGB(pixel_pin=EDIT, num_pixels=EDIT))
#elif defined (KMK_RGB_PEG)
U_HASH from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color; keyboard.extensions.append(Rgb_matrix(EDIT))
#elif defined (KMK_RGB_LED)
U_HASH from kmk.extensions.LED import LED; keyboard.extensions.append(LED(EDIT))
#endif

U_LF

keyboard.keymap = [
#define MIRYOKU_X(LAYER, STRING) \
U_HASH LAYER U_LF \
[ U_LF \
U_MACRO_VA_ARGS(U_MACRO_EXPAND(MIRYOKU_LAYERMAPPING_##LAYER), MIRYOKU_LAYER_##LAYER)\
], U_LF
MIRYOKU_LAYER_LIST
#undef MIRYOKU_X
] U_LF

layer_names_list = [
#define MIRYOKU_X(LAYER, STRING) \
STRING,
MIRYOKU_LAYER_LIST
#undef MIRYOKU_X
] U_LF

if __name__ == '__main__':
     print('starting Miryoku KMK')
     keyboard.go()
