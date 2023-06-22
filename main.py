
def binary_search(numbers, target):

    l = 0
    r = len(numbers) - 1

    while l <= r:
        m = (l + l) // 2
        m_value = numbers[m]
        if m_value == target:
            return True

        elif target < m_value:
            r = m - 1

        else:
            l = m + 1
    return False


numbers = [1, 8, 10, 15, 19, 24, 29, 30, 36, 43, 50, 56, 62, 69, 74, 80, 84, 90, 97]
print(binary_search(numbers, 15))
