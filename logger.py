from datetime import datetime
import os

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

p = os.path.abspath('log.txt')

def fabric_of_functions(old_function):
    def new_function(*args,**kwargs):
        startTime = datetime.now()
        result = old_function(*args,**kwargs)
        f = open('log.txt','w')
        f.write(f"{str(startTime)}\n")
        f.write(f"{str(result)}\n")
        f.write(f"{old_function.__name__}\n")
        f.write(f"{args,kwargs}")
        f.close()
        return result
    return new_function


@fabric_of_functions
def flat_generator(list,param = ''):
    cursor_1 = 0
    cursor_2 = 0
    while cursor_1 < len(list):
        while cursor_2 < len(list[cursor_1]):
            yield list[cursor_1][cursor_2]
            cursor_2 += 1
        cursor_2 = 0
        cursor_1 += 1
    flat_list = [item for item in flat_generator(nested_list)]
    return (flat_list)

flat_generator(nested_list,p)


