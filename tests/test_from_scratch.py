from from_scratch import (
    camel_to_snake_case,
    fix_file_name,
    has_a_vowel,
    has_cats_or_dogs,
    has_no_flippers,
    has_nothing_or_digits,
    has_punctuation_end,
    has_vowel_start,
    hello_world_regex,
    is_valid_email,
    is_valid_phone_number,
    match_all_numbers,
    match_all_numbers_as_numbers,
    match_all_words,
    name_redacter,
    replace_all_numbers,
)

TEST_SUITE_NAME = "From Scratch Tests"


def test_hello_world_regex():
    """hello_world_regex - True if the string contains "hello world" in any case"""
    assert hello_world_regex("Hello world")
    assert hello_world_regex("Hello world?")
    assert hello_world_regex("Hello world, are you there?")
    assert hello_world_regex("hello world")
    assert hello_world_regex("HELLO WORLD!")
    assert hello_world_regex("HeLlO wOrLd!")
    assert not hello_world_regex("Sup world!")
    assert not hello_world_regex("Where in the world is Carmen?")
    assert not hello_world_regex("Hello")
    assert not hello_world_regex("")


def test_has_a_vowel():
    """has_a_vowel - True if the string contains a vowel in any case"""
    assert has_a_vowel("a")
    assert has_a_vowel("AHHHHHH!")
    assert has_a_vowel("HEY")
    assert has_a_vowel("wow")
    assert not has_a_vowel("")
    assert not has_a_vowel("xzy")
    assert not has_a_vowel("y")


def test_has_cats_or_dogs():
    """has_cats_or_dogs - True if the string contains "cats" or "dogs" in any case"""
    assert has_cats_or_dogs("Gosh, I love having so many cats!")
    assert has_cats_or_dogs("Wow, I have a lot of dogs!")
    assert has_cats_or_dogs("Cats rule!")
    assert not has_cats_or_dogs("I do not care for that dog.")
    assert not has_cats_or_dogs("Cat? No way.")
    assert has_cats_or_dogs("Cat? No, but I have a ton of dogs.")


def test_has_vowel_start():
    """has_vowel_start - True if the string starts with a vowel in any case"""
    for vowel in "aeiouAEIOU":
        assert has_vowel_start(vowel)
    assert has_vowel_start("ab")
    assert has_vowel_start("Ab")
    assert not has_vowel_start("ba")
    assert not has_vowel_start("Ba")
    assert not has_vowel_start("qasda")
    assert not has_vowel_start("")


def test_has_punctuation_end():
    """has_punctuation_end - True if the string ends with a . or ? or !"""
    assert has_punctuation_end("a.")
    assert has_punctuation_end("a!")
    assert has_punctuation_end("a?")
    assert not has_punctuation_end("a")
    assert not has_punctuation_end("a!a")
    assert not has_punctuation_end("a?b")
    assert not has_punctuation_end("")


def test_has_nothing_or_digits():
    """has_nothing_or_digits - True if the string is empty or only digits"""
    assert has_nothing_or_digits("")
    assert has_nothing_or_digits("123")
    assert has_nothing_or_digits("9")
    assert has_nothing_or_digits("92102798791387045834")
    assert has_nothing_or_digits("4")
    assert not has_nothing_or_digits("abc")
    assert not has_nothing_or_digits("123abc")
    assert not has_nothing_or_digits("2348234681276384126834623493Q11964")


def test_has_no_flippers():
    """has_no_flippers - True if the string has none of B C c D E H I K O o X x l"""
    assert has_no_flippers("Z")
    assert has_no_flippers("Zabdabbq")
    assert has_no_flippers("")
    assert has_no_flippers("abd")
    assert not has_no_flippers("B")
    assert not has_no_flippers("BC")
    assert not has_no_flippers("oao")
    assert not has_no_flippers("abdefo")


def test_is_valid_email():
    """is_valid_email - True if the string is a valid email"""
    assert is_valid_email("a@b.co")
    assert is_valid_email("tom@gmail.com")
    assert is_valid_email("zo@marcy.org")
    assert is_valid_email("maya.b@marcy.org")
    assert is_valid_email("reuben_O@marcy.org")
    assert not is_valid_email("gonzalo@marcy")
    assert not is_valid_email("ben@marcy.")
    assert not is_valid_email("carms%@marcy.org")


def test_is_valid_phone_number():
    """is_valid_phone_number - True if the string is a valid phone number"""
    assert is_valid_phone_number("860-227-7890")
    assert is_valid_phone_number("(860) 410-7890")
    assert is_valid_phone_number("860 892 8010")
    assert is_valid_phone_number("860.888.4872")
    assert not is_valid_phone_number("860-227-789")
    assert not is_valid_phone_number("860-227-78900")
    assert not is_valid_phone_number("8602277898")
    assert not is_valid_phone_number("ohmannotevenclosehere")


