sentence = "Hello world this is ChatGPT"
words = sentence.split()        # Split sentence into words
reversed_words = words[::-1]    # Reverse the list of words
reversed_sentence = " ".join(reversed_words)  # Join back into a string

print(reversed_sentence)
