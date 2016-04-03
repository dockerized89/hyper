__author__ = 'elopptj'


def main():
    myList = [['345', 'INT', '456'], ['567', 'DINT', '678'], ['723', 'BOOL', '234']]
    print(myList)
    sort_order = {'DINT': 0, 'BOOL': 1, 'INT': 2}
    myList.sort(key=lambda val: sort_order[val[1]])
    print(myList)


if __name__ == '__main__':
    main()
