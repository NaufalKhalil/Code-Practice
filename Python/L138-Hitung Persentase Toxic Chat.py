terlarang = [
    "bodoh", "jelek", "nigga", "jawa", 
    "anjing", "babi", "bangsat", "keparat", 
    "goblok", "tolol", "bego", "setan", "fuck",
    "shit", "asshole", "bitch", "bastard", "suck",
    "crap", "idiot", "noob",
]

text = input("Chat :")
text = text.split()

total = 0

for i in range(len(text)):

    if text[i] in terlarang:
        print("*" * len(text[i]), end=" ")
        total += 1
    if text[i] not in terlarang:
        print(text[i], end=" ")
    
persentase = (total / len(text)) * 100
persentase = round(persentase, 1)
print()
print("-"*24)
print(f"Total kata : {len(text)}")
print(f"Total kata toxic : {total}")
print(f"Toxic : {persentase} %")