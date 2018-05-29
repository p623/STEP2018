Ans=[]
point=[]
##16文字の入力を受け取って、"q","u"の入力を"qu"にする
l=list(input("小文字で入力してください"))
i=0
while i<len(l):
    if l[i]=="q":
        l.remove(l[i+1])
        l[i]="qu"
    else:
        pass
    i+=1
##入力された文字をアルファベット順にする
l.sort()

##辞書にある全ての単語について"q","u"の入力を"qu"にする
dictionaryWords=open("dictionary.words.txt","r")
for line in dictionaryWords:
    ##rstripで変な空白を消す
    k=list(line.rstrip())
    m=0
    while m<len(k):
        if k[m]=="q":
            k.remove(k[m+1])
            k[m]="qu"
        else:
            pass
        m+=1
##Aは今調べてる単語
    A=""
    pt=0
    for K in k:
        K.lower
        A+=K
        ##単語Aのそれぞれの文字が何ポイント得られるのか計算
        forpt={"j":3,"k":3,"qu":3,"x":3,"z":3,"c":2,"f":2,"h":2,"l":2,"m":2,"p":2,"v":2,"w":2,"y":2}
        if K in forpt:
            pt+=forpt[K]
        else:
            pt+=1
    ##単語Aに含まれている文字をアルファベット順にする   
    k.sort()

    ##li=l
    li=[]
    for lis in l:
        li.append(lis)
    ##単語Aに含まれている文字が入力した文字群(l)に含まれているか
    ##それぞれアルファベット順に並べているのでFalseの時、早めにFalseと決まる(?)
    ##xを使うことでlにある数だけ、重複してる文字を使えるようになった(と思う)
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

##for astronomer -> moon starerを考えてみる
##コードもコメントの形式で以下に記す
##単語の組み合わせが意味を持つとは限らないのが難点
##これだと二つの単語の組み合わせしかできない
#Ans2=[]
#Ans2Point=[]

##word1 + word2 に含まれる文字が入力した文字列に全て含まれていればok
#for word1 in Ans:
    #for word2 in Ans[Ans.index(word1):]:##これがうまく動いているか不明
        #wdzpt=0
        #j=0
        #words=word1+word2
        #l2=list(words)
        ##アルファベット順に
        #l2.sort()
        ##各単語に対してポイントを計算する関数を定義しとけばここの記述の重複はなくなる
        ##今回はおまけで考えてみただけなので、重複させたままに
        #for wd in l2:
            #forpt={"j":3,"k":3,"qu":3,"x":3,"z":3,"c":2,"f":2,"h":2,"l":2,"m":2,"p":2,"v":2,"w":2,"y":2}
            #if wd in forpt:
                #wdzpt+=forpt[wd]
            #else:
               #wdzpt+=1
        ##以下のシステムは一つの単語を調べる上述のシステムとほぼ一緒
        ##li=l
        #li=[]
        #for lis in l:
            #li.append(lis)

        #j=0
        #for moj in l2:
            #if moj in li:
                #j+=1
                #if j==len(l2):
                    #Ans2.append(word1+" "+word2)
                    #Ans2Point.append((wdzpt+1)*(wdzpt+1))   
                #else:
                    #li.remove(moj)
            #else:
                #break

##単語AとAを入力したことで得られる点数を紐付ける
dic={}
y=0
while y<len(Ans):
    dic[Ans[y]]=point[y]
    y+=1
##二語からなるものについても同様に
#q=0
#while q<len(Ans2):
    #dic[Ans2[q]]=Ans2Point[q]
    #q+=1

##単語Aと点数のセットを点数の低い順に表示する
sorted_dic=sorted(dic.items(),key=lambda z:z[1], reverse=False)

for z,v in sorted_dic:
    print(z,v)
