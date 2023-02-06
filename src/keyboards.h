// Copyright 2023 Manna Harbour
// https://github.com/manna-harbour/miryoku

#pragma once

#if defined (KMK_KEYBOARD_ATREUS62)
  #include "mapping/62/atreus62.h"
#elif defined (KMK_KEYBOARD_BOARDSOURCE_4X12)
  #include "mapping/48/planck.h"
#elif defined (KMK_KEYBOARD_BOARDSOURCE_5X12)
  #include "mapping/60/preonic.h"
#elif defined (KMK_KEYBOARD_BOARDSOURCE_LULU)
  #include "mapping/62/lulu.h"
#elif defined (KMK_KEYBOARD_BOARDSOURCE_MICRODOX)
  #include "mapping/36/minidox.h"
#elif defined (KMK_KEYBOARD_CRKBD)
  #include "mapping/42/crkbd.h"
#elif defined (KMK_KEYBOARD_CROWBOARD)
  #include "mapping/40/ortho_4x10.h"
#elif defined (KMK_KEYBOARD_ERGO_TRAVEL)
  #include "mapping/52/ergo_travel.h"
#elif defined (KMK_KEYBOARD_FFKB)
  #include "mapping/45/ffkb.h"
#elif defined (KMK_KEYBOARD_HELIX)
  #include "mapping/64/helix.h"
#elif defined (KMK_KEYBOARD_KEEBIO_IRIS)
  #include "mapping/56/iris.h"
#elif defined (KMK_KEYBOARD_KEEBIO_LEVINSON)
  #include "mapping/48/lets_split.h"
#elif defined (KMK_KEYBOARD_KEEBIO_NYQUIST)
  #include "mapping/60/preonic.h"
#elif defined (KMK_KEYBOARD_KLOR)
  #include "mapping/44/klor.h"
#elif defined (KMK_KEYBOARD_KYRIA)
  #include "mapping/50/kyria.h"
#elif defined (KMK_KEYBOARD_LILY58)
  #include "mapping/58/lily58.h"
#elif defined (KMK_KEYBOARD_LUNAKEY_PICO)
  #include "mapping/44/pico.h"
#elif defined (KMK_KEYBOARD_RHYMESTONE)
  #include "mapping/40/ortho_4x10.h"
#elif defined (KMK_KEYBOARD_SOFLE)
  #include "mapping/60/sofle.h"
#elif defined (KMK_KEYBOARD_SPLAYTORAID)
  #include "mapping/41/splaytoraid.h"
#else
  #include "mapping/36/minidox.h"
#endif
