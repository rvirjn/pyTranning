def rev(num):
    num_count, remainder, reverse = 0, 0, 0
    while num > 0:
        remainder = num % 10
        num = num / 10
        reverse = reverse * 10 + remainder
        num_count = num_count + 1
    while len(str(reverse)) < num_count:
        reverse = '0' + str(reverse)
    return reverse

print rev(12345000000)
