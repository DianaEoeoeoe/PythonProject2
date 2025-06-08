try:
    user = input("введіть число.. ")
    number = int(user)
    print(F"ви ввели ціле число... {number}")
except ValueError:
    print("введене значення не можнщ конвертувати в ціле число")