# -*- coding: utf-8 -*-
"""
Создано на чт 12 ноября 2020

@автор: КэроринЭзоРыжаяЛисица
"""


def moneyfunc(first, plus, minus):
    print("何か月先まで計算したいですか?")
    a_range = input()
    a_range = int(a_range)+1

    msg = f"""はじめ{first}円、一か月ごとに増える金額{plus}円、定期的(一週間)に使うお金{minus}円の合計"""
    print(msg)

    money = first

    for month in range(1, a_range):
        money = money + plus -4*minus

        if money <= 0:
            print("これ以上はマイナスになります")
            break

        elif money > 0:
            output = f"{month}か月後の貯金: {money}円"
            print(output)
