# SSAFY 1학기 최종 PJT

## 대주제 : 영화

### 프로젝트 주제 : mbti, 나이, 성별, 본인의 영화 취향을 토대로 한 영화 추천서비스 제작

### 필요한 것:

- django 
- vue 
- js
- SQL 
- chatGPT
---

## 프로젝트 정식 시작 날짜 : 5/16

### 스케줄

- 5/16 ~ 5/18 : 장고 마무리, 목업 수정
- 5/19 ~ 5/22 : 프론트 마무리, back과 front 연동
- 5/23 : ppt 마무리, 최종 확인


### 사실 상 같이 프로젝트 준비 가능한 날

- 5/7
- 5/12
- 5/13
- 5/14
- 5/15
 
---
### 해야할 것

- 서비스의 이름
- 팀 이름
- 스케줄 구체화
- 공부

#### 서비스의 기능 구체화

- 사이트 구성요소, 목업 구성요소들 구상 필요

#### 영화추천서비스 : G-Flex
#### 팀명 : 구찌
#### 팀원 : 김구태, 구현우


#### Home, 영화검색페이지, 회원가입(로그인/로그아웃), 마이페이지

#### API : TMDB MOVIE, Crawling

#### Model : 

- Movie(영화)
  - Title(제목)
  - Overview(줄거리)
  - Popularity
  - ReleaseDate(개봉일)
  - Runtime(영화 전체 시간)
  - Tagline(모름)

- User(유저)
  - UserId(PK)
  - Username(유저 이름)

- Genres
  - GenreID(PK) (장르 자체 ID)
  - Name(장르의 이름)
 
- Actor
  - ActorID(PK) (배우 자체 ID)
  - Name (배우의 이름)


- MoodTag(기분 별 태그)
  - MoodTagID(PK) (분위기 자체 ID)
  - Name(분위기의 이름)

- Article(게시글)
  - UserID(FK) (유저의 ID)
  - ArticleID(게시글의 ID)
  - Title(게시글 제목)
  - Content(게시글 내용)
  - Created_at(게시글 생성 시간)
  - Updated_at(게시글을 수정한 시간)

- Comment(댓글)
  - ArticleID(FK) (게시글의 ID)
  - UserID(FK) (유저의 ID)
  - CommentID(PK) (댓글의 ID)
  - Content (댓글의 내용)
  - Created_at(댓글 생성 시간)
  - Updated_at(댓글을 수정한 시간)

- Rating(평점)
  - MovieId(FK)
  - UserID(FK)
  - RatingID(PK) (평점의 ID)
  - Rate(평점)
  - Review(후기)

