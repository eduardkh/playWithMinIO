# MinIO

> spin-up a server

```bash
docker run -p 9000:9000 -p 9001:9001 \
-e "MINIO_ROOT_USER=username" \
-e "MINIO_ROOT_PASSWORD=password" \
-v $(pwd)/data:/data \
minio/minio server /data --console-address ":9001"

# prod version example...
docker run -p 9000:9000 \
-e "MINIO_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE" \
-e "MINIO_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
-v $(pwd)/data:/data \
minio/minio server /data
```

> install mc tool

```bash
curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

mc --help
```

> configure and use mc tool

```bash
# set endpoint
mc alias set MinIO http://localhost:9000 [YOUR-ACCESS-KEY] [YOUR-SECRET-KEY]
# change bucket policy to read
mc anonymous set download MinIO/media
```
