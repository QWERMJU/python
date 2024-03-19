while True:
    m = input('select123:')
    if m=='1':
        a, b, c, d = input('請輸入四個數字:').split()
        print(f'result = {int(a)*int(c)-int(b)*int(d)}\n')
    elif m=='2':
        print('程式結束')
        break
    elif m=='3':
        num = input('找因數 請輸入一個數字:')
        print(f"{num}的因數有:")
        for i in range(1,int(num)+1):
            if int(num)%i == 0:
                print(i)
        print('\n')