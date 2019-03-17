def fun(arg):
    if arg < 5:
        print("i entered if and arg is", arg)
        new_arg = arg + 1
        fun(new_arg)
        print("i'm here and arg is", arg)

fun(1)
