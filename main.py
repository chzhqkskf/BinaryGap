# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(N):
    b_n = bin(N)
    print(b_n)

    tmp = []
    for i in range(2, len(b_n)):
        print(b_n[i])
        if b_n[i] == '1':
            tmp.append(i)

    print(tmp)

    result = [0]
    for i in range(len(tmp)-1):
        result.append(tmp[i+1]-tmp[i]-1)

    return max(result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    N = 32
    print(print_hi(N))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
