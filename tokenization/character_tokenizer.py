word = "hello"

# simple for loop which create a char list
# issue -> the list contains duplicate characters 
# solution -> use set as it contains only unique characters
# now we have to give Token IDS to each unique charactar we encounter and store it somewhere
def char_tokenizer(word : str) -> tuple[list , set]:
    char_list = []
    char_set = set()
    for char in word:
        char_list.append(char)
        char_set.add(char)
    return char_list , char_set

# unpacking the returned tuple
char_list, char_set = char_tokenizer(word)

print(char_list , char_set)