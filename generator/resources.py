import copy
from dataclasses import dataclass
import os
from typing import *


@dataclass
class Template:
    name: str
    template: str

    def save(self) -> None:
        self.template = self.template.replace("§NAME", self.name)

        with open(
            os.path.join(os.getcwd(), "out", f"{self.name}.zig"), "w", encoding="utf8"
        ) as wf:
            wf.write(self.template)


def get_template(name: str, use: Literal[0, 1, 2]) -> Template:
    text: list[str] = [TEMPLATE_MENUM, TEMPLATE_MSTRUCT, TEMPLATE_MLIST]

    return Template(name, copy.deepcopy(text[use]))


KEYWORDS: list[str] = [
    "NULL",
    "SOH",
    "STX",
    "ETX",
    "EOT",
    "ENQ",
    "ACK",
    "BEL",
    "BACKSPACE",
    "HORTIZONTAL_TAB",
    "LINE_FEED",
    "VERTICAL_TAB",
    "FROM_FEED",
    "ENTER",
    "SHIFT_OUT",
    "SHIFT_IN",
    "DLE",
    "DC1",
    "DC2",
    "DC3",
    "DC4",
    "NAK",
    "SYN",
    "ETB",
    "CANCEL",
    "EM",
    "SUB",
    "ESCAPE",
    "FS",
    "GS",
    "RS",
    "US",
    "SPACE",
    "EXCLAMATION_MARK",
    "DOUBLE_QUOTE",
    "HASHTAG",
    "DOLLARSIGN",
    "PERCENTAGE",
    "ANDSIGN",
    "SINGLE_QUOTE",
    "ROUND_BRACKET_START",
    "ROUND_BRACKET_END",
    "STAR_SIGN",
    "PLUS_SIGN",
    "COMA",
    "MINUS_SIGN",
    "DOT",
    "SLASH_SIGN",
    "NUMBER_0",
    "NUMBER_1",
    "NUMBER_2",
    "NUMBER_3",
    "NUMBER_4",
    "NUMBER_5",
    "NUMBER_6",
    "NUMBER_7",
    "NUMBER_8",
    "NUMBER_9",
    "COLON",
    "SEMI_COLON",
    "LARGER_SIGN",
    "EQUAL_SIGN",
    "SMALLER_SIGN",
    "QUESTION_MARK",
    "AT_SIGN",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "SQUARE_BRACKET_START",
    "BACKSLASH",
    "SQUARE_BRACKET_END",
    "CIRCUMFLEX",
    "UNDERSCORE",
    "GRAVE_ACCENT",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "CURLY_BRACKET_START",
    "VERTICAL_BAR",
    "CURLY_BRACKET_END",
    "SWUNG_DASH",
    "DELETE",
]

