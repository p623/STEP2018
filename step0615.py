def read_wikiWords():
    wikiWords=[]
    wikiPages=open("pages.txt","r")
    for pageLine in wikiPages:
        Index_wikiWord=pageLine.split()
        wikiWords.append(Index_wikiWord[1])
    # wikiWords=['アンパサンド', '言語', '日本語',...]
    return wikiWords


def wikiWords_Search(inputWord):
    wikiWords=read_wikiWords()
    # wikiWords=['アンパサンド', '言語', '日本語',...]
    if inputWord in wikiWords:
        print("--------------------------------------------------")
        print("'"+inputWord+"'についてのサイトはWikipediaに存在します")
        return wikiWords.index(inputWord)
        # return index of inputWord -> relatedWords_Search
    else:
        print("'"+inputWord+"'についてのサイトはWikipediaに存在しません")
        print("Error")
        return "null"
        

def relatedWords_Search(inputWordIndex):
    if inputWordIndex == "null":
        return "null"
    wordIndexs=[]
    wikiLinks=[]
    relatedWords=[]
    wordlinks=open("links.txt","r")
    for linkLine in wordlinks:
        wordIndex_wikiLink=linkLine.split()
        wordIndexs.append(int(wordIndex_wikiLink[0]))
        wikiLinks.append(int(wordIndex_wikiLink[1]))
    #wordIndexs=[0,0,0,...]
    #WikiLinks=[284171, 955, 591, ...]
    wikiWords=read_wikiWords()
    paramForWordIndexs=0
    while paramForWordIndexs < len(wordIndexs):
        if wordIndexs[paramForWordIndexs] > inputWordIndex:
            break
        elif wordIndexs[paramForWordIndexs] == inputWordIndex:# all links from inputWord ->related words
            relatedWords.append(wikiWords[wikiLinks[paramForWordIndexs]])
        paramForWordIndexs+=1
    print("--------------------------------------------------")
    print(wikiWords[inputWordIndex]+"のサイトから飛べるリンクの一覧を表示します")
    print(relatedWords)
    return relatedWords

def evaluate_Relationship(relatedWords1,relatedWords2):
    matchedNumber=0
    matchedWords=[]
    if relatedWords1=="null" or relatedWords2=="null":
        pass
    elif len(relatedWords1) <= len(relatedWords2):
        for relatedWord1 in relatedWords1:
            if relatedWord1 in relatedWords2:
                matchedNumber+=1
                matchedWords.append(relatedWord1)
        print("--------------------------------------------------")
        print("単語1と単語2のサイトの両方から飛べるリンクの一覧を表示します")
        print("--------------------------------------------------")
        print(matchedWords)
        return 100*matchedNumber/len(relatedWords1)
    else:
        for relatedWord2 in relatedWords2:
            if relatedWord2 in relatedWords1:
                matchedNumber+=1
                matchedWords.append(relatedWord2)
        print("--------------------------------------------------")
        print("単語1と単語2のサイトの両方から飛べるリンクの一覧を表示します")
        print("--------------------------------------------------")
        print(matchedWords)
        return 100*matchedNumber/len(relatedWords2)


    
inputWord1=input("類似性を調べたい単語を入力してください(単語1): ")
inputWord2=input("類似性を調べたい単語を入力してください(単語2): ")

inputWord1_Index = wikiWords_Search(inputWord1)
relatedWords1=relatedWords_Search(inputWord1_Index)

inputWord2_Index = wikiWords_Search(inputWord2)
relatedWords2=relatedWords_Search(inputWord2_Index)

relationship = evaluate_Relationship(relatedWords1,relatedWords2)
print("--------------------------------------------------")
print("類似性は"+str(relationship) +"%です")
