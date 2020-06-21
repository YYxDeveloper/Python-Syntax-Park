def determineCompoundInterest():
    #本金和 ＝ 本金＊(1+年利率)＊＊定存年份
    #本金五萬,1.5% 年利率,5年
    money = 50000 * (1+0.015) ** 5
    print(money)