"""Решение задачи 'Расстояние до ближайшего нуля."""


def closest_zero_distance(n:int, arr:list[int]) -> list[int]:
    """Определяет в массиве для каждого числа расстояние до ближайшего нуля.

    Args:
        n: положительное число
        arr: последовательность целых чисел длиной n, содержащая хотя бы один ноль

    Returns:
        последовательность чисел длиной n, где i-й элемент - это разность индексов
        числа под индексом i и ближайшего ноля
    """
    ZERO = 0
    if not ZERO in arr:
        return None

    res_arr = [0] * n

    index_01 = arr.index(ZERO)
    left_border = 0
    stop_cycle = False
    while not stop_cycle:
        # сначала двигаемся влево до разрешенной позиции
        count = 1
        for i in range(index_01 - 1, left_border-1, -1):
            res_arr[i] = count
            count += 1

        # затем двигаемся вправо до разрешенной позиции
        if ZERO in arr[index_01+1:]:
            index_02 = arr.index(ZERO, index_01 + 1)
            right_border = (index_02 - index_01) // 2 + index_01 + 1
        else:
            right_border = len(arr)
            index_02 = right_border

        count = 1
        for i in range(index_01 + 1, right_border):
            res_arr[i] = count
            count += 1

        if right_border == len(arr):
            # условие выхода из цикла
            stop_cycle = True
        else:
            index_01 = index_02
            left_border = right_border

    return res_arr


if __name__ == '__main__':

    try:
        n = int(input('Введите число n: '))
        arr = [int(n) for n in input('Введите последовательность чисел с нулем: ').split()]
    except Exception as err:
        print(f'Ошибка ввода данных ({err}). Перезапустите программу и попробуйте снова.')
        exit(0)
    else:
        print(closest_zero_distance(n, arr))



