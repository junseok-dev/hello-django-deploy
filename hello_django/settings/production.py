from .base import *
import os

# EB 내부에서 ALB가 EC2에 대한 헬스쳌 요청대비
# - EC2 사설ip로 요청하는 경우 Disallowed Host 오류발생
# - ebhealthcheck 앱이 현재 EC2에 사설 ip를 자동으로 ALLOWED_HOST에 등록
INSTALLED_APPS.extend([
    'ebhealthcheck.apps.EBHealthCheckConfig',
])

DEBUG = False

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    '.amanzonaws.com'
]

# 추가 ALLOWED_HOSTS 설정
additional_allowed_hosts = os.getenv('ALLOWED_HOSTS')
if additional_allowed_hosts:
    ALLOWED_HOSTS.extend([host.strip() for host in additional_allowed_hosts.split(',')])

print(f'[production] {ALLOWED_HOSTS = }')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}