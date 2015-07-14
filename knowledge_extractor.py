import pandas as pd
import re
import nltk
sen = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
num = re.compile(r'[0-9]+(\.[0-9][0-9]?)?',re.M)

loc = "/home/keerthi/Desktop/causal_verb.txt"
main_list=[]
final_list=[]
main1_list=[]
inter_list=[]
main_dict={}
inter_dict={}
l=[]
count=0
#df = pd.read_csv(loc,error_bad_lines = False)

with open("Ollie Output") as f:
    for line in f:
        
        try:
            #inter_dict={}
            if sen.match(line):
                #print line
                count=count+1
                if main_dict:
                    #print main_dict
                    if main_dict["det"]:
                        main_list.append(main_dict)
                main_dict={}
                inter_list=[]
                main_dict[count]=line
            elif num.match(line):
                #print line
                con = line.split(":")
                #print con[1]
                qw = con[1].split(";")
                #print qw
                #print qw[0]
                inter_dict={}  
                inter_dict["confidenceValue"]= con[0]
                inter_dict["entity1"] = qw[0]
                inter_dict["relation"] = qw[1]
                inter_dict["entity2"] = qw[2]
                inter_dict["belongs to"] = count
                #print inter_dict
                inter_list.append(inter_dict)
            #print inter_list

            main_dict["det"]=inter_list   
            print main_dict    
        except:
            print "111111111"
    #print main_list[10]
count={}

for i in main_list:
    try:
        #print len(i["det"])
        for j in range(len(i["det"])):
            
            final = i['det'][j]['confidenceValue']
            #print final[2]
            hi=max(final)
            #print hi
            if final[2] >= hi:
                #print final[2]
                final_list.append(i['det'][j])
                #print len(final_list)
                #print i['det'][j]
                del i['det'][j]
                
            
            #print first
            first = i['det'][j]['entity1']

            if first in count:

                count[first]=count[first]+1
            else:
                count[first]=1

                
    
    except:
        pass
#print main_list


for i in main_list:

    try:
        for j in range(len(i["det"])):
            first = i['det'][j]['entity1']
            maximum = count[first]

            if count[first]> maximum:
                maximum = count[first]

    except:
        pass
    if count[first] == maximum:
        l.append(first)
#print l
     
for i in main_list:

    try:
        
        for j in range(len(i["det"])):
            if not i['det'][j]['entity1'] in l:
                #del i['det'][j]
                #print i['det'][j]
                del i['det'][j]
    except:
        pass
#print "______________________________________________________________________KKKKKKKKKKKKKKKKK_________________________"

#print main_list
for i in main_list:
    #print i

    try:
        
        for j in range(len(i["det"])):
            final_list.append(i['det'][j])

    except:
        pass
#print final_list




from nltk.corpus import wordnet as wn
l=[]
verbs = ["actuate"
,"do"
,"incite"
,"mold"
,"provide"
,"actuates"
,"does"
,"incites"
,"molding"
,"provides"
,"actuating"
,"doing"
,"inciting"
,"molds"
,"providing"
,"affect"
,"effect"
,"increase"
,"motivate"
,"provoke"
,"affecting"
,"effecting"
,"increases"
,"motivates"
,"provokes"
,"affects"
,"effects"
,"increasing"
,"motivating"
,"provoking"
,"breed"
,"effectuate"
,"induce"
,"move"
,"reduce"
,"breeding"
,"effectuates"
,"induces"
,"moves"
,"reduces"
,"breeds"
,"effectuating"
,"inducing"
,"moving"
,"reducing"
,"bring"
,"encourage"
,"influence"
,"obligate"
,"regulate"
,"bringing"
,"encourages"
,"influences"
,"obligates"
,"regulates"
,"brings"
,"encouraging"
,"influencing"
,"obligating"
,"regulating"
,"call forth"
,"engender"
,"initiate"
,"oblige"
,"result"
,"calling forth"
,"engendering"
,"initiates"
,"obliges"
,"resulting"
,"calls forth"
,"engenders"
,"initiating"
,"obliging"
,"results"
,"cause"
,"evoke"
,"inspire"
,"occasion"
,"set up"
,"causes"
,"evokes"
,"inspires"
,"occasioning"
,"sets up"
,"causing"
,"evoking"
,"inspiring"
,"occasions"
,"setting up"
,"compel"
,"facilitate"
,"instigate"
,"persuade"
,"shape"
,"compelling"
,"facilitates"
,"instigates"
,"persuades"
,"shapes"
,"compels"
,"facilitating"
,"instigating"
,"persuading"
,"shaping"
,"complicate"
,"force"
,"kick up"
,"pioneer"
,"solicit"
,"complicates"
,"forces"
,"kicking up"
,"pioneering"
,"soliciting"
,"complicating"
,"forcing"
,"kicks up"
,"pioneers"
,"solicits"
,"decide"
,"get"
,"kill"
,"play"
,"spawn"
,"decides"
,"gets"
,"killing"
,"playing"
,"spawning"
,"deciding"
,"getting"
,"kills"
,"plays"
,"spawns"
,"decrease"
,"has"
,"lead"
,"promote"
,"stimulate"
,"decreases"
,"have"
,"leading"
,"promotes"
,"stimulates"
,"decreasing"
,"having"
,"leads"
,"promoting"
,"stimulating"
,"determine"
,"impel"
,"let"
,"prompt"
,"suborn"
,"determines"
,"impelling"
,"lets"
,"prompting"
,"suborning"
,"determining"
,"impels"
,"letting"
,"prompts"
,"suborns"
,"dictate"
,"impose"
,"make"
,"propel"
,"dictates"
,"imposes"
,"makes"
,"propelling"
,"dictating"
,"imposing"
,"making"
,"propels"]

        
for tokens in verbs:
    if tokens not in l:
        l.append(tokens)
    for ss in wn.synsets(tokens,pos=wn.VERB):
        #print ss.name
        for every in ss.lemmas():
            #print every.name()
        #print ss
            if every.name() not in l:
                l.append(every.name())
            for sim in every.similar_tos():
                #print('    {}'.format(sim))
                if sim not in l:
                    l.append(sim)
#print (l)
#print len(l)
THE_list = []
for i in final_list:
    #print i["relation"]
    try:
        
        hybrid = i['relation']
        #print hybrid
        tokenss = nltk.word_tokenize(hybrid)
        #print type(tokenss)
        for each in tokenss:
            #print each
            if each in l:
                THE_list.append(i)
                
    except:
        print "EEEEERRRRRRRRRRRRRRROOOOOOOOOORRRRRRRRRR"
#print THE_list
the_dict = {}
THE_dict = {}
lists = []
b3=[]
for every in THE_list:
    b2 = every["belongs to"]
    if b2 not in b3:
        b3.append(b2)
   

    the_dict["entity1"] = every["entity1"]
    #print the_dict["entity1"]
    the_dict["relation"] = every["relation"]

    the_dict["entity2"] = every["entity2"]
    lists.append(the_dict.copy())


    
    for i in main_list:
        try:
            for j in range(len(main_list)):
                if j in b3 and i[j]:
                    THE_dict["sentence"]=i[j]
                    
                    
            #print high
        except:
            pass
            #print i[b2]
        
    
            
    THE_dict["ERE"]=lists
print THE_dict["ERE"]
#print len(b3)
        
        
                
            
            
