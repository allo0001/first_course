logs =[]

with open('nginx_logs.txt', 'r') as f:
    while True:
        s = f.readline()
        if not s:
            break
        s = s.split('"')[:2]
        logs.append((s[0].split(' ')[0], s[1].split(' ')[0], s[1].split(' ')[1]))
    print(logs)