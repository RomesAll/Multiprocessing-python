import os, time
print(f'Номер процесса {os.getpid()}')
for i in range(2):
    res = os.fork() # Вызов fork начиная с 4 строчки у нас кодовая база
    time.sleep(10)
    # начинает выполняться в 2 процессах, то есть сначало в 1 процессе выводиться
    # на печать res а потов в другом
    print(res)
