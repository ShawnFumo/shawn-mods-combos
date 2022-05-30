# Shawn's Mods & Combos

The aim is to enable a hobbyist keyboard to control the functions of your computer, similar to how a 40% keyboard uses layers. This is very influenced by existing system (see the [Inspirations](#inspirations) section), but has its own specific criteria.

I wanted something that:
* Has the common navigation, symbol, number, and function keys of a keyboard
* Can apply modifiers to those keys
* Is reliable to stroke
* Isn't too hard on the weaker fingers
* Takes advantage of the layout of popular hobbyist boards like:
  * [EcoSteno](https://nolltronics.com/product/ecosteno/?v=7516fd43adaa) - Split # bar
  * [Uni](https://stenokeyboards.com/products/the-uni) - # key for each thumb
* Doesn't need firmware modifications
* Has some control over spacing of output
* Compatible with [Plover theory](https://github.com/openstenoproject/plover/wiki/Learning-Stenography) and [Phoenix theory](https://www.chicorymeadow.com/)
* Uses undoable inputs when possible

## Demonstration
<a href="https://www.youtube.com/watch?v=XMFucXkGYqg" title="Shawn's Mods & Combos for Plover">
  <p>
    <img width="75%" src="https://img.youtube.com/vi/XMFucXkGYqg/maxresdefault.jpg" alt="Video thumbnail"/>
    <br />https://www.youtube.com/watch?v=XMFucXkGYqg
  </p>
</a>

## Basic Concepts

This system uses the number keys, and distinguishes between left and right ones (called `L#` and `R#` in this readme). This can be either a split # bar like on the EcoSteno or thumb # keys (on the outside) like on the Uni.

It provides its own way to input numbers, so can fully replace the default # functionality in your theory. If you want to use it with a theory already using # for special purposes (like [Aerick's theory](https://github.com/aerickt/steno-dictionaries)), the normal # would need its own key like Top S.

`L#` exposes 3 modes. The level vowels help determine the mode. The right vowels control spacing. The [modifiers](#modifiers) are columns on the left side. Desired outputs are on the right.
* [Nav & Symbols](#navigation-and-symbols) - all the keys that aren't a letter, number, or func key. Excludes the shifted number symbols.
* [Number Pad](#number-pad) - The first three columns of the right side become a num pad (along with two ways to write 0). Using shift lets you access their associated symbols.
* [Function Keys](#function-keys) - Same layout as the Number Pad, but with F10-F12 on the fourth column.

`R#` is for using modifiers with single letters, combining the columns on the right for [modifiers](#modifiers), with [finger spelling](#shortcuts-and-fingerspelling) using the left side and vowels. It can also fully replace normal fingerspelling if you want.

> __Note:__ The limitations of Plover with a board using a serial protocol still apply. You can't keep a modifier or other key held down, either to do something like hold Shift and click your mouse, or hold Up to have it repeatedly move upward (see the note in [Installation](#installation) on repeating the last stroke manually via the # key). There may be a way around this eventually with the HID protocol or other methods.

> __Note:__ It is out of scope of this system to provide symbols that aren't on a normal western keyboard. For things like arrows and math symbols, you should still consider something like [Emily's Symbols](#inspirations).


## Modifiers

The modifiers use the consonant keys on the same side as the # key you're pressing.

If you have a # bar, you can use it the way numbers are traditionally done, pressing both the bar and top row key with the same finger (if doing multiple mods at once, remember you only need 1 finger hitting the bar and can use the strongest finger).

If using a thumb # key, it may be more comfortable to reach the modifiers on the lower row instead.

|Modifier|Left #    |Right #     |
|--------|----------|------------|
|GUI     |`S`       |`-T` or `-S`|
|ALT     |`T` or `K`|`-L` or `-G`|
|CTRL    |`P` or `W`|`-P` or `-B`|
|SHIFT   |`H` or `R`|`-F` or `-R`|

> __Note:__ You can use a modifier by itself from either side. For instance, to bring up the start menu on Windows, you could use `L#S` or `R#-T` or `R#-S` to press the GUI/Windows button.


## Spacing
By default, all symbols and numbers will suppress any spacing. Outputting an equal sign in [Nav/Symbols Mode](#navigation-and-symbols) would output something similar to `{^=^}`. Using the right vowels will force a space on the corresponding side (or both).

|Vowel|Output|
|-----|------|
|     |`^=^` |
|E    |`⎵=^` |
|U    |`^=⎵` |
|EU   |`⎵=⎵` |

This works with modifiers and even navigation keys as well. Spacing with mods makes the most sense with shifted symbols, but otherwise it will still output everything in order. `EU` with `CTRL-Left` would output a space, do control+left, and output another space.

> __Note:__ In any mode using `L#`, pressing any of the right vowels and no right-side consonants will output a single space. This lets you add a space without outputting any symbols, but more importantly lets you use modifiers to do things like ctrl-space.


## Navigation and Symbols

This mode is for the common keys that aren't letters, numbers, or function keys. 

|Input |Key   |Notes|
|---|---|---|
|||__Inverted T layout__|
|`-P`|Up||
|`-R`|Left||
|`-B`|Down||
|`-G`|Right||
|||__Other Nav__|
|`-RPG`|Page Up|Shape of an arrow pointed up|
|`-FBL`| Page Down|Shape of an arrow pointed down|
|`-FPL`|Home||
|`-RBG`|End||
|||__Editing__|
|`-F`|Backspace|Deletes to left|
|`-L`|Delete|Deletes to right|
|`-PBS`|Insert|Sounds like `NS`
|`-RB`|Enter|Down-left, like the motion of a new line. Undoable when not used with modifiers|
|`-FR`|Escape||
|`-LG`|Tab|Undoable when not used with modifiers
|||__Diagonal Shapes__|
|`-RP`|/|up-right|
|`-FB`|\ |down-right|
|`-BL`|'|up-right (in some fonts)|
|`-PG`|`|down-right|
|||__Horizontal Lines__|
|`-BG`|-|Lower
|`-PL`|=|Higher
|||__Punctuation__|
|`‑FPLT`|.|Most theories have period on the top row|
|`‑RBGS`|,|Most theories have comma on the bottom row|
|`-PB`|;|Vertical line shape|
|||__Other__|
|`-RPL`|[||
|`-FPG`|]||
|`-PS`|Print Screen| The initials of **P**rint **S**creen


## Number Pad
Numbers are accessed by using `L#A`.

It is laid out like a number pad on the right, using the first three columns and using vertical combos for the middle row. `-R`  for `1`, `-PB` for `5` and `-L` for `9`.

`0` is `-RB` or `-T`. `-T` makes it easier to do `()` by putting `0` next to `9`.

You can get to all the symbols on number keys by using the shift modifier `P` or `R`.


## Function Keys
There is two ways to access function keys. With a top # bar, you can use `L#O`. You can technically use `L#AO` for a thumb # key, but this is usually hard to press. Instead, you can use the number pad of `L#A` along with `-Z`. 

It is laid out the same as the number pad but also uses the fourth row to give `F10` through `F12` via `-S`, `-TS`, and `-T`.


## Shortcuts and Fingerspelling 
To do shortcuts involving letter keys, you can use `R#`, the modifiers on the right side, and then normal finger spelling using the left consonants and vowels (see the note about variations when using thumb # keys).

These are the standard fingerspelling combos like `KR` for `c` and `SKWR` for `j`. For `z`, you can use either Plover's `STKPW` or Phoenix's `SWR`. `i` can be Plover's `EU` or Pheonix's `AOEU`.

> __Note:__ When using a thumb cluster # key like on the Uni, you probably can't easily press `E` or `EU` with `R#`. You can use these variations to help: `AU` for `e` and `AOU` for `i`.

You can also use this as an alternative way to do finger spelling by using no modifiers for lowercase letters and `-P` or `-R` to shift to capitals. You could free up your normal fingerspelling strokes for something else if you wanted.

You can't add spacing via `EU` due to being needed for fingerspelling vowels, but remember you can use `L#` and any right vowel to quickly [add a space](#spacing) (or your theory's normal space stroke).


## Examples
When showing two different strokes, first is for a board with a top # bar, and second for a thumb # key.
|Stroke|Output|Notes
|---|---|---
`L#P`|`Up`|basic navigation (one key per hand!)
`L#AEUL`|`⎵9⎵`|number w/ leading & ending space
`L#REPL`<br>or<br>`L#REWL`|`⎵+`|shifted symbol w/ leading space
`R#KR-P`<br>or<br>`R#KR-B`|`Ctrl-C`|Shortcut w/ modifier
`L#POPB`<br>or<br>`L#WAPBZ`|`Ctrl-F5`|Func key w/ modifier


## Installation
You need to install [Python Dictionary support](https://github.com/benoit-pierre/plover_python_dictionary) to use this dictionary.

You also need to change the default available keys so that the left and right # can be distinguished, and then map them to the corresponding Gemini codes from your keyboard. 

The [StenoType Extended plugin](https://github.com/sammdot/plover-stenotype-extended) adds `^` and `+` to `#`, but I felt `^` is confusing (looks like the attach operator) and didn't want to deal with stuff falling through into old `#` in other dicts.

So I removed `#` and added `+` for the left number key and `!` for the right number key.

If you're using Plover theory, you can install the Extended plugin above and modify the `extended_stenotype.py` and change the top row so it looks like this:
```
KEYS = (
  '+-', '!-',
  'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
  'A-', 'O-',
  '*',
  '-E', '-U',
  '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)
```

If you're using the Phoenix add-on, edit `plover_phoenix_stenotype.py` and add the above code anywhere in it.

> __Note:__ If you really want to keep normal #, you can add it to the very beginning of the above as `"#"`, but you'll need to assign it to its own key like upper S.

__EcoSteno Machine Keymap__ -
The number bar buttons in the EcoSteno send out `#2` and `#4` for the left side, so set them to `+-`. The right side are `#8` and `#A`, so set them to `!-`.

__Uni Machine Keymap__ - 
Set `#1` to `+-` and `#2` to `!-`

> __Note:__ If you want to be able to repeat the last stroke by just pressing a # key by itself, you can add the following two entries to your normal personal dictionary: Translate `!` and `+` to `{*+}`. 


## Inspirations

* [Josh Combos](https://github.com/JoshuaGrams/single-stroke-modifiers) - The main influence. I like the layout of the combos for nav and symbols a lot. But wanted to avoid the starters and enders.
* [Miryoku](https://github.com/manna-harbour/miryoku) - Took the idea of how the modifiers are laid out. It also has a similar approach to the numpad and func keys.
* [Emily's Modifiers](https://github.com/EPLHREU/emily-modifiers) & [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) - The idea of how spacing can be controlled via vowel keys. Also started with the code of Modfiers to see how to do a python dict.


### Todo
* Add pics or video to this readme
* Plover lookup window support
* Optional modal mode
* Make installable through plugin manager?
* Mouse support?