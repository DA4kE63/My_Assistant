
from androidhelper import sl4a


import datetime

print("im now  make voice talker ")

speak = sl4a.Android()
def speaker(need):
    speak.ttsSpeak(need)

#hour = int(datetime.datetime.now().hour)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speaker("sir good. morning")
    elif hour >= 12 and hour < 18 :
        speaker(" good.after. noon . sir ")
    else :
        speaker("good. evening . sir")
    speaker(" sir im python. your .assistant.sir how may i help you")
    

wishme()


#inp = speaker(input("plaes enter your wish "))



#print(inp)
"""
speaker("hlw world. mere bhay.")
"""