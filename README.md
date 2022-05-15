# Shawn's Mods & Combos

The aim is to enable a hobbyist keyboard to control the functions of your computer, similar to how a 40% keyboard uses layers. This is very influenced by existing system (see the Inspirations section), but has its own specific criteria.

I wanted something that:
* Has the common navigation, symbol, number, and function keys of a keyboard
* Can apply modifiers to those keys
* Is reliable to stroke
* Isn't too hard on the weaker fingers
* Takes advantage of the layout of popular hobbyist boards
  * EcoSteno
  * Todo: Uni support
* Doesn't need firmware modifications
* Has some control over spacing of output
* Compatible with Plover and Phoenix theory
* Work with * in a way that makes sense (when possible)
* Todo: Plover's lookup window support
* Todo: Optional modal mode

## Basic Concepts

This system uses the number keys, and distinguishes between left and right ones (called `L#` and `R#`). The main description is for a split number bar (like on EcoSteno). Notes and a toggle for thumb # keys (like on Uni) will be coming soon.

It provides its own way to input numbers, so can fully replace the default # functionality in your theory. It probably won't be compatible with a theory using # for a different purpose (like Aerick's own theory, which uses # for proper names).

`L#` has 3 modes (with `AO` picking the mode). For each mode, the left side top row (`STPH`) is modifiers and `EU` controls output spacing.
* `L#` by itself turns the right side into nav keys, editing keys, and basic symbol keys (except shifted number symbols).
* `L#A` turns the first three columns of the right side into a num pad. Using shift, lets you access their associated symbols.
* `L#O` turns the num same pad into function keys (with F10-F12 on the fourth column).

`R#` is for using modifiers with single letters, combining the top row on the right (`-FPLT`), with finger spelling on the left.



## Modifiers

The modifiers use the # key/bar and the top row of keys on the same side. If you have a # bar, you can use it the way numbers are traditionally done, pressing both with the same finger (if doing multiple mods at once with a bar, remember you only need 1 finger hitting the bar and can use the strongest finger).

|Modifier|Left |Right|
|--------|-----|-----|
|GUI     |`L#S`|`L#T`|
|ALT     |`L#T`|`L#L`|
|CTRL    |`L#P`|`L#P`|
|SHIFT   |`L#H`|`L#F`|

## Navigation and Symbols
...

## Numbers
...

## Function Keys
...

## Inspirations

* [Josh Combos](https://github.com/JoshuaGrams/single-stroke-modifiers) - The main influence. I like the layout of the combos for nav and symbols a lot. But wanted to avoid the starters and enders.
* [Miryoku](https://github.com/manna-harbour/miryoku) - Took the idea of how the modifiers are laid out. It also has a similar approach to the numpad and func keys.
* [Emily's Modifiers](https://github.com/EPLHREU/emily-modifiers) & [Emily's Symbols](https://github.com/EPLHREU/emily-symbols) - The idea of how spacing can be controlled via vowel keys. Also looked at the code of Modfiers to see how to do a python dict.
