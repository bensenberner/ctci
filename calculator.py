'''
given an arithmetic expression consisting of positive integers, +, -, *, /, no
parentheses, compute the result

I would append everything onto a stack, consolidating * and / expressions, and
then I would go through the stack again and consolidating the + and -
expressions. Runtime: O(2n), space O(n)

question for interviewer: should I assume the expression is valid??
'''

# TODO: figure out all the stuff w.r.t. the push / pop / append order

def evaluateExpression(exp):
    exp = exp[::-1]
    stack = []
    n = len(exp)
    if n == 0: return 0
    higherOrderOps = set(["*", "/"])

    # every even index is an operator, every odd is an operand
    # this first loop is to evaluate the higherOrderOps
    while (len(exp) > 0):
        currNum = exp.pop()

        # if there's still some left in the stack, then we can make things work
        # we are assuming that exp[0] is an operator and exp[1] is an operand
        if (len(exp) > 0):
            # evaluate higherOrderOp chain (apply to currNum)
            if (exp[-1] in higherOrderOps):
                while (len(exp) > 0 and exp[-1] in higherOrderOps):
                    operator = exp.pop()
                    operand = exp.pop()
                    currNum = calculate(currNum, operator, operand)
                stack.append("+")
                stack.append(currNum)

            # simply append the lowerOrderOp
            else:
                stack.append(currNum)
                stack.append(exp.pop())
        else:
            stack.append(currNum)

    # now evaluate the stack, which consists solely of lower order expressions
    print(stack)

    # initialize
    if len(stack) > 0:
        finalNum = stack.pop()
    else:
        return 0

    while (len(stack) > 0):
        operator = stack.pop()
        operand = stack.pop()
        finalNum = calculate(finalNum, operator, operand)

    return finalNum

def calculate(op1, operator, op2):
    if operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    elif operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    else:
        return 0

if __name__ == "__main__":
    # ordinarily this would probably be a string and I'd have to do some
    # casting stuff but WHATEVER

    exp = [2, "*", 3, "+", 5, "/", 6, "*", 3, "+", 15]
    print(evaluateExpression(exp))
