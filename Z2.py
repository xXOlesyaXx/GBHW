msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(msg):
    if (msg[i].isdigit() or msg[i][1:].isdigit()) and (msg[i] == '5' or msg[i] == '17' or msg[i] == '+5'):
        if msg[i] == '+5':
            msg[i] = "+" + msg[i][1:].zfill(2)
        else:
            msg[i] = msg[i].zfill(2)
        msg.insert(i, '"')
        msg.insert(i+2, '"')
        i += 2
    else:
        i += 1
Strmsg = " ".join(msg)

print(Strmsg)