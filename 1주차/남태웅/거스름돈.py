m = int(input())
answer = 0

while m%5 != 0:
    m -= 2
    answer += 1
    
answer = answer + m//5

if answer == 0:
    answer = -1

if m<0:
    answer = -1
print(answer)
