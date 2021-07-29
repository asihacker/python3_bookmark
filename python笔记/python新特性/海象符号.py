# if else 使用海象符号
a: list[int] = [1, 2, 3, 4]
if (y := len(a)) > 3:
    print("hahaha")
print(y)
# while中使用海象符号
file = open("demo.txt", "r")
while line := file.readline():
    print(line.strip())
while (p := input("Enter the password: ")) != "youpassword":
    continue
# 推到式中使用
members = [
    {"name": "小五", "age": 23, "height": 1.75, "weight": 72},
    {"name": "小李", "age": 17, "height": 1.72, "weight": 63},
    {"name": "小陈", "age": 20, "height": 1.78, "weight": 82},
]

count = 0


def get_bmi(info):
    global count
    count += 1

    print(f"执行了 {count} 次")

    height = info["height"]
    weight = info["weight"]

    return weight / (height ** 2)


# 查出所有会员中过于肥胖的人的 bmi 指数
fat_bmis = [get_bmi(m) for m in members if get_bmi(m) > 24]

print(fat_bmis)
