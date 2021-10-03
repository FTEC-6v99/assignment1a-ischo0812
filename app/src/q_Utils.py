# Create a function called calculate_avg
# Parameters: the function should have one argument of type list of floats (i.e., the arg should be a list of numbers with decimals)
# Returns: the function should return a float: the average of all the numbers that are given in the list as an argument to this function.
#          The returned value should be rounded to the closest second decimal. Use the build-in round function: https://www.w3schools.com/python/ref_func_round.asp
#
# If the argument is an empty list, raise a new exception with the message: 'expected a non-empty list'
# for reference on exceptions, check the class notes here: https://github.com/FTEC-6v99/python-overview/blob/master/advanced/exceptions.py
#
# Make sure that you add type hints to the function paramter and return value

import typing as t


def cal_average(numbers: list[t.Union[int, float]]) -> float:

    sum: float = 0.0
    if len(numbers) == 0:
        raise Exception('expected a non-empty list')
    else:
        for number in numbers:
            sum += number
    return sum / len(numbers)


numbers = [5.6, 7.7]
print(cal_average(numbers))
