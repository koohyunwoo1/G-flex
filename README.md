# 프로젝트 'G-Flex'

### 프로젝트 개요

---


<img src ="https://img.shields.io/badge/service-Web-red"></img>


<img src ="https://img.shields.io/badge/frontend-Vue-green"></img>


<img src ="https://img.shields.io/badge/backend-Django-092E20"></img><img src ="https://img.shields.io/badge/Database-Sqlite-003B57"></img>

- 진행 기간 : 2024.05.16 ~ 2024.05.24 오전 9시 (9일간) 
- 목표 
  - 검색을 통한 영화 추천서비스 개발
  - 사용자에게 다양한 경험을 제공
  - 장르 및 무드에 따른 영화 추천 서비스 제공

---
### 팀원 정보 및 업부 분담 내역
- 김구태 - 백엔드
  - 사용 Tool : Django
- 구현우 - 프론트엔드
  - 사용 Tool : Vue3

---
### ERD

<img src ="assets/ERD(edited).png"></img>


---

## 우리 서비스 필수 기능


1. 사용자의 검색한 영화와 데이터 베이스 내 영화들의 키워드 유사도 방식을 통해 추천하는 알고리즘
2. 장르, 무드별 태그를 선택했을 때 그에 맞는 영화 추천 제공
3. 영화 포스터 클릭시 영화 정보 제공
4. 영화 리뷰 작성 / 수정 / 삭제 가능
5. 기본적인 회원가입, 로그인, 로그아웃
6. 프로필 페이지


### 서비스 구성 화면

### accounts app
---
  ### 화면 인트로
<img src ="assets/image-3.png"></img>
    - 애니메이션 효과 삽입
  ### 회원가입
<img src ="assets/image.png"></img>
  ### 로그인
<img src ="assets/image-1.png"></img>
  ### 로그아웃
<img src ="assets/image-2.png"></img>

### movies app
---
  ### 홈 화면
<img src ="assets/image-11.png"></img>
  - G-Flex가 추천드리는 영화 8개 추천

  ### 장르별 영화 데이터 가져오기
<img src ="assets/image-4.png"></img>
      - 공포 장르를 선택 했을 때의 영화 추천
  
  ### 무드별 영화 데이터 가져오기
<img src ="assets/image-5.png"></img>
      - 그냥 심심할때 킬링타임 무드를 선택 했을 때의 영화 추천
  
  ### 영화 좋아요 / 좋아요 취소 
<img src ="assets/image-6.png"></img>
<img src ="assets/image-7.png"></img>
  - 좋아요 눌렀을때와 안 눌렀을때의 좋아요 색 차이

  ### 검색한 영화와 유사한 영화 데이터 가져오기
<img src ="assets/image-8.png"></img>
    - ex) 스파이더맨 검색했을 경우, 스파이더맨과 유사한 영화 추천서비스

  ### 영화 디테일 페이지
<img src ="assets/image-9.png"></img>
  - 영화 포스터 클릭시 영화 제목, 배우, 장르, 런타임, 줄거리 소개
  - 영화 리뷰 작성 가능, 수정 / 삭제 기능
  - 영화 리뷰 작성시 글자 수 출력
  - 100글자 이상 시 alert 출력

  ### 마이페이지
<img src ="assets/image10.png"></img>
  - 좋아요 누른 영화 출력
  - 좋아요 누른 영화가 몇개인지 ? 

---

## 느낀 점 

- 김구태 -

- 구현우 - 
  - 첫 프로젝트여서 처음 주제를 정할 때 부터 

