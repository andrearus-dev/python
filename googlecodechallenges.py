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


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for num in numbers:

    if num == 237:
        break

    if num % 2 == 1:
        continue

    print(num)


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return result


print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
