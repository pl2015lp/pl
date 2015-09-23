userInfo = ["Olya", "Savitska", "Yuriivna"]

for i in range(len(userInfo)):
    # заміняємо слово на окремі елементи з межою розділення "і"
    userInfo[i] = userInfo[i].split("i")

print userInfo
