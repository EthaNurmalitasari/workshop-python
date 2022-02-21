# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# You can combine several literals in a single pattern using | (“or”)
case 401 | 403 | 404:
    return "Not allowed"


# Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# You can use positional parameters with some builtin classes that provide an ordering for their attributes
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)


# Patterns can be arbitrarily nested
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")


# We can add an if clause to a pattern, known as a “guard”
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


# Subpatterns may be captured using the as keyword:
case (Point(x1, y1), Point(x2, y2) as p2): ...


# Patterns may use named constants
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")