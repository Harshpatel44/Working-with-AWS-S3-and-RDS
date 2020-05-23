
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
