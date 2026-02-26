FROM python:3.12

# 환경변수 관련
# .pyc파일 생성 방지
ENV DONTWRITEBYTECODE=1 
# 로그 즉시출력(docker logs 실시간 확인)
ENV PYTHONNUMBUFFERED=1

# 이미지(컨테이너) 작업디렉토리 지정
WORKDIR /app 

# python 의존 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 모든 프로젝트 소스코드를 /app으로 복사 (.dockerignore에 작성된 파일 제외)
COPY . . 

EXPOSE 8000

# 컨테이너 실행시 명령어 작성: ENTRYPOINT/CMD
CMD ["gunicorn", "-c", "gunicorn.conf.py", "hello_django.asgi:application"]

