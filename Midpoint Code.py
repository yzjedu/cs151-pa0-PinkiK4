
# User should be prompted to enter both x and y coordinates.

print('What is your x1 value?:')
X1 = float(input())
print('What is your x2 value?:')
X2 = float(input())
print('What is your y1 value?:')
Y1 = float(input())
print('What is your y2 value?:')
Y2 = float(input())

# Code will generate a midpoint and print it to the user
mid_point = ((X1 + X2) / 2, (Y1 + Y2) / 2)
print(mid_point)
