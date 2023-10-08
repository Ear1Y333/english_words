import random
import time 
from PyPDF2 import PdfReader

def get_words():
    pdfFileObj = open('C:\\Users\\Ear1Y\\python\\words\\english.pdf', 'rb')
    reader = PdfReader(pdfFileObj)
    number_of_pages = len(reader.pages)
    dictionary_of_all_words=""
    for i in range(1, number_of_pages-41):
        page = reader.pages[i]
        text = page.extract_text()
        text=text.split('\n')
        for j in range(len(text)):
            word=str(text[j]).partition(' ')[2].strip()
            dictionary_of_all_words+=word+'\n'

    return dictionary_of_all_words.split('\n')

def get_number_of_word(dictionary_of_all_words, old_keys):
    while True:
        new_key=random.randint(2, len(dictionary_of_all_words))
        if str(new_key) not in old_keys:
            return new_key

def time_stop(seconds):
    return time.sleep(seconds)

def get_mark(r_answers, number_of_words):
    relation=r_answers/number_of_words
    if relation>=0.85:
        output='Amazing, right ' + str(r_answers) + '/' + str(number_of_words)
    elif relation>=0.65:
        output='Fine, right ' + str(r_answers) + '/' + str(number_of_words)
    elif relation>=0.45: 
        output='Avarage mark, right ' + str(r_answers) + '/' + str(number_of_words)
    elif relation>=0.15:
        output='Bad mark, right ' + str(r_answers) + '/' + str(number_of_words)
    else:
        output='Very bad, right ' + str(r_answers) + '/' + str(number_of_words)
    return output