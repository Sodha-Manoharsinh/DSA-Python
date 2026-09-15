test_cases = int(input())

while test_cases:

    n = int(input())

    input_str = input().split()

    a = [None]*n

    freq = {}

    for i in range(n):

        if int(input_str[i]) - 2 < 0:
            a[i] = (int(input_str[i]) - 2) * -1
        else:
            a[i] = int(input_str[i]) - 2

        if a[i] in freq:
            freq[a[i]] += 1
        else:
            freq[a[i]] = 1


    print(a)
    print(freq)

    test_cases -= 1