word = input("Enter a word and see if it is a palindrome")
def is_palindrome(sentence):
    # todo: return True or False if the sentence is or isn't a palindrome
    array = []
    backwards = sentence[::-1]
    if sentence == backwards:
        return True
    else:
        return False

    # pass

print(is_palindrome(word))
# is
# def main():
#     # TODO: put your input/output code here
#     pass
#
#
#     if __name__ == '__main__':
#     main()
