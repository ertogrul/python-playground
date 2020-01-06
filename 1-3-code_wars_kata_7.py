
def get_sum(a,b):
    if a == b:
        r = a
    elif a < b:
        i = a; r = a
        while i < b:
            i += 1; r += i
    elif a > b:
        i = b; r = b
        while i < a:
            i += 1; r += i
    return r

print(get_sum(1,5)) # 
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1