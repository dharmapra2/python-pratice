def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        global res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(f"res: {res}")  # Now res is accessible and modified

outer_func()
print(res)  # Now res is accessible and modified
