import re

word = input("Enter a word and see if it is a palindrome\n")
def is_palindrome(user_string):
    # todo: return True or False if the sentence is or isn't a palindrome
    user_string = user_string#.lower()[::-1]
    match = re.search(r'[a-z A-Z]*', user_string)
    return(user_string)
    if user_string != match:
        pass
        return False
    
    return True
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
