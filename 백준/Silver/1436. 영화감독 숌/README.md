# [Silver V] 영화감독 숌 - 1436 

### 생각정리
해당 문제는 브루트알고리즘이으로 1부터 666을 포함하는 숫자를 찾아서 N번째 숫자 발견하면 반복문을 멈추는 방식으로 풀었다. 오래 걸릴까봐 살짝 걱정했는데 브루트알고리즘이 대게 그렇듯 
정답 제출에는 이상이 없었다. 이번에도 느낀건 굳이 어렵게 알고리즘을 돌아가지 말고 그냥 처음부터 쭉 검색하는게 적절한 방법일 때가 있다는 점이다.

[문제 링크](https://www.acmicpc.net/problem/1436) 

### 성능 요약

메모리: 30840 KB, 시간: 672 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다. 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.</p>

<p>하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.</p>

<p>종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.</p>

<p>따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.</p>

<p>숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.</p>

### 입력 

 <p>첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.</p>

