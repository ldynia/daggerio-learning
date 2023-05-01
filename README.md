# Install

```shell
docker build -t dagger -f devops/docker/Dockerfile .

docker run --name dagger --rm -it \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $PWD/src:/usr/src \
    -w /usr/src \
    dagger ash

# This doesn't work in WSL 2
docker run --name dagger --rm -it \
    --privileged \
    -v $PWD/src:/usr/src \
    -w /usr/src \
    dagger ash
```

# RUN

```shell
python main.py
```