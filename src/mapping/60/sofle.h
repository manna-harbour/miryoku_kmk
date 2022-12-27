// Copyright 2023 Manna Harbour
// https://github.com/manna-harbour/miryoku

#if !defined (MIRYOKU_LAYOUTMAPPING_SOFLE)

#define XXX KC.NO

#define MIRYOKU_LAYOUTMAPPING_SOFLE( \
     K00, K01, K02, K03, K04,                K05, K06, K07, K08, K09, \
     K10, K11, K12, K13, K14,                K15, K16, K17, K18, K19, \
     K20, K21, K22, K23, K24,                K25, K26, K27, K28, K29, \
     N30, N31, K32, K33, K34,                K35, K36, K37, N38, N39 \
) \
XXX, XXX, XXX, XXX, XXX, XXX,                XXX, XXX, XXX, XXX, XXX, XXX U_LF \
XXX, K00, K01, K02, K03, K04,                K05, K06, K07, K08, K09, XXX U_LF \
XXX, K10, K11, K12, K13, K14,                K15, K16, K17, K18, K19, XXX U_LF \
XXX, K20, K21, K22, K23, K24,                K25, K26, K27, K28, K29, XXX U_LF \
     XXX, XXX, K32, K33, K34, XXX,      XXX, K35, K36, K37, XXX, XXX U_LF

#define MIRYOKU_KLUDGE_THUMBCOMBOS_LEFT 53 54
#define MIRYOKU_KLUDGE_THUMBCOMBOS_RIGHT 55 56

#endif

#define MIRYOKU_MAPPING MIRYOKU_LAYOUTMAPPING_SOFLE