TEMPLATE_MENUM = """
pub const §NAME = enum(?u8) {
    NULL = $NULL,
    SOH = $SOH,
    STX = $STX,
    ETX = $ETX,
    EOT = $EOT,
    ENQ = $ENQ,
    ACK = $ACK,
    BEL = $BEL,
    BACKSPACE = $BACKSPACE,
    HORTIZONTAL_TAB = $HORTIZONTAL_TAB,
    LINE_FEED = $LINE_FEED,
    VERTICAL_TAB = $VERTICAL_TAB,
    FROM_FEED = $FROM_FEED,
    ENTER = $ENTER,
    SHIFT_OUT = $SHIFT_OUT,
    SHIFT_IN = $SHIFT_IN,
    DLE = $DLE,
    DC1 = $DC1,
    DC2 = $DC2,
    DC3 = $DC3,
    DC4 = $DC4,
    NAK = $NAK,
    SYN = $SYN,
    ETB = $ETB,
    CANCEL = $CANCEL,
    EM = $EM,
    SUB = $SUB,
    ESCAPE = $ESCAPE,
    FS = $FS,
    GS = $GS,
    RS = $RS,
    US = $US,
    SPACE = $SPACE,
    EXCLAMATION_MARK = $EXCLAMATION_MARK,
    DOUBLE_QUOTE = $DOUBLE_QUOTE,
    HASHTAG = $HASHTAG,
    DOLLARSIGN = $DOLLARSIGN,
    PERCENTAGE = $PERCENTAGE,
    ANDSIGN = $ANDSIGN,
    SINGLE_QUOTE = $SINGLE_QUOTE,
    ROUND_BRACKET_START = $ROUND_BRACKET_START,
    ROUND_BRACKET_END = $ROUND_BRACKET_END,
    STAR_SIGN = $STAR_SIGN,
    PLUS_SIGN = $PLUS_SIGN,
    COMA = $COMA,
    MINUS_SIGN = $MINUS_SIGN,
    DOT = $DOT,
    SLASH_SIGN = $SLASH_SIGN,
    NUMBER_0 = $NUMBER_0,
    NUMBER_1 = $NUMBER_1,
    NUMBER_2 = $NUMBER_2,
    NUMBER_3 = $NUMBER_3,
    NUMBER_4 = $NUMBER_4,
    NUMBER_5 = $NUMBER_5,
    NUMBER_6 = $NUMBER_6,
    NUMBER_7 = $NUMBER_7,
    NUMBER_8 = $NUMBER_8,
    NUMBER_9 = $NUMBER_9,
    COLON = $COLON,
    SEMI_COLON = $SEMI_COLON,
    LARGER_SIGN = $LARGER_SIGN,
    EQUAL_SIGN = $EQUAL_SIGN,
    SMALLER_SIGN = $SMALLER_SIGN,
    QUESTION_MARK = $QUESTION_MARK,
    AT_SIGN = $AT_SIGN,
    A = $A,
    B = $B,
    C = $C,
    D = $D,
    E = $E,
    F = $F,
    G = $G,
    H = $H,
    I = $I,
    J = $J,
    K = $K,
    L = $L,
    M = $M,
    N = $N,
    O = $O,
    P = $P,
    Q = $Q,
    R = $R,
    S = $S,
    T = $T,
    U = $U,
    V = $V,
    W = $W,
    X = $X,
    Y = $Y,
    Z = $Z,
    SQUARE_BRACKET_START = $SQUARE_BRACKET_START,
    BACKSLASH = $BACKSLASH,
    SQUARE_BRACKET_END = $SQUARE_BRACKET_END,
    CIRCUMFLEX = $CIRCUMFLEX,
    UNDERSCORE = $UNDERSCORE,
    GRAVE_ACCENT = $GRAVE_ACCENT,
    a = $a,
    b = $b,
    c = $c,
    d = $d,
    e = $e,
    f = $f,
    g = $g,
    h = $h,
    i = $i,
    j = $j,
    k = $k,
    l = $l,
    m = $m,
    n = $n,
    o = $o,
    p = $p,
    q = $q,
    r = $r,
    s = $s,
    t = $t,
    u = $u,
    v = $v,
    w = $w,
    x = $x,
    y = $y,
    z = $z,
    CURLY_BRACKET_START = $CURLY_BRACKET_START,
    VERTICAL_BAR = $VERTICAL_BAR,
    CURLY_BRACKET_END = $CURLY_BRACKET_END,
    SWUNG_DASH = $SWUNG_DASH,
    DELETE = $DELETE,
};
"""

