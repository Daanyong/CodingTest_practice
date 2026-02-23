# 입력: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄에는 수를 공백으로 구분하여 N개 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# 출력: 입력으로 주어진 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력한다.
# 풀이: 계수 정렬을 사용하여 수의 등장 횟수를 기록한 후, 등장 횟수에 따라 수를 출력하는 방식으로 문제를 해결한다. 계수 정렬은 입력된 수의 범위가 제한적일 때 효율적으로 사용할 수 있는 정렬 알고리즘이다.
# 시간 복잡도: O(N + K), 여기서 N은 입력된 수의 개수, K는 수의 최대값(1000)이다. 공간 복잡도: O(K)이다.

import sys #sys.stdin.readline(), sys.stdout.write() 등 빠르게 입출력하기 위해 sys 모듈 사용

N = int(sys.stdin.readline())  # 첫 번째 줄에서 수의 개수 N을 입력받음
count = [0] * 1001 # 0부터 1000까지의 수가 등장할 수 있으므로, 각 수의 등장 횟수를 저장하기 위한 리스트 count를 초기화
numbers = list(map(int, sys.stdin.readline().split())) # 두 번째 줄에서 N개의 수를 입력받아 리스트 numbers에 저장. map(int, ...)을 사용하여 입력된 문자열을 정수로 변환

for number in numbers: 
    count[number] += 1 # count 리스트에서 해당 숫자의 인덱스에 1을 더하여 등장 횟수를 기록

for i in range(1001):
    if count[i] != 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i) + ' ') # count[i]가 0이 아닌 경우, 해당 숫자 i를 count[i]번 출력. sys.stdout.write()를 사용하여 빠르게 출력