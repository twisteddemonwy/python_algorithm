# 方案一
for cock in range(21):
    for hen in range(33):
        for chick in range(101):
            if (cock + hen + chick) == 100 and ((5 * cock) + (3 * hen) + (chick / 3)) == 100:
                print(f"可购买公鸡{cock}只，母鸡{hen}只，小鸡{chick}只")

# 方案二
for cock in range(21):
    for hen in range(33):
        chick = 100 - cock - hen
        if ((5 * cock) + (3 * hen) + (chick / 3)) == 100:
            print(f"可购买公鸡{cock}只，母鸡{hen}只，小鸡{chick}只")
