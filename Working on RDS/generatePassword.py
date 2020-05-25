
def encryptPassword(password):
    password=password.lower()
    f = open('Lookup.txt')
    string=''
    for i in password:
        f.seek(0,0)
        for j in f.readlines():
            if(i==j[0]):
                j=j.rstrip()
                string+=j[2:]
    return string


def decryptPassword(password):
    f = open('Lookup.txt')
    string=''
    count=0
    while(count<len(password)):
        encryptedLetter=str(password[count])+str(password[count+1])
        count+=2
        f.seek(0,0)
        for j in f.readlines():
            j = j.rstrip()
            if(encryptedLetter==j[2:]):
                string+=j[0]
    return string
