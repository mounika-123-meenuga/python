def formatINR(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3,-len(s),-2)][::-1] + [s[-3:]])
    return "".join([r]+ d)
print(formatINR(504678))
