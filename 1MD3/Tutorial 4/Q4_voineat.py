def main():
    word = input("Please enter a word")
    print(pluralplus(word))
def pluralplus(w):
    if w.endswith('s') or w.endswith('h'):
        return w + 'es'
    elif w.endswith('y'):
        return w[:-1]+'ies'
    else:
        return w+'s'
main()
