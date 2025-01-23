from Stack import MyStack


def check(my_str):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = MyStack()
    for i in my_str:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack.peek():
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
