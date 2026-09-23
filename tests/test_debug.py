from debug import is_valid_company_username

TEST_SUITE_NAME = "Debug Tests"


def test_is_valid_company_username():
    """is_valid_company_username - correctly checks if an employee has a valid username"""
    assert is_valid_company_username("sales9b-ajohnson1", "albert", "johnson") is True
    assert is_valid_company_username("tech1a-jjones", "jason", "jones") is True
    assert is_valid_company_username("sales4b-areyes", "ana", "reyes") is True
    assert is_valid_company_username("areyes", "ana", "reyes") is False
    assert is_valid_company_username("", "joe", "cats") is False


def test_is_valid_company_username_escapes_names():
    """is_valid_company_username - treats a name as text, not as a pattern"""
    # A real surname can contain characters that mean something in a regex.
    # Rosa St.John's own username must still work...
    assert is_valid_company_username("sales9b-aSt.John", "ana", "St.John") is True

    # ...but an unescaped "." matches ANY character, which would let a
    # different person's username validate as hers.
    assert is_valid_company_username("sales9b-aStXJohn", "ana", "St.John") is False
    assert is_valid_company_username("sales9b-aSt7John", "ana", "St.John") is False

    # The same goes for a name with a + or a * in it.
    assert is_valid_company_username("tech1a-jO'Brien", "jason", "O'Brien") is True
    assert is_valid_company_username("tech1a-jjones", "jason", "O'Brien") is False
