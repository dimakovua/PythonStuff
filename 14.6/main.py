""" За допомогою стандартного контейнера deque розв’язати задачу:
По колу розташовано n гравців з номерами від 1 до n. У лічилці m слів.
Починають лічити з першого гравця. m-й за ліком вибуває. Потім знову
лічать з наступного гравця за вибулим. Знову m-й вибуває. Так продовжують,
поки не залишиться жодного гравця. Треба показати послідовність номерів,
що вибувають, при заданих n та m.
""" 
from collections import deque


def main():
    n = input("Put n\n")
    m = int(input("Put m\n"))
    aboba = deque()
    for i in range(int(n)+1):
        aboba.append(i)
    aboba.popleft()
    #print(aboba)
    pointer = 0
    print("Result:")
    while len(aboba) > 0:
        if len(aboba) == 1:
            print(aboba[0])
            break
        pointer += m
        while pointer  >= len(aboba):
            pointer = pointer - len(aboba)
        print(f'{aboba[pointer]}, ')
        del aboba[pointer]

if __name__ == "__main__":
    main()