FROM docker:23.0.5-dind

COPY config/etc/ssl/* /etc/ssl

RUN apk update && \
    apk add py3-pip

RUN pip3 install --upgrade pip dagger-io
