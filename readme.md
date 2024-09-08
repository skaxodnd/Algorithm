# 미래아이 알고리즘 🕸️

## **📅 일정 (09.08 ~ )**
| |1|2|3|
|:-:|:-:|:-:|:-:|
|1주차(09.08) Greedy|[거스름돈](https://www.acmicpc.net/problem/14916)|[회의실 배정](https://www.acmicpc.net/problem/1931)|[A->B](https://www.acmicpc.net/problem/16953)
---

## ✔️ 문제 풀이
  - 개수 : 주 3개
  - 알고리즘 유형 : 그래프탐색, 완전탐색, 문자열, DP, 구현, 해시 등
  - 난이도 : 백준 실버부터 start 🥈
   
## ✔️ 풀이 방식 
    - 주에 3문제씩 풀이 진행, 15분간의 풀이 진행 후 코드 업로드
    - 코드 리뷰
    - 문제 풀이 해설 진행
    
## ✔️ 공유 과정

        ex)  
        해당 문제를 보자마자 그리디가 떠올랐는데, 해결이 되지 않았습니다. 
        이후 DP 접근 방식을 떠올리긴했지만, 접근 로직이 명확히 떠오르지 않았습니다. 
        점화식에 대한 공부가 더 필요하다고 느꼈습니다. 
        n번 라인에서 ~~로직을 떠올리지 못했습니다

        def solution(N, number):
        S = [0, {N}]

        for i in range(2, 9):
          case_set = {int(str(N)*i)}
          for j in range(1, i//2+1):  # S[i_half] S[1]
---

## 📁 폴더 구조
    - N주차(mm.dd~mm.dd)
      - 본인 이름 폴더 (ex. kimyongsang) 
        - 문제 풀이 파일 (ex. 하노이탑.py )      
    - readme.md
