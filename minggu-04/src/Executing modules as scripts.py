# When you run a Python module with
python fibo.py <arguments>

# the code in the module will be executed, just as if you imported it
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# you can make the file usable as a script as well as an importable module
python fibo.py 50
# output
0 1 1 2 3 5 8 13 21 34

# If the module is imported, the code is not run:
import fibo