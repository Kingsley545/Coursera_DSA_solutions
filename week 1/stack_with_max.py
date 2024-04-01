#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_values = []

    def Push(self, a):
        self.__stack.append(a)
        if self.__max_values:
            max = self.__max_values[-1]
            if a >= max:
                self.__max_values.append(a)
        else:
            self.__max_values.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__max_values[-1] == self.__stack[-1]:
            self.__stack.pop()
            self.__max_values.pop()
        else:
            self.__stack.pop()



    def Max(self):
        assert (len(self.__stack))
        return self.__max_values[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