TEMPLATE_MSTRUCT = """

pub const KeyCodes = struct {
    NULL: ?u8 = null,
    SOH: ?u8 = null,
    STX: ?u8 = null,
    ETX: ?u8 = null,
    EOT: ?u8 = null,
    ENQ: ?u8 = null,
    ACK: ?u8 = null,
    BEL: ?u8 = null,
    BACKSPACE: ?u8 = null,
    HORTIZONTAL_TAB: ?u8 = null,
    LINE_FEED: ?u8 = null,
    VERTICAL_TAB: ?u8 = null,
    FROM_FEED: ?u8 = null,
    ENTER: ?u8 = null,
    SHIFT_OUT: ?u8 = null,
    SHIFT_IN: ?u8 = null,
    DLE: ?u8 = null,
    DC1: ?u8 = null,
    DC2: ?u8 = null,
    DC3: ?u8 = null,
    DC4: ?u8 = null,
    NAK: ?u8 = null,
    SYN: ?u8 = null,
    ETB: ?u8 = null,
    CANCEL: ?u8 = null,
    EM: ?u8 = null,
    SUB: ?u8 = null,
    ESCAPE: ?u8 = null,
    FS: ?u8 = null,
    GS: ?u8 = null,
    RS: ?u8 = null,
    US: ?u8 = null,
    SPACE: ?u8 = null,
    EXCLAMATION_MARK: ?u8 = null,
    DOUBLE_QUOTE: ?u8 = null,
    HASHTAG: ?u8 = null,
    DOLLARSIGN: ?u8 = null,
    PERCENTAGE: ?u8 = null,
    ANDSIGN: ?u8 = null,
    SINGLE_QUOTE: ?u8 = null,
    ROUND_BRACKET_START: ?u8 = null,
    ROUND_BRACKET_END: ?u8 = null,
    STAR_SIGN: ?u8 = null,
    PLUS_SIGN: ?u8 = null,
    COMA: ?u8 = null,
    MINUS_SIGN: ?u8 = null,
    DOT: ?u8 = null,
    SLASH_SIGN: ?u8 = null,
    NUMBER_0: ?u8 = null,
    NUMBER_1: ?u8 = null,
    NUMBER_2: ?u8 = null,
    NUMBER_3: ?u8 = null,
    NUMBER_4: ?u8 = null,
    NUMBER_5: ?u8 = null,
    NUMBER_6: ?u8 = null,
    NUMBER_7: ?u8 = null,
    NUMBER_8: ?u8 = null,
    NUMBER_9: ?u8 = null,
    COLON: ?u8 = null,
    SEMI_COLON: ?u8 = null,
    LARGER_SIGN: ?u8 = null,
    EQUAL_SIGN: ?u8 = null,
    SMALLER_SIGN: ?u8 = null,
    QUESTION_MARK: ?u8 = null,
    AT_SIGN: ?u8 = null,
    A: ?u8 = null,
    B: ?u8 = null,
    C: ?u8 = null,
    D: ?u8 = null,
    E: ?u8 = null,
    F: ?u8 = null,
    G: ?u8 = null,
    H: ?u8 = null,
    I: ?u8 = null,
    J: ?u8 = null,
    K: ?u8 = null,
    L: ?u8 = null,
    M: ?u8 = null,
    N: ?u8 = null,
    O: ?u8 = null,
    P: ?u8 = null,
    Q: ?u8 = null,
    R: ?u8 = null,
    S: ?u8 = null,
    T: ?u8 = null,
    U: ?u8 = null,
    V: ?u8 = null,
    W: ?u8 = null,
    X: ?u8 = null,
    Y: ?u8 = null,
    Z: ?u8 = null,
    SQUARE_BRACKET_START: ?u8 = null,
    BACKSLASH: ?u8 = null,
    SQUARE_BRACKET_END: ?u8 = null,
    CIRCUMFLEX: ?u8 = null,
    UNDERSCORE: ?u8 = null,
    GRAVE_ACCENT: ?u8 = null,
    a: ?u8 = null,
    b: ?u8 = null,
    c: ?u8 = null,
    d: ?u8 = null,
    e: ?u8 = null,
    f: ?u8 = null,
    g: ?u8 = null,
    h: ?u8 = null,
    i: ?u8 = null,
    j: ?u8 = null,
    k: ?u8 = null,
    l: ?u8 = null,
    m: ?u8 = null,
    n: ?u8 = null,
    o: ?u8 = null,
    p: ?u8 = null,
    q: ?u8 = null,
    r: ?u8 = null,
    s: ?u8 = null,
    t: ?u8 = null,
    u: ?u8 = null,
    v: ?u8 = null,
    w: ?u8 = null,
    x: ?u8 = null,
    y: ?u8 = null,
    z: ?u8 = null,
    CURLY_BRACKET_START: ?u8 = null,
    VERTICAL_BAR: ?u8 = null,
    CURLY_BRACKET_END: ?u8 = null,
    SWUNG_DASH: ?u8 = null,
    DELETE: ?u8 = null,
};

pub const §NAME: KeyCodes = .{
    .NULL = $NULL,
    .SOH = $SOH,
    .STX = $STX,
    .ETX = $ETX,
    .EOT = $EOT,
    .ENQ = $ENQ,
    .ACK = $ACK,
    .BEL = $BEL,
    .BACKSPACE = $BACKSPACE,
    .HORTIZONTAL_TAB = $HORTIZONTAL_TAB,
    .LINE_FEED = $LINE_FEED,
    .VERTICAL_TAB = $VERTICAL_TAB,
    .FROM_FEED = $FROM_FEED,
    .ENTER = $ENTER,
    .SHIFT_OUT = $SHIFT_OUT,
    .SHIFT_IN = $SHIFT_IN,
    .DLE = $DLE,
    .DC1 = $DC1,
    .DC2 = $DC2,
    .DC3 = $DC3,
    .DC4 = $DC4,
    .NAK = $NAK,
    .SYN = $SYN,
    .ETB = $ETB,
    .CANCEL = $CANCEL,
    .EM = $EM,
    .SUB = $SUB,
    .ESCAPE = $ESCAPE,
    .FS = $FS,
    .GS = $GS,
    .RS = $RS,
    .US = $US,
    .SPACE = $SPACE,
    .EXCLAMATION_MARK = $EXCLAMATION_MARK,
    .DOUBLE_QUOTE = $DOUBLE_QUOTE,
    .HASHTAG = $HASHTAG,
    .DOLLARSIGN = $DOLLARSIGN,
    .PERCENTAGE = $PERCENTAGE,
    .ANDSIGN = $ANDSIGN,
    .SINGLE_QUOTE = $SINGLE_QUOTE,
    .ROUND_BRACKET_START = $ROUND_BRACKET_START,
    .ROUND_BRACKET_END = $ROUND_BRACKET_END,
    .STAR_SIGN = $STAR_SIGN,
    .PLUS_SIGN = $PLUS_SIGN,
    .COMA = $COMA,
    .MINUS_SIGN = $MINUS_SIGN,
    .DOT = $DOT,
    .SLASH_SIGN = $SLASH_SIGN,
    .NUMBER_0 = $NUMBER_0,
    .NUMBER_1 = $NUMBER_1,
    .NUMBER_2 = $NUMBER_2,
    .NUMBER_3 = $NUMBER_3,
    .NUMBER_4 = $NUMBER_4,
    .NUMBER_5 = $NUMBER_5,
    .NUMBER_6 = $NUMBER_6,
    .NUMBER_7 = $NUMBER_7,
    .NUMBER_8 = $NUMBER_8,
    .NUMBER_9 = $NUMBER_9,
    .COLON = $COLON,
    .SEMI_COLON = $SEMI_COLON,
    .LARGER_SIGN = $LARGER_SIGN,
    .EQUAL_SIGN = $EQUAL_SIGN,
    .SMALLER_SIGN = $SMALLER_SIGN,
    .QUESTION_MARK = $QUESTION_MARK,
    .AT_SIGN = $AT_SIGN,
    .A = $A,
    .B = $B,
    .C = $C,
    .D = $D,
    .E = $E,
    .F = $F,
    .G = $G,
    .H = $H,
    .I = $I,
    .J = $J,
    .K = $K,
    .L = $L,
    .M = $M,
    .N = $N,
    .O = $O,
    .P = $P,
    .Q = $Q,
    .R = $R,
    .S = $S,
    .T = $T,
    .U = $U,
    .V = $V,
    .W = $W,
    .X = $X,
    .Y = $Y,
    .Z = $Z,
    .SQUARE_BRACKET_START = $SQUARE_BRACKET_START,
    .BACKSLASH = $BACKSLASH,
    .SQUARE_BRACKET_END = $SQUARE_BRACKET_END,
    .CIRCUMFLEX = $CIRCUMFLEX,
    .UNDERSCORE = $UNDERSCORE,
    .GRAVE_ACCENT = $GRAVE_ACCENT,
    .a = $a,
    .b = $b,
    .c = $c,
    .d = $d,
    .e = $e,
    .f = $f,
    .g = $g,
    .h = $h,
    .i = $i,
    .j = $j,
    .k = $k,
    .l = $l,
    .m = $m,
    .n = $n,
    .o = $o,
    .p = $p,
    .q = $q,
    .r = $r,
    .s = $s,
    .t = $t,
    .u = $u,
    .v = $v,
    .w = $w,
    .x = $x,
    .y = $y,
    .z = $z,
    .CURLY_BRACKET_START = $CURLY_BRACKET_START,
    .VERTICAL_BAR = $VERTICAL_BAR,
    .CURLY_BRACKET_END = $CURLY_BRACKET_END,
    .SWUNG_DASH = $SWUNG_DASH,
    .DELETE = $DELETE,
};
"""

