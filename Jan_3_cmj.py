# No. 1546   평균(브론즈1)
n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
average = sum(scores) / n * 100 / max_score
print(average)

# No. 1157   단어 공부(브론즈1)
word = input().upper()
char_count = {}
for char in word:
    char_count[char] = char_count.get(char, 0) + 1
max_count = max(char_count.values())
most_frequent = [char for char, count in char_count.items() if count == max_count]
if len(most_frequent) > 1:
    print("?")
else:
    print(most_frequent[0])
    
# No. 1316   그룹 단어 체커(실버5)
n = int(input())
group_word_count = 0

for _ in range(n):
    word = input()
    seen = set()
    prev_char = ''
    is_group_word = True

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
            prev_char = char

    if is_group_word:
        group_word_count += 1
print(group_word_count)
