# Copyright 2022 Manna Harbour
# https://github.com/manna-harbour/miryoku


# create macro with value appended

ifneq ($(strip $(MIRYOKU_ALPHAS)),)
  OPT_DEFS += -DMIRYOKU_ALPHAS_$(MIRYOKU_ALPHAS)
endif

ifneq ($(strip $(MIRYOKU_EXTRA)),)
  OPT_DEFS += -DMIRYOKU_EXTRA_$(MIRYOKU_EXTRA)
endif

ifneq ($(strip $(MIRYOKU_TAP)),)
  OPT_DEFS += -DMIRYOKU_TAP_$(MIRYOKU_TAP)
endif

ifneq ($(strip $(MIRYOKU_NAV)),)
  OPT_DEFS += -DMIRYOKU_NAV_$(MIRYOKU_NAV)
endif

ifneq ($(strip $(MIRYOKU_CLIPBOARD)),)
  OPT_DEFS += -DMIRYOKU_CLIPBOARD_$(MIRYOKU_CLIPBOARD)
endif

ifneq ($(strip $(MIRYOKU_LAYERS)),)
  OPT_DEFS += -DMIRYOKU_LAYERS_$(MIRYOKU_LAYERS)
endif

ifneq ($(strip $(MIRYOKU_MAPPING)),)
  OPT_DEFS += -DMIRYOKU_MAPPING_$(MIRYOKU_MAPPING)
endif

ifneq ($(strip $(KMK_KEYBOARD)),)
  OPT_DEFS += -DKMK_KEYBOARD_$(KMK_KEYBOARD)
endif

ifneq ($(strip $(KMK_RGB)),)
  OPT_DEFS += -DKMK_RGB_$(KMK_RGB)
endif


# create macro with value

ifneq ($(strip $(KMK_KCP)),)
  OPT_DEFS += -DKMK_KCP=$(KMK_KCP)
endif

