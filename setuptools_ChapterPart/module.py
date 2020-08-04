import random

def shuffle_text(text):
    # In the book there was some code for this function with 'german' variables, but I decided to make my own function once I understood what it does
    text_list = text.split(" ")
    shuffled_word_list = list() 
    
    for word in text_list:
        if len(word) >= 4:
            word = list(word)
            in_between_words = word[1:-1]
            random.shuffle(in_between_words)
            shuffled_word_list.append("{0}{1}{2}".format(
                word[0],
                "".join(in_between_words),
                word[-1]
            ))
        else:
            shuffled_word_list.append(word)

    return "".join(shuffled_word_list)

text = "Hello world, this is Python 3"
print(shuffle_text(text))
