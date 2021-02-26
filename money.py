# -*- coding: utf-8 -*-
"""
Создано на чт 12 ноября 2020

@автор: КэроринЭзоРыжаяЛисица
"""


print("手元にある金額を入力してください")
a = input()

print("一か月にもらえる金額を入力してください")
b = input()

print("""定期的(一週間づつ)な支出を入力してください""")
c = input()

import program_moneyfunc
program_moneyfunc.moneyfunc(int(a), int(b), int(c))