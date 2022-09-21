#!/usr/bin/python3
def to_uper(character):
    if k(character) >= 97 and k(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)

    def uppercase(string):
    string_new = ""
    for character in string:
        string_new += "%c" % to_uper(character)
    print("{:s}".format(string_new))
