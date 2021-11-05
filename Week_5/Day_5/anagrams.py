from Anagram_Checker import AnagramChecker


def is_word_valid(word):
    return len(word.split()) == 1 and word.isalpha()


while True:
    user_choice = input('A. Find a word\'s anagrams\nX. Exit\n')
    if user_choice in 'xX':
        print('Goodbye')
        break
    elif user_choice.upper() == 'A':
        selected_word = input('give us the word to check for anagrams\n')
        if is_word_valid(selected_word):
            clean_word = selected_word.strip()
            a = AnagramChecker()
            anagrams = a.get_anagrams(clean_word)
            msg = f'''YOUR WORD :"{clean_word}"
this is a valid English word.
Anagrams for your word:'''
            print(msg, *anagrams)
        else:
            print('not a valid word')
