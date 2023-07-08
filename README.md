# MinIO

> spin-up a server

```bash
docker run -p 9000:9000 -p 9001:9001 \
-e "MINIO_ROOT_USER=username" \
-e "MINIO_ROOT_PASSWORD=password" \
minio/minio server /data --console-address ":9001"

```
