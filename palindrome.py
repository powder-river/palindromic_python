import re
# blue = "Blue!"
# print(blue)
# blue = blue.lower()[::-1]
# print(blue)
# blue = re.sub(r'\W',"", blue)
#
# print(blue)
def is_palindrome(user_string):
    # todo: return True or False if the sentence is or isn't a palindrome
    user_string = user_string.lower()
    user_string = re.sub(r'\W',"", user_string)
    reverse_string = user_string[::-1]
    print(reverse_string)
    if user_string == reverse_string:
        return True

    else:
        return False

def main():
    word = input("Enter a word and see if it is a palindrome\n")
    if is_palindrome(word) == True:
        return "Your Sentance is a palendrome"
    else:
        return "nope"

if __name__ == '__main__':
    main()
