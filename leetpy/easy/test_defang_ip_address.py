def defangIPaddr(address):
    return address.replace(".", "[.]")


def test_1():
    assert defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"


def test_2():
    assert defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
