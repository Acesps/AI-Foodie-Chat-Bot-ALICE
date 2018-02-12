import aiml
import datetime
import requests
import json
import os
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
# kernel.verbose(False)
kernel.learn('startup.xml')
kernel.respond("LOAD AIML B")

path=datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
#savePath ='/mnt/E:/AI_chatbot/LOG/' + path + '.txt'
savePath =os.path.join('LOG/' + path + '.txt')

template_save = open(savePath,"w")
template_save.write(path)

apikey = "d2546b7fe80695161745d3d3e274b1ee"
baseURL = "https://api.darksky.net/forecast/" + apikey + "/"
fullURL=baseURL +'17.5443,78.5719'

kernel.setBotPredicate("name", "foodie")
kernel.setBotPredicate("master", "ARS")

def learn():
	req = json.loads(requests.get(fullURL).text) 
	return 'In Bphc, it is {temp} fahrenheit and {cond}'.format(temp=req['currently']['temperature'], cond=req['currently']['summary'])
					
# Press CTRL-C to break this loop
while True:
    inputstr=raw_input(">>>> ")
    curr=datetime.datetime.now().strftime("%H:%M")
    template_save.write(curr + ' User:' + inputstr + '\n')
    outputstr=kernel.respond(inputstr)
    if "weather" in inputstr:
    	outputstr = learn()
    curr=datetime.datetime.now().strftime("%H:%M")
    template_save.write(curr + ' foodie:' + outputstr + '\n')
    print outputstr
    if "bye" in inputstr:
    	break;

template_save.close()
