# Task 1
# There is string s = "string". Write the code that reverses string, i.e. returns "gnirts"


def reversed_string(s):
    if not isinstance(s, str):
        raise TypeError('Expected input type is string, not {}'.format(type(s)))
    else:
        r = s[::-1]
    return r