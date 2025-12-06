'''
Write a python function to remove a given word from a list ad strip it at the sametime.
'''

def remove_word_and_strip(words_list, word_to_remove):
    cleaned_list = [item.strip() for item in words_list if item.strip() != word_to_remove]
    return cleaned_list

words = [" apple ", "banana", "   mango", "apple", " grapes "]
result = remove_word_and_strip(words, "apple")
print(result)
