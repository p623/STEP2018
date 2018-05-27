Ans=[]
point=[]
#16文字の入力を受け取って、"q","u"の入力を"qu"にする
l=list(input("小文字で入力してください"))
i=0
while i<len(l):
    if l[i]=="q":
        l.remove(l[i+1])
        l[i]="qu"
    else:
        pass
    i+=1
#入力された文字をアルファベット順にする
l.sort()

#辞書にある全ての単語について"q","u"の入力を"qu"にする
dictionaryWords=open("dictionary.words.txt","r")
for line in dictionaryWords:
    #rstripで変な空白を消す
    k=list(line.rstrip())
    m=0
    while m<len(k):
        if k[m]=="q":
            k.remove(k[m+1])
            k[m]="qu"
        else:
            pass
        m+=1
#Aは今調べてる単語
    A=""
    pt=0
    for K in k:
        K.lower
        A+=K
        #単語Aのそれぞれの文字が何ポイント得られるのか計算
        forpt={"j":3,"k":3,"qu":3,"x":3,"z":3,"c":2,"f":2,"h":2,"l":2,"m":2,"p":2,"v":2,"w":2,"y":2}
        if K in forpt:
            pt+=forpt[K]
        else:
            pt+=1
    #単語Aに含まれている文字をアルファベット順にする   
    k.sort()

    #li=l
    li=[]
    for lis in l:
        li.append(lis)
    #単語Aに含まれている文字が入力した文字群(l)に含まれているか
    #それぞれアルファベット順に並べているのでFalseの時、早めにFalseと決まる(?)
    #xを使うことでlにある数だけ、重複してる文字を使えるようになった(と思う)
    x=0
    for moji in k:
        if moji in li:
            x+=1
            if x==len(k):
                Ans.append(A)
                point.append(((pt+1)*(pt+1)))
            else:
                
                li.remove(moji)
        else:
            break

#単語AとAを入力したことで得られる点数を紐付ける
dic={}
y=0
while y<len(Ans):
    dic[Ans[y]]=point[y]
    y+=1

#単語Aと点数のセットを点数の低い順に表示する
sorted_dic=sorted(dic.items(),key=lambda z:z[1], reverse=False)

for z,v in sorted_dic:
    print(z,v)
