#  Simple calculator using operators +, -, * and /
2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5  # division always returns a floating point number

# Division (/) always returns a float.
17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # floored quotient * divisor + remainder

#  Use the ** operator to calculate powers 1
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7

#  (=) is used to assign a value to a variable
width = 20
height = 5 * 9
width * height

#  If a variable is not “defined” (assigned a value), trying to use it will give you an error

#  Operators with mixed type operands convert the integer operand to floating point
4 * 3.75 - 1


#   Interactive mode, the last printed expression is assigned to the variable
tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)