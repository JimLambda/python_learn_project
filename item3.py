input_list_1 = [5, 5, 10, 10]

cash_list_1 = []


def fun(input_list, cash_list):
    if len(input_list) == 0:
        print('true')
        return
    elif input_list[0] == 5:
        cash_list.append(input_list[0])
        input_list.pop(0)
        fun(input_list, cash_list)
    elif input_list[0] == 10:
        if 5 in cash_list:
            cash_list.remove(5)
            cash_list.append(input_list[0])
            input_list.pop(0)
            fun(input_list, cash_list)
        else:
            print('false')
            return
    elif input_list[0] == 20:
        if 5 in cash_list and 10 in cash_list:
            cash_list.remove(5)
            cash_list.remove(10)
            cash_list.append(input_list[0])
            input_list.pop(0)
            fun(input_list, cash_list)
        elif cash_list.count(5) >= 3:
            for i in range(3):
                cash_list.remove(5)
            cash_list.append(input_list[20])
            input_list.pop(0)
            fun(input_list, cash_list)
        else:
            print('false')
            return


if __name__ == '__main__':
    fun(input_list_1, cash_list_1)






