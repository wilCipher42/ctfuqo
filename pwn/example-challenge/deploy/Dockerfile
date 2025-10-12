FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    gcc-multilib \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY src/vuln /app/vuln

RUN chmod +x /app/vuln

EXPOSE 9999

CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:/app/vuln"]
