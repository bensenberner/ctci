def validate(string):
    stack = []
    parens = {"(": ")",
              "{": "}",
              "[": "]"}
    for i in string:
        if i in parens.keys(): stack.append(i)
        if i in parens.values():
            if not stack: return False
            leftParen = stack.pop()
            if parens[leftParen] is not i:
                return False

    return True if not stack else False

if __name__ == "__main__"
    a = "{}()[])"
    b = "{[(])}"
    c = "{[()]}"
    print(validate(a))
    print(validate(b))
    print(validate(c))
