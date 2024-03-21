#!/usr/bin/python3

def remove_char_at(str, n):
    """function that creates a copy of the string
    And removing the character at the position.
    """
    if n < 0 or n >= len(str):
        return (str)
    return str[:n] + str[n + 1:]
