FROM alpine:3.10

COPY httpserver.py /httpserver.py
RUN apk --no-cache add python && chmod +x /httpserver.py

WORKDIR /tmp

ENTRYPOINT ["/httpserver.py"]

