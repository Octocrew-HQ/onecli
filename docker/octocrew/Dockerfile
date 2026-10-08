# Only the gateway binary differs from the official OneCLI 1.41.0 image.
FROM rust:1.94.0-alpine3.23@sha256:ff0adc35894eb79586ce752a1b5a9eadc88b938c56d8f2b4b537b6258ff3fa10 AS gateway-builder
RUN apk add --no-cache musl-dev pkgconfig openssl-dev openssl-libs-static
WORKDIR /build
COPY apps/gateway/ ./
RUN cargo build --locked --release
FROM ghcr.io/onecli/onecli@sha256:66dc84042310cab762ed3b1f71a98349a72aa132ad44651b7ae76c371aaafe6b
COPY --from=gateway-builder /build/target/release/onecli-gateway /usr/local/bin/onecli-gateway
COPY LICENSE NOTICE /usr/share/licenses/onecli/
