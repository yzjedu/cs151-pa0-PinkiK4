# Programmed by Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: September 18, 2024
# Programming Assignment: 01


# The purpose of this code is to prompt the user to input coordinates, /
# and use these coordinates to output a midpoint value

# User should be prompted to enter both x and y coordinates. /
# User inputs will then be converted to a float value
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
print('Your midpoint value is', mid_point)
