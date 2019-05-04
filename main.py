import sys
from collections import Counter

def str_norm(line):
    symbols = ['.' , ',', ':', ';', '!', '?',
                '(', ')', '%', '[', ']', '{',
                '}', '\t', '@', '#', '&', '\\', 
                '/', '<', '>', '+', '=', '-', '–', 
                '_', '\'', '\"', '…', '«', '»']
    for i in symbols:
        line = line.replace(i, ' ')
    return line.lower()

def total(word_dict):
    num = 0
    for value in word_dict.values():
        num += value
    return num

def print_result(sorted_dict, word_dict, in_file=False, frequence_count=0):
    if in_file == True:
        with open('analysis.txt', 'w') as file:
            file.write("Total count - {}\nWord frequency analysis:\n".format(total(word_dict)))
            for i in sorted_dict:
                if i[1] > frequence_count:
                    file.write("   {} - {}\n".format(i[0], i[1]))
        print("Result has been written in analysis.txt")

    else:
        print("Total count - {}\nWord frequency analysis:".format(total(word_dict)))
        for i in sorted_dict:
            if i[1] > frequence_count:
                print("   {} - {}".format(i[0], i[1]))

def main(word_len):
        word_dict = dict()
        with open(sys.argv[6], 'r') as fd:
            for line in fd:
                line = str_norm(line).split()
                for word in line:
                    if len(word) > word_len:
                        if word not in word_dict:
                            word_dict[word] = 1
                        else:
                            word_dict[word] += 1
        sorted_dict = Counter(word_dict).most_common()
        if sys.argv[1] == '-t':
            print_result(sorted_dict, word_dict, False, int(sys.argv[5]))
        elif sys.argv[1] == '-f':
            print_result(sorted_dict, word_dict, True, int(sys.argv[5]))

if __name__ == '__main__':
    if len(sys.argv) == 7:
        main(int(sys.argv[3]))
    else:
        print("\tusage: python3 main.py [-f (in file) | -t (to terminal)] [-w [minimal word length]] [-c [word frequence count]] [file]")