# API 서버 구축

## 1. 가상환경 생성

```bash
python -m venv venv
```

<br>

## 2. 가상환경 실행

```python
source venv/Scripts/activate
```

<br>

## 3. 패키지 설치

```bash
pip install -r requirements.txt
```

<br>

## 4. migration

```bash
python manage.py makemigrations
python manage.py migrate
```
<br>

## 5. fixture 데이터 로드

```bash
python manage.py loaddata actor.json genre.json moodtag.json movie.json
```

<br>

## 6. 서버 실행

```bash
python manage.py runserver
```
