# 시간 초과의 원인을 찾아 해결하기

# 일반적인 입출력 방식
a = int(input())
print(a)

# 빠른 입출력 방식
import sys
b = int(sys.stdin.readline())
sys.stdout.write(str(b) + '\n') # sys.stdout.write()는 문자열만 출력할 수 있으므로, 정수는 str()로 변환하여 출력