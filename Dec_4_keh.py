# N0. 3052

count=[False for i in range(1000)]
result=0;

for i in range(10):
    a=int(input())
    num=a%42
    if count[num]!=True:
        count[num]=True
        result+=1
    else:
        continue
    
print(result)



# NO.2577

A=int(input())
B=int(input())
C=int(input())
count=[0 for i in range(11)] #배열 생성과 동시에 0으로 초기화+정적 배열 할당
result=str(A*B*C)

for i in range(len(result)):
    x=int(result[i])
    count[x]+=1

for i in range(10):
    print(count[i])



# NO. 8958

a=int(input())


for i in range(a):
    count=0
    sum=0
    x=input()
    for j in range(len(x)):
        if x[j]=='O':
            count+=1
            sum+=count
        else:
            count=0
    print(sum)



# NO. 1978

a=int(input())
arr=input().split(" ")
result=0

for i in range(a):
    x=int(arr[i])
    num=0
    for j in range(2, x):
        if x%j==0:
            num=1
    if num==0 and x!=1:
        result+=1

print(result)



# NO. 2750

a=int(input())
arr=[]

for i in range(a):
    x=int(input())
    arr.append(x)

arr.sort()

for i in range(a):
    print(arr[i])



# NO. 2798

x, y=map(int, input().split())
# map(): 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환
# map(function, iterable) 형식으로 사용하며, iterable의 각 요소에 대해 function 함수를 적용한 결과를 반환함.
# 이 문제에서는 input()으로 받은 문자열을 .split()을 통해 공백문자 기준으로 나누어 int를 적용한 뒤( 즉, int(input().split()) ), x와 y에 각각 저장함. 

arr=map(int, input().split())
arr=list(arr)
# map은 인덱싱이 안됨. 즉, 리스트/튜플/딕셔너리처럼 []를 이용하여 접근 불가능. 따라서 객체변환을 해준 뒤 접근해야 함.
    
result=[]
max=0
for i in range(x):
    for j in range(i+1, x):
        for k in range(j+1, x):
            sum=arr[i]+arr[j]+arr[k]
            if sum<=y and max<sum:
                max=sum

print(max)



# NO. 2292

a=int(input())
count=0

while a>1:
    if a-6>=0:
        count+=1
        a-=6*count
    else:
        count+=1
        break
    
print(count+1)


 

# 추가문제(내가 자바스터디 문제를 착각하고 파이썬으로 풀어버림...ㅠㅠㅠㅠㅠㅠㅠ)
# NO. 11650
a=int(input())
arr=[]

for i in range(a):
    x, y=map(int, input().split())
    arr.append([x, y])

arr.sort()

for i in range(a):
    print(arr[i][0], arr[i][1])
                
'''처음 코드 작성했을 때, a=input()로 받은 뒤 arr.append(a.split())를 이용하여 리스트 내부에 리스트로 저장하였으나
arr.sort()를 하는 과정에서 문자열로 정렬이 이루어져 1 -1, 1 -2를 입력했을 때 1 -2, 1 -1 순서대로 출력이 되는것이 아닌 반대로 출력되었다.
따라서 map(int, input().split())를 이용해 int형으로 리스트를 추가하고 정렬하였다.'''
