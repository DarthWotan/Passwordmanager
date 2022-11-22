def encoding(word: str) -> bool:
    test = list(word)
    x = 0
    new = []
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ1234567890 !§$%&/()=?`*'+#;:_,.-<>^°'„¡“¶¢[]|{}≠¿'«∑€®†Ω¨⁄øπ•±å‚∂ƒ©ªº∆@œæ‘≤¥≈ç√∫~µ∞…–"  # Zahlen/Buchstaben/Zeichen, die im Text verwendet werden können
    for i in range(len(test)):
        for l in range(len(alphabet)):

            if test[i] == alphabet[l - 1]:
                x = alphabet[l]
                new.append(x)
    return "".join(new)


def decoding(word: str) -> bool:
    test = list(word)
    x = 0
    old = []
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ1234567890 !§$%&/()=?`*'+#;:_,.-<>^°'„¡“¶¢[]|{}≠¿'«∑€®†Ω¨⁄øπ•±å‚∂ƒ©ªº∆@œæ‘≤¥≈ç√∫~µ∞…–"
    for i in range(len(test)):
        for l in range(len(alphabet)):
            if test[i] == alphabet[l - 1]:
                x = alphabet[l - 2]
                old.append(x)
    return "".join(old)


if __name__ == "__main__":
    while True:
        x = encoding(input("Please enter the word: "))
        print(x)
        y = decoding(input("Please enter the word: "))
        print(y)
