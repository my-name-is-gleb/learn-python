minutes_input = int(input("Введіть час (хв) –> "))
hours = minutes_input // 60
minutes_left = minutes_input % 60
print(f"{minutes_input} хв це {hours} г. {minutes_left} хв.")
# "//" - это деление нацело(остаток забываем)
# % - это, то что остается после деленея нацело

x = float(input("> "))
if x > 1:
    print(round(1*x+1/x**0.5-1, 3))
else:
    print(f"Число {x}- меньше 1")

