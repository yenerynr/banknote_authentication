from memory_profiler import profile


##redocarate the function to the profiled
@profile
def my_function():
    a= 2
    b = 3
    c = a + b

## run the progammme with the memory profiler

if __name__ == '__main__':
    my_function()