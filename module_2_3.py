# while 1 > 0: # True #Условие выполнения цикла
#     # пока условие правдиво цикл будет повторяться
#     number = int(input("Введите число: "))
#     if number % 2 == 0:
#         print("Число чётное")
#         continue # Пропускает выполнение последующих операций если условие выполнено и переходит на след. Повтор цикла
#     else:
#         print("Число нечётное")
#         # break #останавливает цикл после выполнения в данном случае ==>else<==
#     print("Меня не забыли")
# print("Я за циклом")  # Программа до нее не доходит
# ======================================================================================================================


numbers =[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0

while counter < len(numbers): #and numbers == 0:
    if numbers[counter] == 0:
        counter += 1
        continue
    elif numbers[counter] < 0:
        break
    print(numbers[counter])
    counter += 1


    # print(my_list[counter])

    # show_number = my_list[counter]






    # elif my_list[counter] == 0:
    #     continue
    #     print(my_list[counter])

    #
    # print(f"Сейчас в счётчике цифра {counter}")
    # print(f"с помощью счётчика берём букву {text[counter]}")
    # print(f"с помощью счётчика берём цифру {numbers[counter]}")
    # counter += 1