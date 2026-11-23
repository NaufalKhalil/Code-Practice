terlarang = [
    "bodoh", "jelek", "nigga", "jawa", 
    "anjing", "babi", "bangsat", "keparat", 
    "goblok", "tolol", "bego", "setan", "fuck",
    "shit", "asshole", "bitch", "bastard", "suck",
    "crap", "idiot", "noob",
]

text = input("Chat :")
text = text.split()

sudah_tampil = []

total = 0

for i in range(len(text)):
    if text[i] in terlarang and text[i] not in sudah_tampil:
        print(text[i])
    if text[i] in terlarang:
        total += 1
    sudah_tampil.append(text[i])
    

print(f"Total kata terlarang yang di temukan = {total}")