TEMPLATE_MLIST = """
pub const §NAME = [128]?u8{ 
    $NULL,
    $SOH,
    $STX,
    $ETX,
    $EOT,
    $ENQ,
    $ACK,
    $BEL,
    $BACKSPACE,
    $HORTIZONTAL_TAB,
    $LINE_FEED,
    $VERTICAL_TAB,
    $FROM_FEED,
    $ENTER,
    $SHIFT_OUT,
    $SHIFT_IN,
    $DLE,
    $DC1,
    $DC2,
    $DC3,
    $DC4,
    $NAK,
    $SYN,
    $ETB,
    $CANCEL,
    $EM,
    $SUB,
    $ESCAPE,
    $FS,
    $GS,
    $RS,
    $US,
    $SPACE,
    $EXCLAMATION_MARK,
    $DOUBLE_QUOTE,
    $HASHTAG,
    $DOLLARSIGN,
    $PERCENTAGE,
    $ANDSIGN,
    $SINGLE_QUOTE,
    $ROUND_BRACKET_START,
    $ROUND_BRACKET_END,
    $STAR_SIGN,
    $PLUS_SIGN,
    $COMA,
    $MINUS_SIGN,
    $DOT,
    $SLASH_SIGN,
    $NUMBER_0,
    $NUMBER_1,
    $NUMBER_2,
    $NUMBER_3,
    $NUMBER_4,
    $NUMBER_5,
    $NUMBER_6,
    $NUMBER_7,
    $NUMBER_8,
    $NUMBER_9,
    $COLON,
    $SEMI_COLON,
    $LARGER_SIGN,
    $EQUAL_SIGN,
    $SMALLER_SIGN,
    $QUESTION_MARK,
    $AT_SIGN,
    $A,
    $B,
    $C,
    $D,
    $E,
    $F,
    $G,
    $H,
    $I,
    $J,
    $K,
    $L,
    $M,
    $N,
    $O,
    $P,
    $Q,
    $R,
    $S,
    $T,
    $U,
    $V,
    $W,
    $X,
    $Y,
    $Z,
    $SQUARE_BRACKET_START,
    $BACKSLASH,
    $SQUARE_BRACKET_END,
    $CIRCUMFLEX,
    $UNDERSCORE,
    $GRAVE_ACCENT,
    $a,
    $b,
    $c,
    $d,
    $e,
    $f,
    $g,
    $h,
    $i,
    $j,
    $k,
    $l,
    $m,
    $n,
    $o,
    $p,
    $q,
    $r,
    $s,
    $t,
    $u,
    $v,
    $w,
    $x,
    $y,
    $z,
    $CURLY_BRACKET_START,
    $VERTICAL_BAR,
    $CURLY_BRACKET_END,
    $SWUNG_DASH,
    $DELETE,
};
"""

