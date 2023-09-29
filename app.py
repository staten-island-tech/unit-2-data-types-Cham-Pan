def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)
print(gcf(0, 123456789))