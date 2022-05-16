# Josh's combos - in Python (via Shawn)
import re
from functools import reduce
from plover import log

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

    "RB": "return",
}

symbolsMap = {
    "RP": "/",
    "FB": "\\",
    "BL": "'",
    "PG": "`",
    "BG": "-",
    "PL": "=",
    "RPL": "[",
    "FBG": "]",
    # todo: period, comma
}

symbolsMap2 = {
    "RP": "slash",
    "FB": "backslace",
    "BL": "apostrophe",
    "PG": "grave",
    "BG": "minus",
    "PL": "equal",
    "RPL": "bracketleft",
    "FBG": "bracketright",
}

leftModsMap = {
    "S": "super",
    "T": "alt",
    "K": "alt",
    "P": "control",
    "W": "control",
    "H": "shift",
    "R": "shift",
}

rightModsMap = {
    "T": "super",
    "S": "super",
    "L": "alt",
    "G": "alt",
    "P": "control",
    "B": "control",
    "F": "shift",
    "R": "shift",
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
    "T": "0"
}}

funcsMap = {**numsBase, **{
    "S": "10",
    "TS": "11",
    "T": "12"
}}

def lookup(chord):
    # extract the chord for easy use
    stroke = chord[0]
    log.info("--- new stroke ---")
    log.info(stroke)
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

    symResult = handleSymbols(stroke)
    if symResult is not None:
        log.info("symResult: " + symResult)
        return symResult

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
    log.info("in handleNav")
    navMatch = re.fullmatch(r'\+([STKPWHR]*)-(.*)', stroke)

    if navMatch is None:
        return None

    (mods, rest) = navMatch.groups()

    if not mods and not rest:
        return None

    if rest and rest not in navsMap:
        return None

    log.info("found nav match")
    modded = addMods(mods, leftModsMap, navsMap.get(rest, ""))
    # return modded
    return "{#" + modded + "}"

def handleSymbols(stroke):
    log.info("in handleSymbols")
    match = re.fullmatch(r'\+([STKPWHR]*)-?([EU]*)(.*)', stroke)

    if match is None:
        return None

    (mods, spacing, rest) = match.groups()

    if not mods and not rest:
        raise KeyError

    if rest and rest not in symbolsMap:
        raise KeyError

    if mods:
        value = symbolsMap2.get(rest, "")
        modded = addMods(mods, leftModsMap, value)
        return "{#" + modded + "}"
    else:
        value = symbolsMap.get(rest, "")
        spaced = addSpacing2(spacing, value)
        return "{^" + spaced + "^}"
    

def handleShortcut(stroke):
    match = re.fullmatch(r'!(.*?)-?([FRPBLGTS]+)', stroke)

    if match is None:
        return None

    (rest, mods) = match.groups()

    if rest and rest not in spellingMap:
        raise KeyError

    modded = addMods(mods, rightModsMap, spellingMap.get(rest, ""))
    return "{#" + modded + "}"

def handleNums(stroke):
    match = re.fullmatch(r'\+([STKPWHR]*)A([EU]*)(.*)', stroke)

    if match is None:
        return None

    (mods, spacing, rest) = match.groups()

    if not rest or rest not in numsMap:
        raise KeyError

    value = numsMap.get(rest, "")
    modded = addSpacing(spacing, value) if spacing else addMods(mods, leftModsMap, value)
    return "{#" + modded + "}"

def handleFuncs(stroke):
    match = re.fullmatch(r'\+([STKPWHR]*)O(.*)', stroke)

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

def addSpacing2(spacing, text):
    before = " " if "E" in spacing else ""
    after = " " if "U" in spacing else ""
    return before + text + after