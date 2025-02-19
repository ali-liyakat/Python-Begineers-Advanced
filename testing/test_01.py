def add(a, b):
    return a + b

def testing_add():
    assert add(1, 2) == 3
    assert add(-1, -4) == -5

def testing_add_big_nums():
    assert add(2000000, 3000000) == 5000000  # Corrected expected value
