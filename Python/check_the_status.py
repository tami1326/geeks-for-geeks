def check_status(a, b, flag):
    if flag == False:
        if a >= 0 or b >= 0:
            if a >= 0 and b < 0 or a < 0 and b >= 0:
                return True
    elif a < 0 and b < 0 and flag == True:
        return True
    return False

print(check_status(1, -1, False))