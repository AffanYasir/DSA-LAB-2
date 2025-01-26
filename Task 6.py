with open("input.txt", "r") as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print("Longest Word:", longest_word)
