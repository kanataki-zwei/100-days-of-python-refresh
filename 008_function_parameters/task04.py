# love score
def calculate_love_score(name1,name2):
    combined = name1+name2
    normalised = combined.lower().replace(" ","")
    word1="true"
    word2="love"
    count1 = 0
    count2 = 0
    for char in word1:
        char_count = normalised.count(char)
        count1+=char_count
    for char in word2:
        char_count = normalised.count(char)
        count2+=char_count
    result = int(str(count1)+str(count2))
    print(result)
    return result
    
calculate_love_score("Mary Jane", "Patrick")