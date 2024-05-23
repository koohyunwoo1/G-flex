import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

# 추천 알고리즘 함수
def recommend_movies_names(xMovie, idx, movies):
    # 불용어 제거
    countVec = CountVectorizer(max_features=3000, stop_words='english')

    # 영화 키워드 벡터라이징
    dataVectors = countVec.fit_transform(xMovie).toarray()

    # 코사인 유사도
    similarity = cosine_similarity(dataVectors)
    
    # 유사도 내림차순 5개 영화의 인덱스
    idx_collection = []
    for i in idx:
        distances = similarity[i]
        listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
        idx_collection.extend(listofMovies)
 
    # 인덱스를 pk로 바꾸기
    pk_collection = []
    for idx in idx_collection:
        pk_collection.append(movies[idx[0]]['pk'])

    return pk_collection

# 새로운 영화에 moodtag 부여하는 함수
def assign_moodtags_to_movies(movies, xMovie):
    for i, movie in enumerate(movies):
        if not movie['fields']['moodtag']:
            print(f"Assigning moodtags for movie index {i} with title '{movie['fields']['title']}'")

            # 유사한 영화 찾기
            similar_movie_pks = recommend_movies_names(xMovie, [i], movies)
            print(f"Similar movies found: {similar_movie_pks}")

            # 유사한 영화들의 moodtag 수집
            similar_moodtags = []
            for pk in similar_movie_pks:
                for m in movies:
                    if m['pk'] == pk:
                        similar_moodtags.extend(m['fields']['moodtag'])
            print(f"Collected moodtags from similar movies: {similar_moodtags}")
            
            # 중복을 제거한 모든 moodtag 추가
            unique_moodtags = list(set(similar_moodtags))
            if unique_moodtags:
                movie['fields']['moodtag'].extend(unique_moodtags)
                print(f"Assigned moodtags: {unique_moodtags}")
    
    return movies

# 메인 함수
def main():
    try:
        # 데이터 로드
        with open('movie.json', 'r', encoding='utf-8') as f:
            movies = json.load(f)
        print("Data loaded successfully.")

        # xMovie 데이터 생성 (영화 제목과 개요를 결합한 문자열 리스트)
        xMovie = [movie['fields']['title'] + " " + movie['fields']['overview'] for movie in movies]
        print("xMovie data prepared successfully.")

        # 영화 데이터에 moodtag 부여
        movies_with_moodtags = assign_moodtags_to_movies(movies, xMovie)
        print("Moodtags assigned successfully.")

        # 결과 저장
        with open('movies_with_moodtags.json', 'w', encoding='utf-8') as f:
            json.dump(movies_with_moodtags, f, ensure_ascii=False, indent=4)
        print("Data saved successfully to movies_with_moodtags.json.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
