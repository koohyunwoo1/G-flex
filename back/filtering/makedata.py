import json

# 영화 데이터 필터링 함수
def filter_movies_by_popularity(movies):
    filtered_movies = []
    for movie in movies:
        if movie['fields']['popularity'] > 50:
            filtered_movies.append(movie)
    return filtered_movies

# 메인 함수
def main():
    try:
        # 데이터 로드
        with open('movie.json', 'r', encoding='utf-8') as f:
            movies = json.load(f)
        print("Data loaded successfully.")

        # 영화 데이터 필터링
        filtered_movies = filter_movies_by_popularity(movies)
        print(f"Filtered movies count: {len(filtered_movies)}")

        # 결과 저장
        with open('filtered_movies.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_movies, f, ensure_ascii=False, indent=4)
        print("Filtered data saved successfully to filtered_movies.json.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# python makedata.py 를 하면 영화 populartity가 
# 50 넘는 데이터만 남은 새로운 filtered_movies.json이 생성된다