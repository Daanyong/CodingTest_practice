# 나머지 연산의 중요성 알아보기

# solution 1: 1부터 100,000까지 곱한 값을 1,000,000,007로 나눈 나머지를 구하는 문제
import time

answer = 1
start = time.time() # 시작 시간 기록
for i in range(1, 100001):
    answer *= i

answer = answer % 1000000007 # 나머지 연산을 통해 결과를 1,000,000,007로 나눈 나머지를 구함
end = time.time() # 종료 시간 기록
print("결과: ", answer)
print("수행 시간: {:.6f}초".format(end - start)) # 소요 시간 출력

# solution 2: 곱셈을 수행할 때마다 나머지 연산을 수행하는 로직
import time

MOD = 1000000007
answer = 1
start = time.time() # 시작 시간 기록
for i in range(1, 100001):
    answer = (answer * i) % MOD

end = time.time() # 종료 시간 기록
print("결과: ", answer)
print("수행 시간: {:.6f}초".format(end - start)) # 소요 시간 출력