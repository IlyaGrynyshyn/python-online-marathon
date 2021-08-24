<<<<<<< HEAD:sprint 05/Task 4.py
=======
import cmath


def solve_quadric_equation(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = b ** 2 - 4 * a * c

        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
        return (f"The solution are x1={x1} and x2={x2}")

    except ValueError:
        return ("Could not convert string to float")
    except ZeroDivisionError:
        return ("Zero Division Error")


print(solve_quadric_equation(1, 5, 6))
print(solve_quadric_equation(0, 8, 1))
print(solve_quadric_equation(1, "abc", 5))
>>>>>>> 85c59ec6779f309321881c55f5564d4f90caa29d:sprint 05 ( Exception handling )/Task 4.py
