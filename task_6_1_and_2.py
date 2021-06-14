with open('nginx_logs.txt') as f:
    data = []
    detect_spam = {}
    for line in f:
        info_in_line = line.split()
        data.append((info_in_line[0], info_in_line[5].replace('"', ''), info_in_line[6]))
        detect_spam.setdefault(info_in_line[0], 0)
        detect_spam[info_in_line[0]] += 1

#Task 1
print(data)

#Task 2
detect_spam = sorted(detect_spam.items(), key=lambda i: i[1])
detect_spam.reverse()
print(f' Спамер: {detect_spam[:1]}')