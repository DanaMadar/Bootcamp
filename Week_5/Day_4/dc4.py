import re
import json

# Create a class called Text that takes a string as an argument and store the text in a attribute.


class Text:
    def __init__(self):
        pass

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')
    def ferquence(self):
        frequency = {}
        doc = open('the_stranger.txt', 'r')
        text_str = doc.read().lower()
        pattern = re.findall(r'\b[a-z]{3,15}\b', text_str)
        
        for word in pattern:
            
