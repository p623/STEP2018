import itertools
print("n×nの行列の積を計算します")
n = int(input("nの値を入力してください:"))

#n×nの行列の生成
a = [[1 for i in range(n)] for j in range(n)]
b = [[1 for i in range(n)] for j in range(n)]
c = [[1 for i in range(n)] for j in range(n)]


#行列a,bに値を入力する
list1=range(0,n)
list2=range(0,n)

for A in list1:
    for B in list2:
        a[A][B]=int(input("左から掛ける行列の("+str(A)+","+str(B)+")の値を入力してください"))
print("--------------------------------------------------------------------")
for A in list1:
    for B in list2:
        b[A][B]=int(input("右から掛ける行列の("+str(A)+","+str(B)+")の値を入力してください"))
print("--------------------------------------------------------------------")
print("左から掛ける行列を表示します")
print(a)
print("--------------------------------------------------------------------")
print("右から掛ける行列を表示します")
print(b)

#Σ式の定義
def sigma(frm, to,A,B):
    result=0
    for l in range(frm, to):
        result=result+a[A][l]*b[l][B]
    return result

#行列の計算
for A in list1:
    for B in list2:
        c[A][B]=sigma(0,n,A,B)
print("--------------------------------------------------------------------")
print("計算結果を表示します")
print(c)