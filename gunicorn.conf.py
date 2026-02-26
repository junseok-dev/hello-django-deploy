import multiprocessing

# worker(process) 논리코어 * 2 + 1
cpu_count = multiprocessing.cpu_count()
workers = (cpu_count * 2) + 1
print(f'{workers = }')

bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker' # 하나의 worker프로세스는 UvicornWorker클래스로 처리
timeout = 30