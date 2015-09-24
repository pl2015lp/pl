#Представити прізвище, ім'я та по батькові як список стрічок. Розділити речення на мокремі елементи, межа рорзділу голосна
буква

userInfo = ["Olya", "Savitska", "Yuriivna"]
for i in range(len(userInfo)):
    # заміняємо слово на окремі елементи з межою розділення "і"
    userInfo[i] = userInfo[i].split("i")
print userInfo
[['Olya'], 'Savitska', 'Yuriivna']
[['Olya'], ['Sav', 'tska'], 'Yuriivna']
[['Olya'], ['Sav', 'tska'], ['Yur', '', 'vna']]
