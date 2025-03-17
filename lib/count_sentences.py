#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")  # Print instead of raising an error
            self._value = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Print instead of raising an error

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        return sum(1 for sentence in sentences if sentence.strip())

# Test
string = MyString()
string.value = 123  # Should print "The value must be a string."
