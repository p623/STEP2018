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

def readKakeru(line, index):
    token = {'type': 'KAKERU'}
    return token, index + 1

def readWaru(line, index):
    token = {'type': 'WARU'}
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
            (token, index) = readKakeru(line, index)
        elif line[index] == '/':
            (token, index) = readWaru(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'KAKERU':
                tokens[index]["number"]=tokens[index-2]["number"]*tokens[index]["number"] #[4][*][2]=[null][null][8]に
                del tokens[index-1] #上の[null][null]を消去
                del tokens[index-2]
                index=1 #tokensの要素数を減らしてしまったのでindexの初期化

            elif tokens[index - 1]['type'] == 'WARU':
                tokens[index]["number"]=tokens[index-2]["number"]/tokens[index]["number"] #[4][/][2]=[null][null][2]に
                del tokens[index-1] #上の[null][null]を消去
                del tokens[index-2]
                index=1 #tokensの要素数を減らしてしまったのでindexの初期化
            else:
                pass
        index += 1

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
    actualAnswer = evaluate(tokens)
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
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ',)
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)