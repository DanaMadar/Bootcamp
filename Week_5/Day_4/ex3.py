# ex1

import json
import random


# def get_words_from_file():
#     file_list = open("random_word_list.txt")
#     lines = []
#     for line in file_list:
#         lines.append(line.strip())
#     return lines


# def get_random_sentence(length):
#     random_sentence = ""
#     get_words = get_words_from_file()
#     random_words = random.choices(get_words, k=length)
#     for word in random_words:
#         random_sentence += word + " "
#     return print(random_sentence.lower())


# length = 0


# def main():
#     print("This program is giving back a random sentence out of a downloaded list.(the sentence doesn't have to make sence)")
#     try:
#         length = input("How many words between 2 and 20 do you want:\n")
#         while not 2 < int(length) < 20:
#             length = input("How many words between 2 and 20 do you want:\n")
#         return int(length)
#     except:
#         print("invalit input. type in a number between 2 and 20")


# length = main()
# get_random_sentence(length)
# get_words_from_file()


# ex2
with open('dict.json', 'r') as f:
    my_data = json.load(f)

print(my_data['company']['employee']['payable'])
test_data = my_data["company"]["employee"]["birthday"] = "10.01.1988"
my_data = "my_data"

with open('dict.json', 'w') as f:
    json.dump(my_data, f, indent=2)  # same as the two lines below
   # my_json_string = json.dumps(my_data, indent=2)
    f.write()
