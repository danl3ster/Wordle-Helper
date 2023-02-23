def convert(s):
 
    # initialization of string to ""
    new = ""
 
    # traverse in the string
    for x in s:
        new += x[0]
 
    # return string
    return new

def top_5_guesses(chararr_words,abundancearr,w,s):
    ans = []
    for i in range(len(w)):
        if i == 0:
            ans = investigate_words(chararr_words,abundancearr,w[i],s[i])
            tempwordarr = ans[0]
            tempabundancearr = ans[1]
        else:
            ans = investigate_words(tempwordarr,tempabundancearr,w[i],s[i])
            tempwordarr = ans[0]
            tempabundancearr = ans[1]

    abundance_dict = {}

    for i in range(len(ans)):
        abundance_dict[convert(ans[0][i])] = ans[1][i]

    sortedarr = sorted(abundance_dict.items(), key = lambda x:x[1],reverse=True)

    sortarr = sortedarr[0:4]

    return sortarr

def investigate_words(basearr,abundancearr,wordarr,statearr):

    # e.g wordarr
    # [C,R,A,T,E]
    
    # e.g statearr
    # [1,2,1,1,3]
    #
    # 1 = black (not present)
    # 2 = yellow (present but not that index)    
    # 3 = green (present in that index)
    
    # 1.Filter for words with the green letters in the right spots
    # 2.Filter for words with the yellow letters
    # 3.Filter for words that do not contain black letters   
    # 4.Rank list using abundance from csv
    # 5.Export Top 5 ranked

    greenarr, yellowarr, blackarr = [],[],[]

    for k in range(len(statearr)):
        if statearr[k] == 3:
            greenarr.append(k)
        if statearr[k] == 2:
            yellowarr.append(k)
        if statearr[k] == 1:
            blackarr.append(k)
    
    results = []
    abundance = []

    for i in range(len(basearr)):

        Keepword = True

        if not greenarr == []:
            for j in range(len(greenarr)):
                if not basearr[i][greenarr[j]][0] ==  wordarr[greenarr[j]]:
                    Keepword = False

        if not yellowarr == []:
            for j in range(len(yellowarr)):
                if not convert(basearr[i]).__contains__(wordarr[yellowarr[j]]):
                    Keepword = False
                if basearr[i][yellowarr[j]][0] == wordarr[yellowarr[j]]:
                    Keepword = False

        if not blackarr == []:
            for j in range(len(blackarr)):
                if basearr[i][blackarr[j]][0] ==  wordarr[blackarr[j]]:
                    Keepword = False

        if Keepword:
                results.append(basearr[i])
                abundance.append(abundancearr[i])

    return [results,abundance]