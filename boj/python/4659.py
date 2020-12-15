def check_password(password):
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in vowel:
            if i in password:
                break
            elif i == vowel[-1]:
                print("<%s> is not acceptable." %passward)
                return
        for j in range((len(password) - 2)):
            overlap_count = 0
            for k in vowel:
                overlap_count += password[j:j+3].count(k)
            if overlap_count == 3 or overlap_count == 0:
                print("<%s> is not acceptable." %passward)
                return
        for l in range((len(password) - 1)):
            if passward[l] == password[l+1]:
                if passward[l] != 'e' and passward[l] != 'o':
                    print("<%s> is not acceptable." %passward)
                    return
        print("<%s> is acceptable." % passward)

if __name__ == "__main__":
    while True:
        passward = input()
        if passward != 'end':
            check_password(passward)
        else:
            break