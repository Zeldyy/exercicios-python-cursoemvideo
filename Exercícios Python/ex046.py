import emoji
from time import sleep
print('Contagem de fogos de artifício!!!')
for c in range(10,-1, -1):
    print('{}!'.format(c))
    if c != 0:
        sleep(1)
print(emoji.emojize(':collision: BUMM!!! :collision:'))