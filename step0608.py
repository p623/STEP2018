def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def readStartKakko(line,index):
    token = {'type': 'START'}
    return token, index + 1

def readFinishKakko(line,index):
    token = {'type': 'FINISH'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)
        elif line[index] == '(':
            (token, index) = readStartKakko(line, index)
        elif line[index] == ')':
            (token, index) = readFinishKakko(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def evaluateKakko(tokens):
    while True:
        index=0#"("と")"がどこにあるのかその都度調べる
        startKakkoIndex=[]
        finishKakkoIndex=[]
        finishKakkoIndexMinusA=[]
        while index < len(tokens):
            if tokens[index]["type"]=="START":
                startKakkoIndex.append(index)
            elif tokens[index]["type"]=="FINISH":
                finishKakkoIndex.append(index)
            else:
                pass
            index+=1
        if startKakkoIndex==[] or finishKakkoIndex==[]:#括弧がない時にはbreak
            break
        else:
            tokensForKakko=[]#括弧の中身の計算のためのtokens
            calculateStartKakko=max(startKakkoIndex)#より内側の括弧から計算するためのa,bを考える
            for element in finishKakkoIndex:#一番後ろの(から始まる()の計算をするために一番後ろの(のちょっと後ろのIndexの)を探す
                if element-calculateStartKakko>0:
                    finishKakkoIndexMinusA.append(element-calculateStartKakko)
            calculateFinishKakko=min(finishKakkoIndexMinusA)+calculateStartKakko
            indexForKakko=calculateStartKakko+1
            while indexForKakko < calculateFinishKakko:#目的の括弧の中身をtokensForKakkoに追加
                tokensForKakko.append(tokens[indexForKakko])
                indexForKakko+=1
            #tokensForKakkoの中身に対して四則演算を実行、)の一つ前のtokensの要素をその値で更新
            tokens[calculateFinishKakko-1]["number"]=evaluatePlusAndMinus(evaluateMultiplyAndDivide(tokensForKakko)) #[(][2][-][1][)]=[(][null][null][1][)]に
            #[(][null][null]と[)]の消去
            del tokens[calculateStartKakko:calculateFinishKakko-1]
            del tokens[calculateStartKakko+1]
    return tokens


def evaluateMultiplyAndDivide(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                tokens[index]["number"]=tokens[index-2]["number"]*tokens[index]["number"] #[4][*][2]=[null][null][8]に
                del tokens[index-1] #上の[null][null]を消去
                del tokens[index-2]
                index=1 #tokensの要素数を減らしてしまったのでindexの初期化

            elif tokens[index - 1]['type'] == 'DIVIDE':
                if tokens[index]["number"]==0: #0で割られれた時のエラー
                    print("ZeroDivisionError")#"ZeroDivisionError"を表示
                    tokens=[]#"ZeroDivisionError"の時はAnswer=0を返す
                    break
                else:
                    tokens[index]["number"]=tokens[index-2]["number"]/tokens[index]["number"] #[4][/][2]=[null][null][2]に
                    del tokens[index-1] #上の[null][null]を消去
                    del tokens[index-2]
                    index=1 #tokensの要素数を減らしてしまったのでindexの初期化
            else:
                pass
        index += 1
    return tokens

def evaluatePlusAndMinus(tokens):
    answer = 0
    index = 1 #tokensの[*][/]の処理が終わったところで[+][-]の処理を開始
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number'] 
            else:
                print('Invalid syntax')
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluatePlusAndMinus(evaluateMultiplyAndDivide(evaluateKakko(tokens)))
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("2*3",6)
    test("4/2",2)
    test("4/2*3",6)
    test("1.0+2.1/3*0.7-0.3",1.19)
    test("6*3/2-3+4",10)
    test("28/7*8/16+5-1",6)
    test("0-3*6",-18)
    test("0-3*2+4/2-5.0-6.0/2+72/2.0",24)
    test("2",2)
    test("3/0-2+3*4+6*2",0)
    test("",0)
    test("4*(2-1)",4)
    test("(3+4*(2-1))/5",1.4)
    test("(3+4*(2-1)+(4+2)/2)/5",2)
    test("(1)",1)
    test("(1+2)",3)
    test("2*(3+4)",14)
    test("(2+3)*4",20)
    test("((1))",1)
    test("((1+2)*(3+4))",21)
    test("(1+2)*(3+4)",21)
    test("1-(2-3)",2)
    test("1-(2-(3-4))",-2)
    test("1-(2-(3-(4-5)))",3)
    test("1-(2-(3-(4-5)-6))",-3)
    test("1-(2-(3-(4-5)-6)-7)",4)
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ',)
    line = input()
    tokens = tokenize(line)
    answer=evaluatePlusAndMinus(evaluateMultiplyAndDivide(evaluateKakko(tokens)))
    print("answer = %f\n" % answer)