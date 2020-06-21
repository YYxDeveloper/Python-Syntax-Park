class NonInstantClassManager:
    @classmethod
    def exampleClassMethod(cls):
        TheA.cm()  # 类方法cm(cls)调用者： A
        TheB.cm()  # 类方法cm(cls)调用者： B

    @staticmethod
    def exampleStaticMethod():
        TheA.sm()  # 类方法cm(cls)调用者： A
        TheB.sm()  # 类方法cm(cls)调用者： B




#測試用class
class TheA:
    @classmethod
    #https://blog.csdn.net/youngbit007/article/details/68957848
    # 類方法有類變量cls傳入，從而可以用cls做一些相關的處理。
    # 並且有子類繼承時，調用該類方法時，傳入的類變量cls是子類，而非父類。
    def cm(cls):
        print('类方法cm(cls)调用者：', cls.__name__)

    @staticmethod
    #静态方法的使用场景：
    # 如果在方法中不需要访问任何实例方法和属性，
    # 纯粹地通过传入参数并返回数据的功能性方法，
    # 那么它就适合用静态方法来定义，
    # 它节省了实例化对象的开销成本，
    # 往往这种方法放在类外面的模块层作为一个函数存在也是没问题的，
    # 而放在类中，仅为这个类服务。

    def sm():
        print('静态方法sm()被调用')

class TheB(TheA):
    pass


