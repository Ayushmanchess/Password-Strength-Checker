import time

def password_cracker(password):
    start_time = time.time()
    dictionary = ["A", "a", "B", "b", "C", "c", "D", " ", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W",
                  "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "@", "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "|", ":", ";", "\"", "'", ",", "<", ".", ">", "/", "?", "`", "~"]
    letter = []
    p_word = password
    for x in range(0, len(p_word)):
        for y in range(0, len(dictionary)):
            if p_word[x] == dictionary[y]:
                letter.append(dictionary[y])
                print(letter)

            else:
                print(letter)

    print(letter)
    endtime = time.time()
    elapsedtime = endtime - start_time
    print("That took " + str(elapsedtime) + " seconds to crack the password") 
                
print("Welcome to the Password Strength Checker!")
print("This tool helps you see how long it takes to crack a password")

password = input("What is the password you want to crack? ")
password_cracker(password)


