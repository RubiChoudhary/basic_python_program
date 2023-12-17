punctuation = ''' !@~#$%^&*()_+{}:"<>?><.,;'[]=- '''
string = input("enter paragraph with punctuation: ")
blank = ""
for i in string:
    if i not in punctuation:
        blank= blank + i
print(blank)
