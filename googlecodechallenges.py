# variables

# Write a code fragment (a short part of a Python program) to count heads, shoulders, knees, and toes at a party. The grader will automatically define a variable people for you, counting the number of people at the party. Your code must define four variables, one called heads, one called shoulders, one called knees, and one called toes, equal to the number of heads, shoulders, knees, and toes in total at the party. Your program does not need to print any output. The grader will select a new random value for people each time your code runs.

import random
random_num = random.randint(0, 100)

people = random_num

head = 1*people
shoulders = 2*people
knees = 2*people
toes = 10*people

print(head)
print(shoulders)
print(knees)
print(toes)


def make_bricks(small, big, goal):

    # fail #1 = not enough bricks
    if (goal > big*5 + small):
        return False
# fail #2 not enough small bricks
    if (goal % 5 > small):
        return False

    else:
        return True


print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
