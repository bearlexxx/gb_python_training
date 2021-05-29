tsk_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

lenght_tsk_lst = len(tsk_lst)
for i in range(lenght_tsk_lst):
    if tsk_lst[i].isdigit():
        tsk_lst.extend(['"', f'{int(tsk_lst[i]):02d}', '"'])
    elif tsk_lst[i].count('+') or tsk_lst[i].count('-') > 0:
        tsk_lst.extend(['"', f'+{int(tsk_lst[i]):02d}', '"'])
    else:
        tsk_lst.append(tsk_lst[i])

tsk_lst = tsk_lst[lenght_tsk_lst::]
print(' '.join(tsk_lst))

#Remove unnecessary spaces near "
while tsk_lst.count('"') > 0:
    tsk_lst.remove('"')

lenght_tsk_lst = len(tsk_lst)
for i in range(lenght_tsk_lst):
    if tsk_lst[i].isdigit():
        tsk_lst.append(f'"{int(tsk_lst[i]):02d}"')
    elif tsk_lst[i].count('+') or tsk_lst[i].count('-') > 0:
        tsk_lst.append(f'"+{int(tsk_lst[i]):02d}"')
    else:
        tsk_lst.append(tsk_lst[i])

tsk_lst = tsk_lst[lenght_tsk_lst::]
print(' '.join(tsk_lst))
