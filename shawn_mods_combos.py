# Shawn's Mods & Combos
# https://github.com/ShawnFumo/shawn-mods-combos
import re
from functools import reduce
from plover import log
import json

# This is global, so restart Plover or set back to "INFO" to get back to normal logging
# log.set_level("DEBUG")

LONGEST_KEY = 1

spellingMap = {
    "A"     : "a",
    "PW"    : "b",
    "KR"    : "c",
    "TK"    : "d",
    "E"     : "e",
    "AU"    : "e", # for thumb cluster # keys on outside
    "TP"    : "f",
    "TKPW"  : "g",
    "H"     : "h",
    "AOEU"  : "i",
    "AOU"   : "i", # for thumb cluster # keys on outside
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
    "R": {"command": "left"},
    "P": {"command": "up"},
    "B": {"command": "down"},
    "G": {"command": "right"},

    "F": {"command": "backspace"},
    "L": {"command": "delete"},
    "PBS": {"command": "insert"},

    "RPG": {"command": "page_up"},
    "FBL": {"command": "page_down"},

    "FPL": {"command": "home"},
    "RBG": {"command": "end"},

    "FR": {"command": "escape"},
    "LG": {"command": "tab", "text": "\t"},

    "RB": {"command": "return", "text": "\n"}, # Does Plover care about \n vs \r?

    "RP": {"text": "/", "command": "slash"},
    # Spaces around \ needed for escaping problem with that and {^}. They aren't printed.
    "FB": {"text": " \\ ", "command": "backslash"},

    "RBGS": {"text": ",", "command": "comma"},
    "FPLT": {"text": ".", "command": "period"},

    "BL": {"text": "'", "command": "apostrophe"},
    "PG": {"text": "`", "command": "grave"},

    "PB": {"text": ";", "command": "semicolon"},

    "BG": {"text": "-", "command": "minus"},
    "PL": {"text": "=", "command": "equal"},

    "RPL": {"text": "[", "command": "bracketleft"},
    "FBG": {"text": "]", "command": "bracketright"},

    "PS": {"command": "print"},
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
    log.debug("--- new stroke ---")
    log.debug(stroke)

    # quick tests to avoid regex if non-relevant stroke is sent
    if len(chord) != 1:
        raise KeyError
    assert len(chord) <= LONGEST_KEY

    (nums, leftC, leftV, rightV, rightC) = parseStroke(stroke)
    log.debug("Parsed: (" + nums + ") (" + leftC + ") (" + leftV + ") (" + rightV + ") (" + rightC + ")")
 
    # The system relies on at least one num key being pressed
    if not nums:
        raise KeyError

    # Press a modifier by itself on either side
    if nums == "+" and leftC and not leftV and not rightV and not rightC:
        log.debug("single modifier left side")
        return handleJustMods(leftC, leftModsMap)
    if nums == "!" and rightC and not leftV and not rightV and not leftC:
        log.debug("single modifier right side")
        return handleJustMods(rightC, rightModsMap)

    if nums == "+" and rightV and not rightC:
        log.debug("single space special case")
        return handleSingleSpace(leftC)

    if nums == "+" and leftV == "A":
        # For thumb cluster #s on outside, where it is hard to hit #O or #AO
        if "Z" in rightC or "D" in rightC:
            log.debug("funcs layer via num + D or Z")
            return handleFuncs(leftC, rightV, rightC.replace("D", "").replace("Z", ""))
        else:
            log.debug("nums layer")
            return handleNums(leftC, rightV, rightC)

    # Todo: Could also possibly do something like R=1, RB = F1, PB=5, PBLG=F5?
    if nums == "+" and (leftV == "O" or leftV == "AO"):
        log.debug("funcs layer")
        return handleFuncs(leftC, rightV, rightC)

    if nums == "+" and not leftV:
        log.debug("nav/sym layer")
        return handleNav(leftC, rightV, rightC)

    if nums == "!":
        log.debug("shortcut layer")
        return handleShortcut(rightC, leftC + leftV + rightV)

    # stop if none of our handlers match
    raise KeyError
    
def parseStroke(stroke):
    navMatch = re.fullmatch(r'([\+!]*)([STKPWHR]*)([AO]*)-?([EU]*)(.*)', stroke)

    if navMatch is None:
        raise KeyError

    return navMatch.groups()

def handleSingleSpace(modifiers):
    # Just a single space by itself. Doesn't matter which vowels are used.
    spaceVal = {"text": " ", "command": "space"}
    log.debug("doing a space")
    if modifiers:
        return addMods(modifiers, leftModsMap, spaceVal)
    else:
        return "{^ ^}"

def handleJustMods(modifiers, map):
    return addMods(modifiers, map, {"command": ""})

def handleNav(modifiers, spacing, rest):
    log.debug("in handleNav")
    log.debug("mods: " + modifiers)
    log.debug('spacing: ' + spacing)
    log.debug('rest: ' + rest)

    if not modifiers and not rest:
        log.debug("not mods and not rest")
        raise KeyError

    if rest and rest not in navsMap:
        log.debug("rest and rest not in navsMap")
        raise KeyError

    val = navsMap[rest]
    log.debug(json.dumps(val))
    
    final = addSpacing(spacing, addMods(modifiers, leftModsMap, val))
    log.debug(final)
    return final
    
def handleNums(modifiers, spacing, rest):
    if not modifiers and not rest:
        log.debug("not mods and not rest")
        raise KeyError

    if rest and rest not in numsMap:
        log.debug("rest and rest not in navsMap")
        raise KeyError

    val = {"text": numsMap[rest], "command": numsMap[rest]}
    return addSpacing(spacing, addMods(modifiers, leftModsMap, val))

def handleFuncs(modifiers, spacing, rest):
    # Todo: Should spacing for funcs be removed?
    log.debug("mods: " + modifiers)
    log.debug('spacing: ' + spacing)
    log.debug('rest: ' + rest)
    
    if not modifiers and not rest:
        log.debug("not mods and not rest")
        raise KeyError

    if rest and rest not in funcsMap:
        log.debug("rest and rest not in funcsMap")
        raise KeyError

    val = {"command": "F" + funcsMap[rest]}
    return addSpacing(spacing, addMods(modifiers, leftModsMap, val))

def handleShortcut(modifiers, rest):
    if not modifiers and not rest:
        log.debug("not mods and not rest")
        raise KeyError
    
    if rest and rest not in spellingMap:
        log.debug("rest and rest not in spellingMap")
        raise KeyError

    val = {"text": spellingMap[rest], "command": spellingMap[rest]}
    return addSpacing("", addMods(modifiers, rightModsMap, val))
    

def addMods(mods, map, val):
    addMod = lambda text, mod: mod + "(" + text + ")"

    text = val["command"]
    useCommand = mods or "text" not in val

    modNames = [map[mod] for mod in mods]
    modded = reduce(addMod, modNames, text)

    return "{#" + modded + "}" if useCommand else val["text"]

def addSpacing(spacing, text):
    space = "{^ ^}"
    before = space if "E" in spacing else "{^}"
    after = space if "U" in spacing else "{^}"
    return before + text + after
