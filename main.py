l = 8
for i in range(1, l + 1):
    print(("" * (l - i) + "*" * (i)) + ("  " * (l - i) + "*" * (i)))
else:
   l = 8
for i in range(l):
    print(("" * i + "*" * (l - i)) + ("  " * i + "*" * (l - i)))