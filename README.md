# OTFA Flask Server

Docker에서 실행하는 간단한 Flask API 서버입니다.

## 실행 방법

Docker Compose로 빌드하고 실행합니다.

```bash
docker compose up -d --build
```

서버 주소: <http://localhost:5000>

## API

| 경로 | 설명 |
| --- | --- |
| `/` | 서버 상태 메시지 |
| `/health` | 헬스 체크 |
| `/api/hello` | 인사 메시지 |

중지하려면 다음 명령을 실행합니다.

```bash
docker compose down
```
