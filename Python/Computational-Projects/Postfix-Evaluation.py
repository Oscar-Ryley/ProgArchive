import operator
operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def eval_postfix(postfix):
    stack = []
    for i in postfix:
        if i.isdigit() == True:
            stack.append(int(i))
        else:
            first = int(stack.pop())
            second = int(stack.pop())
            stack.append(operator_dict[i](second, first))
    return(stack[0])

print(eval_postfix(["4", "5", "1", "2", "+", "-", "/"]))