# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def func(A, K):
    tmp = list(range(len(A)))
    for i in range(len(A)):
        tmp[(i+K)%len(A)] = A[i]

    return tmp





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3

    func(A, K)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