def test_match_all_numbers():
    """match_all_numbers - returns a list of all the numbers as strings"""
    assert match_all_numbers("My favorite number is 12.") == ["12"]
    assert match_all_numbers("I have no favorite number.") == []
    assert match_all_numbers(
        "There were 40 fire drills last year, and luckily 0 fires"
    ) == ["40", "0"]
    assert match_all_numbers(
        "I have 1 dog, 2 cats, and 4 bunnies. Oh wait, 8 bunnies."
    ) == ["1", "2", "4", "8"]
    assert match_all_numbers("abc") == []
    assert match_all_numbers("") == []


def test_match_all_numbers_as_numbers():
    """match_all_numbers_as_numbers - returns a list of all the numbers as ints"""
    assert match_all_numbers_as_numbers("My favorite number is 12.") == [12]
    assert match_all_numbers_as_numbers("I have no favorite number.") == []
    assert match_all_numbers_as_numbers(
        "There were 40 fire drills last year, and luckily 0 fires"
    ) == [40, 0]
    assert match_all_numbers_as_numbers(
        "I have 1 dog, 2 cats, and 4 bunnies. Oh wait, 8 bunnies."
    ) == [1, 2, 4, 8]
    assert match_all_numbers_as_numbers("abc") == []
    assert match_all_numbers_as_numbers("") == []


def test_match_all_words():
    """match_all_words - returns a list of all the words in the string"""
    assert match_all_words("123") == []
    assert match_all_words("Hello world!") == ["Hello", "world"]
    assert match_all_words("It looks like...rain today?") == [
        "It", "looks", "like", "rain", "today",
    ]
    assert match_all_words("") == []
    assert match_all_words("I don't think I'm going, but you can!") == [
        "I", "don't", "think", "I'm", "going", "but", "you", "can",
    ]
    assert match_all_words("wow_this_screen_name_is_long") == [
        "wow", "this", "screen", "name", "is", "long",
    ]
    assert match_all_words("I have 3 dogs, 2 cats, and 10 bunnies.") == [
        "I", "have", "dogs", "cats", "and", "bunnies",
    ]


def test_replace_all_numbers():
    """replace_all_numbers - replaces all the numbers in the string with "???" """
    assert replace_all_numbers("My favorite number is 12.") == (
        "My favorite number is ???."
    )
    assert replace_all_numbers("I have no favorite number.") == (
        "I have no favorite number."
    )
    assert replace_all_numbers(
        "There were 40 fire drills last year, and luckily 0 fires"
    ) == "There were ??? fire drills last year, and luckily ??? fires"
    assert replace_all_numbers(
        "I have 1 dog, 2 cats, and 4 bunnies. Oh wait, 8 bunnies."
    ) == "I have ??? dog, ??? cats, and ??? bunnies. Oh wait, ??? bunnies."
    assert replace_all_numbers("abc") == "abc"
    assert replace_all_numbers("") == ""
    assert replace_all_numbers("1") == "???"
    assert replace_all_numbers("100") == "???"


def test_fix_file_name():
    """fix_file_name - replaces all the whitespace in the string with underscores"""
    assert fix_file_name("") == ""
    assert fix_file_name(" ") == "_"
    assert fix_file_name("\t") == "_"
    assert fix_file_name("\n") == "_"
    assert fix_file_name("hello world") == "hello_world"
    assert fix_file_name("hello   world") == "hello_world"
    assert fix_file_name("hello\n    world") == "hello_world"
    assert fix_file_name("first hw-trial spring") == "first_hw-trial_spring"
    assert fix_file_name("assignment-12") == "assignment-12"


def test_name_redacter():
    """name_redacter - replaces ALL CAPS words of 2 or more characters with REDACTED"""
    assert name_redacter("My name is ITZEL.") == "My name is REDACTED."
    assert name_redacter("A name is not something I have.") == (
        "A name is not something I have."
    )
    assert name_redacter("Today is MAYA's first day, ZO will help her out.") == (
        "Today is REDACTED's first day, REDACTED will help her out."
    )


def test_camel_to_snake_case():
    """camel_to_snake_case - converts a camelCase string to snake_case"""
    assert camel_to_snake_case("helloWorld") == "hello_world"
    assert camel_to_snake_case("helloWorldHowAreYou") == "hello_world_how_are_you"
    assert camel_to_snake_case("hello_world") == "hello_world"
    assert camel_to_snake_case("do-not-touch-kebab-case") == "do-not-touch-kebab-case"
    assert camel_to_snake_case("hello") == "hello"
    assert camel_to_snake_case("") == ""
