FROM python:3.12.3-slim

# 컨테이너 내부 작업 디렉터리
WORKDIR /app

# Python 패키지 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY app/ ./app/
COPY wsgi.py .

# 컨테이너 포트
EXPOSE 5000

# Flask 서버 실행
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "wsgi:app"]