# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')

class Text:
    def __init__(self, string):
        self.content = string
        self.word_list = self.content.split()
        self.unique = set(self.word_list)

    def word_frequency(self, word):
        '''return a nicely formatted sentence with the frequency of a word in the text or None if not found'''
        freq = self.__word_frequency(word)
        if freq:
            return f'the word "{word}" shows up {freq} times in the current text'

    def __word_frequency(self, word):
        '''return the frequency of a word in the text or None if not found'''
        if word in self.word_list:
            return self.word_list.count(word)

    def most_common_word(self):
        word_dict = list({word: self.__word_frequency(word)
                         for word in self.unique}.items())
        return sorted(word_dict, key=lambda x: x[1])[-1][0]

    def unique_words(self):
        return list(self.unique)

    @classmethod
    def from_file(cls, file_name):
        '''returns a Text instance but with a text file'''
        with open(file_name, 'r') as f:
            file_text = f.read()
        return cls(file_text)


my_text = Text('hello world hello hello hello goodbye world')
print(my_text.word_frequency('world'))
print(my_text.most_common_word())

strange = Text.from_file('the_stranger.txt')
# print(strange.unique_words())
print(strange.most_common_word())
