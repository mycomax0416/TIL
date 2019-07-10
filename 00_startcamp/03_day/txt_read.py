# read() : 개행문자를 포함한 하나의 문자열
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)

# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list 로 만들어냄
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        # line 'This is line 1\n'
        # print(\n)
        # '문자열'.strip() 개행문자를 다 지워줌
        # print(dir(line)): line 뒤에 사용할 수 있는 명령어를 다 찾아줌.(dir)