import os
import multiprocessing as mp
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

param = []
for i in range(0, len(content)):
    [usern, psd] = content[i].split(' ')
    psd = psd.split('\n')[0]
    param.append('flooder.py '+usern+' '+psd+' "'+msg+'"')

all_process = tuple(param)

def execute(process):                                                             
    os.system(f'python3 {process}')                                       
                                                                                
                                                                                
process_pool = mp.Pool(processes = 4)                                                        
process_pool.map(execute, all_process)