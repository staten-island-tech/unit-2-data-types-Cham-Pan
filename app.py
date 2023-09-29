def gcf(x, y):
    if x == 0:
        return y
    return gcf(y % x, x)
print(gcf(0, 123456789))