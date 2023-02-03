def stem_prefix_suffix(word):
    prefixes = ["የ", "ለ", "አል", "በ", "ሳይ", "አት", "አስ", "እንደ", "እስኪ", "ያል", "ባለ", "እንዲ", "እያስ", "በስተ", "ወደ", "ያስ", "ት", "ስለ", "እስክ", "ሲ", "እንድ","አስ", "ምት", "በስተ", "ወደ", "ያለ", "ማይ", "የ", "ሳት","ያስ", "እንዲ", " ት", "ያ", "አላ", "እስከ", "በ", "ተ", "ት", "ሚ", "እን", "በት", "ከ", "ተ", "ወ", "አይ", "የ"]
    suffixes = ["ን", "ና", "ሽ", "ነት","ሽው", "ው","ዮሽ", "ቸው", "ህ", "ባት", "ዋ", "ችኋል", "ዎች", "ም", "ለን", "ለት", "ዊ","ቹ", "ውያን", "ዎች", "ዋ", "ኝ", "ኞች", "ያ", "ችን", "ቸው","ች", "ቸው" "ዊ", "በት", "ችሁ", "ዋ", "ን", "ህ","ኛ", "አቸዋል","አችን","ቹ", "ችሁ", "ውያን", "ቻቸው", " ይ", "ቸው", "ህ", "ኞቸ", "ለ", "ት"]

    word=word.replace("ሠ","ሰ")
    word=word.replace("ሃ", "ሀ")
    word=word.replace("ሐ", "ሀ")
    word=word.replace("ሓ", "ሀ")
    word=word.replace("ኅ", "ሀ")
    word=word.replace("ኃ", "ሀ")
    word=word.replace("ኋ", "ኋ")
    word=word.replace("ሗ", "ኋ")
    word=word.replace("ኁ", "ሁ")
    word=word.replace("ኅ", "ህ")
    word=word.replace("ኂ", "ሂ")
    word=word.replace("ኄ", "ሄ")
    word=word.replace("ሑ", "ሁ")
    word=word.replace("ሒ", "ሂ")
    word=word.replace("ሔ", "ሄ")
    word=word.replace("ሕ", "ህ")
    word=word.replace("ሡ", "ሱ")
    word=word.replace("ሖ", "ሆ")
    word=word.replace("ሢ", "ሲ")
    word=word.replace("ሣ", "ሳ")
    word=word.replace("ሤ", "ሴ")
    word=word.replace("ሥ", "ስ")
    word=word.replace("ሦ", "ሶ")
    word=word.replace("ጸ", "ፀ")
    word=word.replace("ጹ", "ፁ")                    
    word=word.replace("ጺ", "ፂ")
    word=word.replace("ጻ", "ፃ")
    word=word.replace("ጼ", "ፄ")
    word=word.replace("ጽ", "ፅ")
    word=word.replace("ጾ", "ፆ")
    word=word.replace("ዉ", "ው")
    word=word.replace("ዪ", "ይ")
    word=word.replace("ዓ", "አ")
    word=word.replace("ዑ", "ኡ")
    word=word.replace("ዒ", "ኢ")
    word=word.replace("ዐ", "አ")
    word=word.replace("ኣ", "አ")
    word=word.replace("ዔ", "ኤ")
    word=word.replace("ዕ", "እ")
    word=word.replace("ዖ", "ኦ")

    if word.startswith('አ') and word.endswith('ጥ'):
        word = word[:-1] 
        if word.startswith('አ'):
             word = word[1:]
             return word
    if word.startswith('አ') and word.endswith('ል'):
        word = word[:-1] 
        if word.startswith('አ'):
             word = word[1:]
             return word
    if word.startswith('አ') and word.endswith('ብ'):
        word = word[:-1] 
        if word.startswith('አ'):
             word = word[1:] 
             return word
    if word.startswith('አስ') and word.endswith('ች'):
        word = word[:-1] 
        if word.startswith('አስ'):
             word = word[2:]
             return word
                     

    elif word.endswith('ጆች'):
        word = word[:-2] + 'ጅ'
        return word
    elif word.endswith('ቶች'):
        word = word[:-2] + 'ት'
        return word
    elif word.endswith('ኞች'):
        word = word[:-2] + 'ኛ'
        return word
    elif word.endswith('ጎች'):
        word = word[:-2] + 'ግ'
        return word

    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):]  
            break

    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break
    return word



sentence = input("Enter a sentence: ")
words = sentence.split()
stemmed_words = [stem_prefix_suffix(word) for word in words]
print("Stemmed sentence:", " ".join(stemmed_words))
