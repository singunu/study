

num_lst = []
not_self = []
self_num = []
for i in range(1,10001):
    num_lst.append(i)

for i in num_lst:
    str_num = str(i)
    a = i
    for j in str_num:
        a += int(j)
    if a <= 10000:
        not_self.append(a)

for i in num_lst:
    if i not in not_self:
        self_num.append(i)

for i in self_num:
    print(i)


