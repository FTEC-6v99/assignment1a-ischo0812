
import typing as t


def calc_avg(numbers: list[t.Union[int, float]]) -> float:

    sum: float = 0.0
    if len(numbers) == 0:
        raise Exception('expected a non-empty list')
    else:
        for number in numbers:
            sum += number
    return round(sum / len(numbers), 2)
