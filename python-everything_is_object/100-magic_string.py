#!/usr/bin/python3
def magic_string():
    return ', '.join(["BestSchool"] * (magic_string.n := getattr(magic_string, "n", 0) + 1))
