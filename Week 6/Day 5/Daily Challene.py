

word = input('Enter a word\n')
encrypt = input("Do you want to encrypt ?\n")
shift = int(input("what shift do you want to use for encryption ?\n"))
final_word = ''


if encrypt == "yes":
    for letter in word:
    num = ord(letter)
    let = chr(num + shift)
    final_word += let

else:
    print("okay")

print(f"The encrypted word is {final_word}")
decrypt = input("do you want to decrypt ?\n")

if decrypt == "yes":
    print(f"The original word was {word}")
else:
    print("no prob")
