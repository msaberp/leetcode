def reverseArray(a: list[int]) -> list[int]:
    """Reverses the given array"""
    for num_idx, num in enumerate(a):
        if num_idx < len(a) // 2:
            reverse_idx = len(a) - num_idx - 1
            reverse_num = a[reverse_idx]
            a[num_idx] = reverse_num
            a[reverse_idx] = num
    return a


if __name__ == '__main__':
    reverseArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])