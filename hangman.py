import random
def hangman():
    list1=["chandni","rachu","neha","india","pakistan","gues","hangman","mango"]
    word=random.choice(list1)
    time=10
    str=''
    v=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        m_word=""
        for letter in word:
            if letter in str:
                m_word=m_word+letter
            else:
                m_word=m_word+"_ "
        if m_word==word:
            print(m_word)
            print(" ** you won!!!!!*")
            break
        print("guess the word",m_word,)
        guess=input()
        if guess in v:
            str=str+guess
        else:
            print("enter velid charracter")
            guess=input()
        if guess not in word:
            time=time-1
            if time==9:
                print("8time is left!!!!!!")
                print("-------------")
            if time==8:
                print("6 time is left!!!!!!")
                print("   o     ")
            if time ==7:
                print("6 time is left!!!!!!")
                print("   o    ")
                print("   |   ")
            if time ==6:
                print("5 time is left!!!!!!")
                print("   o    ")
                print("   |   ")
                print("  /   ")
            if time ==5:
                print("4  time is left!!!!!!")
                print("   o    ")
                print("   |   ")
                print("  / \  ")
                
            if time ==4:
                print("3 time is left!!!!!!")
                print("  \o    ")
                print("   |   ")
                print("  / \  ")
            if time ==3:
                print("2 time is left!!!!!!")
                print("  \o/   ")
                print("   |   ")
                print("  / \  ")
            if time ==2:
                print("1 time is left!!!!!!")
                print("  \o/ |  ")
                print("   |   ")
                print("  / \  ")
            if time ==1:
                print("only one trun is left")
                print("  \o/__|")
                print("   |   ")
                print("  / \  ")
            if time ==0:
                print("ooppssss sorrry you loss")
                break
name=input("enter your name")
print("WELCOME",name)
print("try to guess the words less then 10 times")
hangman()