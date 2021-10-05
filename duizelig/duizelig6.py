x = 50
y = 51
ans = 0 
# while ans <= 1000:
#     ans = ans + x + y
#     print(str(ans) + "+" + str(x) + " + " + str(y) + " = " + str(ans))
#     y = y + 2
#     x = x + 2

while ans <= 1000:
    ans = x + ans
    print(str(ans) + "+" + str(x) + "=" + str(ans))
    x = x + 1



