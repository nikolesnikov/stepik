day = int(input())
weight = float(input())
weight2 = 100 - day * 0.2
if weight <= weight2:
    print("Все идет по плану")
    print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {weight2} кг")
else:
    print("Что-то пошло не так")
    print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {weight2} кг")
