terlarang = [
    "bodoh", "jelek", "nigga", "jawa", 
    "anjing", "babi", "bangsat", "keparat", 
    "goblok", "tolol", "bego", "setan", "fuck",
    "shit", "asshole", "bitch", "bastard", "suck",
    "crap", "idiot", "noob",
]

text = input("Chat :")
text = text.split()

for i in range(len(text)):
    if text[i] in terlarang:
        print("*" * len(text[i]), end=" ")
    else :
        print(text[i], end=" ")