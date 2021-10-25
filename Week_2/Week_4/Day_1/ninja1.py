# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)


#ex4
# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# print(len(my_text))

#ex5
longst_sentence = ""

i = 1
while i < 6:

    sentence = input("give me the longest sencens you can think of without the letter 'a'\n")
    
    if "a" in sentence:
      print("No 'a's I said!")

    if len(longst_sentence) < len(sentence):
        longst_sentence += sentence
        print("Congrats! this is the longest santence ever")
    

i += 1

print("this is the longest sentence of them all : ", longst_sentence)