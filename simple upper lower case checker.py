enter = input('Please input a word: ')

#lower case
if enter == enter.lower():
    print("The word you enter is in lower case")
#Upper case
elif enter == enter.upper():
    print("The word you enter is in upper case")
#Lower case & Upper case combine
else:
    print("The word you enter is in both upper and lower case")