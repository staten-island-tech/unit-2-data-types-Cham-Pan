def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)

print(gcf(100, 200))
print(gcf(200, 100))