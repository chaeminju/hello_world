------------------------------------------
# No. 2751 수 정렬하기
import sys

n=int(sys.stdin.readline().rstrip())
list=[]

for i in range(n):
    list.append(int(sys.stdin.readline()))

list.sort()

for i in list:
    print(i)


------------------------------------------
# No. 2941 크로아티아 알파벳
list=["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

a=input()
count=0
result=len(a)

for i in list:
    if  a.find(i)!=-1:
        count+=a.count(i)

print(result-count)


------------------------------------------
# No. 1181 단어 정렬
n=int(input())
arr=[]

for i in range(n):
    x=input()
    if x in arr: continue
    else: arr.append(x)

arr.sort(key=lambda x:(len(x), x))
# 아래 블로그가 lambda에 대해 가장 잘 설명해 둔 듯!
# https://velog.io/@rockwellvinca/python-sorted-sort-key-%EC%82%AC%EC%9A%A9%EB%B2%95

for i in arr:
    print(i)


------------------------------------------
# No. 1193 분수찾기
a=int(input())
count=1
N=a

while N>count:
    N-=count
    count+=1

x=0
y=0
if count==1: print("1/1")
else:
    if count%2==0:
        x=(count+1)-N
        y=N
        print(str(y)+"/"+str(x))
    elif count%2==1:
        x=N
        y=(count+1)-N
        print(str(y)+"/"+str(x))


------------------------------------------
# No. 11651 좌표 정렬하기2
n=int(input())

list=[]

for i in range(n):
    x, y=map(int, input().split())
    list.append([x, y])

list.sort(key=lambda x:(x[1], x[0]))

for i in list:
    print(i[0], i[1])


------------------------------------------
# No. 2563 색종이
list=[[False for i in range(100)]for i in range(100)]

n=int(input())

for i in range(n):
    x, y=map(int, input().split(" "))
    for a in range(x, x+10):
        for b in range(y, y+10):
            list[a][b]=True

count=0
for i in list:
    for j in i:
        if j==True: count+=1

print(count)


------------------------------------------
# No. 25206 너의 평점은
sum=0
result=0

for i in range(20):
    a, b, c=map(str, input().split())
    if c=="A+":
        sum+=float(b)*4.5
        result+=float(b)
    elif c=="A0":
        sum+=float(b)*4.0
        result+=float(b)
    elif c=="B+":
        sum+=float(b)*3.5
        result+=float(b)
    elif c=="B0":
        sum+=float(b)*3.0
        result+=float(b)
    elif c=="C+":
        sum+=float(b)*2.5
        result+=float(b)
    elif c=="C0":
        sum+=float(b)*2.0
        result+=float(b)
    elif c=="D+":
        sum+=float(b)*1.5
        result+=float(b)
    elif c=="D0":
        sum+=float(b)*1.0
        result+=float(b)
    elif c=="F":
         result+=float(b)

print(sum/result)


------------------------------------------

