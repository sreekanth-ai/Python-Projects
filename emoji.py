def emoji_converter(msg):
    word = msg.split(" ")
    emoji = {
        ":)": "😊",
        ":>": "😂",
        ":(": "😒",
        "?": "👍👍"
    }
    output = ""
    for words in word:
        output += emoji.get(words,words) + " "
    return output


msg = input(">")
result = emoji_converter(msg)
print(result)