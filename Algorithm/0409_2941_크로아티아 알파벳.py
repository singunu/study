inpt = 'AA'
inpt += str(input())
inpt += 'AA'
cnt = len(inpt)-4

for i in range(2,len(inpt)-2):
    if inpt[i]+inpt[i+1] == 'c=' or inpt[i]+inpt[i+1] == 'c-':
        cnt -= 1
    elif inpt[i] == 'z':
        if inpt[i-1] == 'd' and inpt[i+1] == '=':
            cnt -= 2
        elif inpt[i+1] == '=':
            cnt -= 1
    elif inpt[i] + inpt[i+1] == 'd-':
        cnt -= 1
    elif inpt[i] + inpt[i+1] == 'lj' or inpt[i] + inpt[i+1] == 'nj':
        cnt -= 1
    elif inpt[i] + inpt[i+1] == 's=':
        cnt -= 1
print(cnt)

