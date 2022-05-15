# Josh's combos - in Python (via Shawn)
import re
from functools import reduce

LONGEST_KEY = 1



spellingMap = {
    "A"     : "a",
    "PW"    : "b",
    "KR"    : "c",
    "TK"    : "d",
    "E"     : "e",
    "TP"    : "f",
    "TKPW"  : "g",
    "H"     : "h",
    "AOEU"  : "i",
    "SKWR"  : "j",
    "K"     : "k",
    "HR"    : "l",
    "PH"    : "m",
    "TPH"   : "n",
    "O"     : "o",
    "P"     : "p",
    "KW"    : "q",
    "R"     : "r",
    "S"     : "s",
    "T"     : "t",
    "U"     : "u",
    "SR"    : "v",
    "W"     : "w",
    "KP"    : "x",
    "KWR"   : "y",
    "SWR"   : "z",
}

navsMap = {
    "R": "left",
    "P": "up",
    "B": "down",
    "G": "right",

    "F": "backspace",
    "L": "delete",

    "RPG": "page_up",
    "FBL": "page_down",

    "FPL": "home",
    "RBG": "end",

    "FR": "escape",
    "LG": "tab",

    "RB": "return"
    
}

leftModsMap = {
    "S": "super",
    "T": "alt",
    "P": "control",
    "H": "shift"
}

rightModsMap = {
    "T": "super",
    "L": "alt",
    "P": "control",
    "F": "shift"
}

numsBase = {
    "R": "1",
    "B": "2",
    "G": "3",
    "FR": "4",
    "PB": "5",
    "LG": "6",
    "F": "7",
    "P": "8",
    "L": "9",
}

numsMap = {**numsBase, **{
    "RB": "0",
}}

funcsMap = {**numsBase, **{
    "S": "10",
    "TS": "11",
    "T": "12"
}}

def lookup(chord):
    # extract the chord for easy use
    stroke = chord[0]
    # return stroke

    # quick tests to avoid regex if non-relevant stroke is sent
    if len(chord) != 1:
        raise KeyError
    assert len(chord) <= LONGEST_KEY

    # if stroke is "+-" or "!-":
    #     return "{*+}"

    navResult = handleNav(stroke)
    if navResult is not None:
        return navResult

    shortcutResult = handleShortcut(stroke)
    if shortcutResult is not None:
        return shortcutResult

    numsResult = handleNums(stroke)
    if numsResult is not None:
        return numsResult

    funcsResult = handleFuncs(stroke)
    if funcsResult is not None:
        return funcsResult

    # stop if none of our handlers match
    raise KeyError
    

def handleNav(stroke):
    navMatch = re.fullmatch(r'\+([STPH]*)-(.*)', stroke)

    if navMatch is None:
        return None

    (mods, rest) = navMatch.groups()

    if not mods and not rest:
        raise KeyError

    if rest and rest not in navsMap:
        raise KeyError

    modded = addMods(mods, leftModsMap, navsMap.get(rest, ""))
    # return modded
    return "{#" + modded + "}"

def handleShortcut(stroke):
    match = re.fullmatch(r'!(.*?)-?([FPLT]+)', stroke)

    if match is None:
        return None

    (rest, mods) = match.groups()

    if rest and rest not in spellingMap:
        raise KeyError

    modded = addMods(mods, rightModsMap, spellingMap.get(rest, ""))
    return "{#" + modded + "}"

def handleNums(stroke):
    match = re.fullmatch(r'\+([STPH]*)A([EU]*)(.*)', stroke)

    if match is None:
        return None

    (mods, spacing, rest) = match.groups()

    if not rest or rest not in numsMap:
        raise KeyError

    value = numsMap.get(rest, "")
    modded = addSpacing(spacing, value) if spacing else addMods(mods, leftModsMap, value)
    return "{#" + modded + "}"

def handleFuncs(stroke):
    match = re.fullmatch(r'\+([STPH]*)O(.*)', stroke)

    if match is None:
        return None

    (mods, rest) = match.groups()

    if not rest or rest not in funcsMap:
        raise KeyError

    modded = addMods(mods, leftModsMap, "F" + funcsMap.get(rest, ""))
    return "{#" + modded + "}"


    return stroke

def addMods(mods, map, text):
    modNames = [map[mod] for mod in mods]
    addMod = lambda text, mod: mod + "(" + text + ")"
    return reduce(addMod, modNames, text)
 
def addSpacing(spacing, text):
    before = "space " if "E" in spacing else ""
    after = " space" if "U" in spacing else ""
    return before + text + after