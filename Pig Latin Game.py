def main():
    lst = ['ch', 'ph', 'sl', 'gl', 'fl', 'pl', 'st', 'sm', 'tr', 'sr','cl', 'bl']
    sentence = input("Type what you would like to translate into pig-latin and press ENTER: ")
    sentence = sentence.split()
    for k in range(len(sentence)):
        i = sentence[k]
        if i[0] in ('a', 'e', 'i', 'o', 'u'):
            sentence[k] = i + 'ay'
        elif t(i) in lst:
            sentence[k] = i[2:] + i[:2] + 'ay'
        elif i.isalpha()==False:
            sentence[k] = i
        else:
            sentence[k] = i[1:] + i[0] + 'ay'
        return ' '.join(sentence)
def t(str):
    return str[0] + str[1]
if __name__=='__main__':
    x = main()
    print(x)
