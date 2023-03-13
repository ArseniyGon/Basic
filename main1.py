# # import csv
# # import pickle
# # FILENAME = "user.dat"
# #
# # users = [
# #     ["Tom", 23, "male", "married", 60000],
# #     ["Bob",20],
# #     ["John",30]
# # ]
# #
# # with open(FILENAME, "wb") as file:
# #     pickle.dump(users[0][0], file)
# #     pickle.dump(users[0][1], file)
# #
# # with open(FILENAME, "rb") as file:
# #     name = pickle.load(file)
# #     age = pickle.load(file)
# #     print(name)
# #     print(age)
# #
# #
# #
# #
# #
# #
# # # print(users[0][1])
# # #
# # # users = [
# # #     {"name": "Tom", "age": 28},
# # #     {"name": "Bob", "age": 20},
# # #     {"name": "John", "age": 30}
# #
# # # ]
# #
# # # with open(FILENAME, "r", newline="") as file:
# #     # writer = csv.writer(file)
# #     # writer.writerows(users)
# #     # # writer.writerow(users[1])
# #     # reader = csv.reader(file)
# #     # for x in reader:
# #     #     print(x[0])
# #
# # # with open(FILENAME, "w", newline="") as file:
# # #     columns = ["name", "age"]
# # #     writer = csv.DictWriter(file, fieldnames=columns)
# # #     writer.writeheader()
# # #     writer.writerows(users)
# # #
# # # with open(FILENAME, "r", newline="") as file:
# # #     reader=csv.DictReader(file)
# # #     for x in reader:
# # #         print(x["name"] + " " + x["age"])
# #
# #
# import os
# # os.mkdir("hello")
# # os.rmdir("hello")
# # os.rename("dec.py", "newdec.py")
# if os.path.exists("newdec.py"):
#     os.rename("newdec.py", "dec.py")
#     print("exists")
# else:
#     print("does not exist")
#

import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


# ['123456', '123456', '123456', '123456', '123456123456', '5432211', '5432211', '5432211']
def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


print(get_words("trial.txt"))
if __name__ == "__main__":
    main()