BACKWARDS_TABLE = {
    0: "NULL",
    1: "SOH",
    2: "STX",
    3: "ETX",
    4: "EOT",
    5: "ENQ",
    6: "ACK",
    7: "BEL",
    8: "BACKSPACE",
    9: "HORTIZONTAL_TAB",
    10: "LINE_FEED",
    11: "VERTICAL_TAB",
    12: "FROM_FEED",
    13: "ENTER",
    14: "SHIFT_OUT",
    15: "SHIFT_IN",
    16: "DLE",
    17: "DC1",
    18: "DC2",
    19: "DC3",
    20: "DC4",
    21: "NAK",
    22: "SYN",
    23: "ETB",
    24: "CANCEL",
    25: "EM",
    26: "SUB",
    27: "ESCAPE",
    28: "FS",
    29: "GS",
    30: "RS",
    31: "US",
    32: "SPACE",
    33: "EXCLAMATION_MARK",
    34: "DOUBLE_QUOTE",
    35: "HASHTAG",
    36: "DOLLARSIGN",
    37: "PERCENTAGE",
    38: "ANDSIGN",
    39: "SINGLE_QUOTE",
    40: "ROUND_BRACKET_START",
    41: "ROUND_BRACKET_END",
    42: "STAR_SIGN",
    43: "PLUS_SIGN",
    44: "COMA",
    45: "MINUS_SIGN",
    46: "DOT",
    47: "SLASH_SIGN",
    48: "NUMBER_0",
    49: "NUMBER_1",
    50: "NUMBER_2",
    51: "NUMBER_3",
    52: "NUMBER_4",
    53: "NUMBER_5",
    54: "NUMBER_6",
    55: "NUMBER_7",
    56: "NUMBER_8",
    57: "NUMBER_9",
    58: "COLON",
    59: "SEMI_COLON",
    60: "LARGER_SIGN",
    61: "EQUAL_SIGN",
    62: "SMALLER_SIGN",
    63: "QUESTION_MARK",
    64: "AT_SIGN",
    65: "A",
    66: "B",
    67: "C",
    68: "D",
    69: "E",
    70: "F",
    71: "G",
    72: "H",
    73: "I",
    74: "J",
    75: "K",
    76: "L",
    77: "M",
    78: "N",
    79: "O",
    80: "P",
    81: "Q",
    82: "R",
    83: "S",
    84: "T",
    85: "U",
    86: "V",
    87: "W",
    88: "X",
    89: "Y",
    90: "Z",
    91: "SQUARE_BRACKET_START",
    92: "BACKSLASH",
    93: "SQUARE_BRACKET_END",
    94: "CIRCUMFLEX",
    95: "UNDERSCORE",
    96: "GRAVE_ACCENT",
    97: "a",
    98: "b",
    99: "c",
    100: "d",
    101: "e",
    102: "f",
    103: "g",
    104: "h",
    105: "i",
    106: "j",
    107: "k",
    108: "l",
    109: "m",
    110: "n",
    111: "o",
    112: "p",
    113: "q",
    114: "r",
    115: "s",
    116: "t",
    117: "u",
    118: "v",
    119: "w",
    120: "x",
    121: "y",
    122: "z",
    123: "CURLY_BRACKET_START",
    124: "VERTICAL_BAR",
    125: "CURLY_BRACKET_END",
    126: "SWUNG_DASH",
    127: "DELETE",
}
