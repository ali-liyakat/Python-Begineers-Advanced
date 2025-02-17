import time

def get_square(numbers):
    start = time.time()
    result = []
    for n in numbers:
        result.append(n*n)
    end = time.time()
    print(f"get_square took {(end - start)*1000} mil seconds")
    return result


def get_cube(numbers):
    start = time.time()
    result = []
    for n in numbers:
        result.append(n*n*n)
    end = time.time()    
    print(f"get_cube took {(end - start)*1000} mil seconds")
    return result


mylist = [1,2,3,4,5]

print(get_square(mylist))


print(get_cube(mylist))

_ = get_square(range(100000))

_ = get_cube(range(100000))


# decorator

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {(end - start) * 1000} seconds")
        return result
    return wrapper

@timer
def get_square(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
        return result
    

_ = get_square(range(100000))
