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

print("End of this exercise. Moving on to the next")


def array123(nums):

    for num in nums:
        if nums == 1 and nums == 2 and nums == 3:
            return True
        else:
            return False


print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))

print("End of this exercise. Moving on to the next")


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


array123([1, 1, 2, 3, 1])
array123([1, 1, 2, 4, 1])
array123([1, 1, 2, 1, 2, 3])


# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.


def FirstFactorial(num):

    if num == 1:
        return 1

    else:
        return num*(FirstFactorial((num-1)))


print(FirstFactorial(input()))
