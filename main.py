from logic import *

dictionary_for_repeat=''
keys=''
if __name__ == "__main__":
    dictionary_of_all_words=get_words()
    lenght_of_output=int(input("Enter number of words: "))
    for i in range(lenght_of_output):
        key=get_number_of_word(dictionary_of_all_words, keys)
        keys+=str(key)
        print(dictionary_of_all_words[key])
        dictionary_for_repeat+=dictionary_of_all_words[key]+'splitkey'
        time_stop(5)
    dictionary_for_repeat=dictionary_for_repeat[:-8].split('splitkey')
    print("Let's repeat this words...\n")
    time_stop(2)

    random.shuffle(dictionary_for_repeat)
    for i in range(lenght_of_output):
        right_answers=0

        word=str(dictionary_for_repeat[i])
        print('How to translate this word? ', word[word.find(']')+3:])
        right_guess=word[:word.find('[')-1]
        guess=str(input())
        if guess == right_guess.strip():
            right_answers+=1    
    mark=get_mark(right_answers, lenght_of_output)
    print(mark)