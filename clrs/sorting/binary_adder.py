def add(n1, n2):
    sum = [0 for _ in range(len(n1)+1)]
    carryover = 0
    for i in range(len(n1)-1, -1, -1):
        digit_sum = carryover + n1[i] + n2[i]
        # 0, 1, 2, 3
        leftover_digit = digit_sum % 2
        sum[i+1] = leftover_digit
        carryover = int(digit_sum >= 2)
    sum[0] = carryover
    return sum


if __name__ == "__main__":
    n1 = [1, 0]
    n2 = [1, 0]
    result = add(n1, n2)
    print(result)
