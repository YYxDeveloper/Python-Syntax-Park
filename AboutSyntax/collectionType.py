'''
List
'''
def exampleIninListWithRange():
    #10~50可以被七整除之list
    alist = [item for item in range(10,50)if(item % 7 == 0)]
    print(alist)

def eample2ListFilterNewList():
    num = ['ab01','ab425','ch004','dd0048']
    room = ['a','b','c']
    rooms = [r + '-' + n for r in room for n in num if r[0] == n[0]]
    print(rooms)


'''
Tuple
 tuple is immutable
'''
exampleIninListWithRange()