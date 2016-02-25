def stringFromSubstring(string):


def canSubstringMakeString(substr, string):
    test = substr
    while len(substr) < len(string):
        test += substr
