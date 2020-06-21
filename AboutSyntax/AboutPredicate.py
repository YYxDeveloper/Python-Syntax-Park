import re
# https://zhuanlan.zhihu.com/p/32568168
def re_dPlus():
    content = 'Hello 12345 is a 999 number. Regex String'
    result = re.match('^Hello (\d+).*String$', content)
    # "^Hello " 匹配字符串开头; (\d+) 匹配任意个数字; .* 匹配任意字符(换行符除外);
    # String$ 匹配字符串结尾
    if result:
        print(result.group(1))  # 取出第一个括号的内容, 即(\d+)中的数字
        # 输出结果12345

def re_dPlus_howManyNumberCount():
    content = 'Hello 123456 is a number. Regex String'
    result = re.match('.*(\d+).*', content)
    # 使用.*匹配其他所有字符, (\d+)匹配我们想要的数字數量
    if result:
        print(result.group(1))
def exampleGreedResults():
    example = "<div>test1</div><div>test2</div>"
    greedPattern = re.compile("<div>.*</div>")
    notGreedPattern = re.compile("<div>.*?</div>")
    greedResult = greedPattern.search(example)
    notGreedResult = notGreedPattern.search(example)
    print("greedResult = %s" % greedResult.group())  # <div>test1</div><div>test2</div>
    print("notGreedResult = %s" % notGreedResult.group())  # <div>test1</div>
def compile(pattern, flags=0):
    "Compile a regular expression pattern, returning a pattern object."
    # 生成一个正则表达式模式，返回一个Regex对象
    return _compile(pattern, flags)
def exampleFindEachNumber():
    str = "Working 6 hours a day. Studying 44 hours a day."
    mobj = re.findall(r'[0-9]', str)
    print(mobj)

def exampleFilterNumber():
    s1 = "768 Working 2343 789 five 234 656 hours 324 4646 a 345 day"
    obj1 = re.sub(r'\d', "8", s1)
    print(obj1)
def exampleFilterChar():
    s = "768 Working 2343 789 five 234 656 hours 324 4646 a 345 day"
    obj = re.sub(r'\D', "i", s)
    print(obj)
def exampleFindFirstNum():
    # r"\d" 意思是在字串中的第一個數字
    pattern = re.compile(r"\d")
    result = pattern.match("9aaa123")#第一個字元只能是數字
    # 轉型失敗::'NoneType' object has no attribute 'group'
    print(result.group())
def exampleFindFirstChar():
    pattern = re.compile(r"\D")#第一個字元只能是英文
    result = pattern.match("Ab11")
    print(result.group())
# re_dPlus()
# re_dPlus_howManyNumberCount()
# exampleGreedResults()

# https://www.delftstack.com/zh-tw/tutorial/python-modules-tutorial/python-regular-expression/
# exampleFindEachNumber()
# exampleFilterChar()
# exampleFilterNumber()
exampleFindFirstNum()
exampleFindFirstChar()


pattern = re.compile(r"abc d", re.I|re.X)
"""
 I = IGNORECASE # 忽略大小写
 X = VERBOSE    # 冗余模式,可以忽略正则表达式中的空白和#号的注释
 """
result = pattern.match("AbcD")
print(result.group())




