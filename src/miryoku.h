// Copyright 2022 Manna Harbour
// https://github.com/manna-harbour/miryoku

#pragma once

#include "custom_config.h"

#include "keyboards.h"

#include "miryoku_babel/miryoku_layer_selection.h"
#include "miryoku_babel/miryoku_layer_list.h"

#define U_MACRO_VA_ARGS(MACRO, ...) MACRO(__VA_ARGS__)
#define U_MACRO_EXPAND(...) __VA_ARGS__
#define U_STRINGIFY(x) #x

#define U_NP KC.NO // key is not present
#define U_NA KC.NO // present but not available for use
#define U_NU KC.NO // available but not used

#define U_TAPPING_TERM 200

#define U_MT(TAP, HOLD) KC.MT(TAP, HOLD, prefer_hold=False, tap_interrupted=True, tap_time=U_TAPPING_TERM)
#define U_LT(HOLD, TAP) KC.LT(HOLD, TAP, prefer_hold=True, tap_interrupted=False, tap_time=U_TAPPING_TERM)
#define U_DF(LAYER) KC.TD(KC.NO, KC.DF(LAYER), tap_time=U_TAPPING_TERM)

#define U_CW KC.TD(KC.CW, KC.CAPS, tap_time=U_TAPPING_TERM)
#define U_BOOT KC.TD(KC.NO, KC.RELOAD, tap_time=U_TAPPING_TERM)

#if !defined (KMK_KCP)
  #define KMK_KCP
#endif

#if defined (MIRYOKU_CLIPBOARD_FUN)
  #define U_RDO KC.NO
  #define U_PST KC.NO
  #define U_CPY KC.NO
  #define U_CUT KC.NO
  #define U_UND KC.NO
#elif defined (MIRYOKU_CLIPBOARD_MAC)
  #define U_RDO KC.LSFT(KC.LGUI(KC.Z))
  #define U_PST KC.LGUI(KC.V)
  #define U_CPY KC.LGUI(KC.C)
  #define U_CUT KC.LGUI(KC.X)
  #define U_UND KC.LGUI(KC.Z)
#elif defined (MIRYOKU_CLIPBOARD_WIN)
  #define U_RDO KC.LCTL(KC.Y)
  #define U_PST KC.LCTL(KC.V)
  #define U_CPY KC.LCTL(KC.C)
  #define U_CUT KC.LCTL(KC.X)
  #define U_UND KC.LCTL(KC.Z)
#else
  #define U_RDO KC.NO
  #define U_PST KC.LSFT(KC.INS)
  #define U_CPY KC.LCTL(KC.INS)
  #define U_CUT KC.LSFT(KC.DEL)
  #define U_UND KC.NO
#endif

#if defined (KMK_RGB_RGB)
  #define U_RGB_HUD KC.RGB_HUD
  #define U_RGB_HUI KC.RGB_HUI
  #define U_RGB_MOD KC.NO
  #define U_RGB_RMOD KC.NO
  #define U_RGB_OFF KC.NO
  #define U_RGB_SAD KC.RGB_SAD
  #define U_RGB_SAI KC.RGB_SAI
  #define U_RGB_TOG KC.RGB_TOG
  #define U_RGB_VAD KC.RGB_VAD
  #define U_RGB_VAI KC.RGB_VAI
#elif defined (KMK_RGB_PEG)
  #define U_RGB_HUD KC.NO
  #define U_RGB_HUI KC.NO
  #define U_RGB_MOD KC.NO
  #define U_RGB_RMOD KC.NO
  #define U_RGB_OFF KC.NO
  #define U_RGB_SAD KC.NO
  #define U_RGB_SAI KC.NO
  #define U_RGB_TOG KC.RGB_TOG
  #define U_RGB_VAD KC.RGB_BRD
  #define U_RGB_VAI KC.RGB_BRI
#elif defined (KMK_RGB_LED)
  #define U_RGB_HUD KC.NO
  #define U_RGB_HUI KC.NO
  #define U_RGB_MOD KC.NO
  #define U_RGB_RMOD KC.NO
  #define U_RGB_OFF KC.NO
  #define U_RGB_SAD KC.NO
  #define U_RGB_SAI KC.NO
  #define U_RGB_TOG KC.LED_TOG()
  #define U_RGB_VAD KC.LED_DEC()
  #define U_RGB_VAI KC.LED_INC()
#else
  #define U_RGB_HUD KC.NO
  #define U_RGB_HUI KC.NO
  #define U_RGB_MOD KC.NO
  #define U_RGB_RMOD KC.NO
  #define U_RGB_OFF KC.NO
  #define U_RGB_SAD KC.NO
  #define U_RGB_SAI KC.NO
  #define U_RGB_TOG KC.NO
  #define U_RGB_VAD KC.NO
  #define U_RGB_VAI KC.NO
#endif
