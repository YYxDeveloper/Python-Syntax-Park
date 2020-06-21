class StringProvingGround:
    @staticmethod
    def exampleFormatString():
        aa = 9876543.123456
        bb = "jj"
        print("bb %5s format string  = %5.2f" % (bb,aa))
    #%5s 字數壹定要大於5位數少於會用空白補齊
    
    def exampleUseFormatLib():
        age = 3
        name = "bill"
        print("format string with variable,{name}&{age}".format(name = name,age = age))
        #類似swift無限參數設定...
        print("use format show {0} & {1}".format(0,1))

        print("9876.12345 = {0:.2}".format(9876.12345))
        print("5.5625 = {0:.2}".format(5.5625))

        print("{0:10}with 10 space &{1:_^10}".format("bill",100))
    

#
#KILL ZONE
#
StringProvingGround.exampleFormatString()
StringProvingGround.exampleUseFormatLib()

