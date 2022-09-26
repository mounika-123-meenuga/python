Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sum(x > k for x in arr))