import subprocess as sp

msg=''

def input_tweet():
    global msg
    msg = input("Enter tweet in 280 characters only: ")
    if len(msg)>280:
        print("Text exceeded 280 characters. Shorten it!")
        input_tweet()

file = open('cred.tfuc', 'r')
content = file.readlines()

input_tweet()

for i in range(0, len(content)):
    [usern, psd] = content[i].split(' ')
    psd = psd.split('\n')[0]
    p=sp.Popen(['gnome-terminal','--tab','--','./act.sh',usern,psd,msg], stdout= sp.PIPE)
    print(p.communicate())
