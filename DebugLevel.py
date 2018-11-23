import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt', 'r')# 打开字典文件
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptPass == cryptWord:
            print('Found passed:', word)
            return
        print('Password not found!')
        return


