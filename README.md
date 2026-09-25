# Regular Expressions

Practice describing patterns in text, then searching, extracting and replacing
with them.

**Practicing:** regex, the `re` module, raw strings

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `hello_world_regex`](#question-1-hello_world_regex)
  - [Question 2: `has_a_vowel`](#question-2-has_a_vowel)
  - [Question 3: `has_cats_or_dogs`](#question-3-has_cats_or_dogs)
  - [Question 4: `has_vowel_start`](#question-4-has_vowel_start)
  - [Question 5: `has_punctuation_end`](#question-5-has_punctuation_end)
  - [Question 6: `has_nothing_or_digits`](#question-6-has_nothing_or_digits)
  - [Question 7: `has_no_flippers`](#question-7-has_no_flippers)
  - [Question 8: `is_valid_email`](#question-8-is_valid_email)
  - [Question 9: `is_valid_phone_number`](#question-9-is_valid_phone_number)
  - [Question 10: `match_all_numbers`](#question-10-match_all_numbers)
  - [Question 11: `match_all_numbers_as_numbers`](#question-11-match_all_numbers_as_numbers)
  - [Question 12: `match_all_words`](#question-12-match_all_words)
  - [Question 13: `replace_all_numbers`](#question-13-replace_all_numbers)
  - [Question 14: `fix_file_name`](#question-14-fix_file_name)
  - [Question 15: `name_redacter`](#question-15-name_redacter)
  - [Question 16: `camel_to_snake_case`](#question-16-camel_to_snake_case)
- [Modify](#modify)
  - [Question 17: `swap_all_cases`](#question-17-swap_all_cases)
- [Debug](#debug)
  - [Question 18: `is_valid_company_username`](#question-18-is_valid_company_username)
- [Resources](#resources)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it what a
character class does, or having it read a pattern back to you in plain
English. Ask it a hundred questions — that is the whole point. What you do
not do is ask it for the pattern. Paste this at the start of a chat and it
will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
must list the strings that should match and the ones that should not. Regex is
where generated code looks right and is subtly wrong, so test every case
yourself. If what comes back does more than you asked for, reject it.

You own every line either way, and you will be asked to explain it.

## Setup

Work in `development/mod-1`. Make a draft branch before you start.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` for everything, or `pytest -k has_a_vowel` for one question.
Scores land in `scores/scores.json`.

75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

## Before You Start

Python keeps regex in the [`re` module](https://www.w3schools.com/python/python_regex.asp).
Patterns are plain strings you pass to a function, rather than their own
piece of language syntax.

```python
import re

re.search(r"cat", "concatenate")    # a match object, or None
re.fullmatch(r"\d+", "123")         # must match the WHOLE string
re.findall(r"\d+", "1 and 22")      # ['1', '22']
re.sub(r"\d+", "#", "1 and 22")     # '# and ##'
```

**Always write patterns as raw strings**, with an `r` in front. Without it,
Python reads the backslashes first and your pattern is not what you typed:
`"\b"` is a backspace character, not a word boundary. Get in the habit now
and it will never bite you.

The `search` functions return a **match object** rather than `True` or `False`.
A match object is truthy and `None` is falsy, so wrap it in `bool()` when a
question asks for a boolean.

[Regex101](https://regex101.com/) lets you build a pattern and see what it
matches as you type. Set the flavor to Python. It is the single most useful
thing you can have open for this assignment.

## From Scratch

Write your solutions in `src/from_scratch.py`. The first nine return `True` or
`False`.

### Question 1: `hello_world_regex`

Write a function `hello_world_regex` that returns `True` if the string
contains "hello world" anywhere, in any mix of cases.

```python
hello_world_regex("HeLlO wOrLd!")   # True
hello_world_regex("Hello")          # False
```

Listing every combination of upper and lower case would mean 2048 patterns.
Ask your AI tutor in **tutor mode** how `re` can be told to ignore case. Make
it explain the idea rather than hand you the pattern.

### Question 2: `has_a_vowel`

Write a function `has_a_vowel` that returns `True` if the string contains a
vowel, in any case. `y` does not count.

```python
has_a_vowel("a")         # True
has_a_vowel("AHHHHHH!")  # True
has_a_vowel("HEY")       # True
has_a_vowel("wow")       # True
has_a_vowel("")          # False
has_a_vowel("xzy")       # False
has_a_vowel("y")         # False
```

### Question 3: `has_cats_or_dogs`

Write a function `has_cats_or_dogs` that returns `True` if the string contains
"cats" or "dogs", in any case. The singular forms do not count.

```python
has_cats_or_dogs("Cats rule!")              # True
has_cats_or_dogs("I do not care for that dog.")   # False
```

### Question 4: `has_vowel_start`

Write a function `has_vowel_start` that returns `True` if the string *starts*
with a vowel, in any case.

```python
has_vowel_start("a")    # True
has_vowel_start("A")    # True
has_vowel_start("ab")   # True
has_vowel_start("Ab")   # True
has_vowel_start("ba")   # False
has_vowel_start("Ba")   # False
has_vowel_start("")     # False
```

### Question 5: `has_punctuation_end`

Write a function `has_punctuation_end` that returns `True` if the string
*ends* with a `.`, `?` or `!`.

```python
has_punctuation_end("a!")    # True
has_punctuation_end("a!a")   # False
```

Inside a character class, a `.` is just a dot. Outside one it means "any
character". Food for thought.

### Question 6: `has_nothing_or_digits`

Write a function `has_nothing_or_digits` that returns `True` if the string is
empty or made up entirely of digits.

```python
has_nothing_or_digits("")        # True
has_nothing_or_digits("123")     # True
has_nothing_or_digits("123abc")  # False
```

"Entirely" is the hard part. A search that finds digits *somewhere* will
happily accept `123abc`.

### Question 7: `has_no_flippers`

Write a function `has_no_flippers` that returns `True` if the string contains
none of these characters: `B C c D E H I K O o X x l`.

Note this list is case sensitive, and only some letters appear in both cases.

```python
has_no_flippers("Z")         # True
has_no_flippers("Zabdabbq")  # True
has_no_flippers("")          # True
has_no_flippers("abd")       # True
has_no_flippers("B")         # False
has_no_flippers("BC")        # False
has_no_flippers("oao")       # False
has_no_flippers("abdefo")    # False
```

### Question 8: `is_valid_email`

Write a function `is_valid_email` that returns `True` if the string is a valid
email address.

```python
is_valid_email("maya.b@marcy.org")    # True
is_valid_email("gonzalo@marcy")       # False, no domain ending
is_valid_email("ben@marcy.")          # False, empty domain ending
is_valid_email("carms%@marcy.org")    # False, % is not allowed
```

Read the tests for exactly which forms count. Real email validation is
famously horrible, so match the tests rather than the whole specification.

### Question 9: `is_valid_phone_number`

Write a function `is_valid_phone_number` that returns `True` for a US phone
number written any of these ways:

```python
is_valid_phone_number("860-227-7890")     # True
is_valid_phone_number("(860) 410-7890")   # True
is_valid_phone_number("860 892 8010")     # True
is_valid_phone_number("860.888.4872")     # True
is_valid_phone_number("8602277898")       # False, no separators
```

This one is a stumper. Build it a piece at a time in Regex101, and remember
that a `(` means something in a pattern, so a literal one needs escaping.

### Question 10: `match_all_numbers`

Write a function `match_all_numbers` that returns a list of every number in
the string, as **strings**.

```python
match_all_numbers("I have 1 dog and 22 cats.")   # ['1', '22']
match_all_numbers("abc")                          # []
```

Note `22` comes back whole, not as `2` and `2`.

### Question 11: `match_all_numbers_as_numbers`

Write a function `match_all_numbers_as_numbers` that does the same thing, but
returns **integers**.

```python
match_all_numbers_as_numbers("I have 1 dog and 22 cats.")   # [1, 22]
```

### Question 12: `match_all_words`

Write a function `match_all_words` that returns a list of every word in the
string. Digits are not words, and an apostrophe stays inside a word.

```python
match_all_words("I don't think I'm going, but you can!")
# ['I', "don't", 'think', "I'm", 'going', 'but', 'you', 'can']

match_all_words("wow_this_screen_name_is_long")
# ['wow', 'this', 'screen', 'name', 'is', 'long']
```

Careful: `\w` includes digits and underscores, and both tests above say it
should not. You may want to spell out the letters you mean.

### Question 13: `replace_all_numbers`

Write a function `replace_all_numbers` that replaces every number with `"???"`.

```python
replace_all_numbers("There were 40 fire drills, and 0 fires")
# 'There were ??? fire drills, and ??? fires'
```

`100` becomes one `???`, not three.

### Question 14: `fix_file_name`

Write a function `fix_file_name` that replaces every run of whitespace with a
single underscore.

```python
fix_file_name("hello   world")            # 'hello_world'
fix_file_name("first hw-trial spring")    # 'first_hw-trial_spring'
```

Tabs and newlines are whitespace too, and a run of them becomes one
underscore.

### Question 15: `name_redacter`

Write a function `name_redacter` that replaces every ALL CAPS word of two or
more characters with `"REDACTED"`.

```python
name_redacter("Today is MAYA's first day, ZO will help her out.")
# "Today is REDACTED's first day, REDACTED will help her out."
```

Note the `'s` survives. A single capital `A` is left alone.

### Question 16: `camel_to_snake_case`

Write a function `camel_to_snake_case` that converts a camelCase string to
snake_case.

```python
camel_to_snake_case("helloWorldHowAreYou")     # 'hello_world_how_are_you'
camel_to_snake_case("do-not-touch-kebab-case") # unchanged
```

You need the matched capital in your replacement, not a fixed string. Ask your
AI tutor in **tutor mode** how to refer back to what you matched inside
`re.sub`. Make it explain the idea rather than hand you the replacement. This
is a cool trick to know, I can't wait till you learn it too!

## Modify

### Question 17: `swap_all_cases`

Rewrite `swap_all_cases` in `src/modify.py` so it uses `re.sub` instead of
looping over every character by hand. It should swap the case of every letter
and leave everything else alone.

```python
swap_all_cases("SpONGeBoB TeXT")   # 'sPongEbOb tExt'
```

`re.sub` accepts a **function** in place of the replacement string, and calls
it with each match. The tests check you used `.upper()` and `.lower()` once
each.

Python does have `str.swapcase()`, which would do the whole thing in one call.
The tests forbid it, because then you would not have written a regex. Sorry.

## Debug

### Question 18: `is_valid_company_username`

Oh man. `is_valid_company_username` in `src/debug.py` checks a username
against a pattern built from the employee's own name. It works, right up
until it meets a surname with a `.` in it.

Rosa **St.John** validates fine. So does a completely different person, whose
username is `sales9b-aStXJohn`. The `.` from her surname went straight into
the pattern, where it means "any character". Her name became part of the
pattern instead of text to look for.

Fix it so that a name is treated as literal text. Look up
[`re.escape`](https://www.w3schools.com/python/ref_module_re.asp), and think
about which other characters in a real surname would cause the same problem.

This one matters beyond the assignment. Building a pattern out of a value
somebody else controls, without escaping it, is a real bug with a real name.
It is how validation quietly lets the wrong thing through.

## Resources

- [Learn Regular Expressions in 20 Minutes](https://www.youtube.com/watch?v=rhzKDrUiJVk)
  — a good place to start if patterns still look like line noise
- [regular-expressions.info](https://www.regular-expressions.info) — the
  reference for what every symbol does, in any language
- [Launch School RegEx Mini Course](https://launchschool.com/books/regex/read/introduction)
  — short, and language neutral
- [W3Schools Python RegEx](https://www.w3schools.com/python/python_regex.asp)
  — the `re` functions and flags, with examples
- [Real Python: Regular Expressions](https://realpython.com/regex-python/) —
  longer, and Python specific
- [Regex101](https://regex101.com/) — build a pattern and watch what it
  matches. Set the flavor to Python
- [Regexr](https://regexr.com) — another tester, with a cheat sheet down the
  side

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Open a pull request to your instructor for feedback.

## Good luck!

Regex looks like line noise until one day it does not. Keep Regex101 open,
build patterns a piece at a time, and you got this!
