# No. 10811 바구니 뒤집기
n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])
print(' '.join(map(str, basket)))

# No. 2587   대표값2
nums = []
for _ in range(5):
    nums.append(int(input()))
nums.sort()
print(sum(nums)//5)
print(nums[2])

# No. 2745   진법 변환
n, b = input().split()
b = int(b)
result = 0
for i in range(len(n)):
    if n[i].isalpha():
        result += (ord(n[i]) - 55) * (b ** (len(n) - i - 1))
    else:
        result += int(n[i]) * (b ** (len(n) - i - 1))
print(result)

# No. 2747   피보나치 수
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
print(fibonacci(n))

# No. 25305 커트라인
n = int(input())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[n-1])

# No. 5585   거스름돈
change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coins:
    count += change // coin
    change %= coin
print(count)

# No. 19532 수학은 비대면 강의입니다
a, b, c, d, e, f = map(int, input().split())
x = (c*e - b*f) // (a*e - b*d)
y = (a*f - c*d) // (a*e - b*d)
print(x, y)