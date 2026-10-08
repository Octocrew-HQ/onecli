# Octocrew OneCLI refresh backport

Operator-authorized temporary 1.41.0 + ONLY f8179ac (#434).
Base source: fe0981f09122358d4b3c721ef3e141026a2fdc46.
Base OCI index: sha256:66dc84042310cab762ed3b1f71a98349a72aa132ad44651b7ae76c371aaafe6b.
Base linux/amd64 manifest: sha256:9491798c8aef6495907a63ea85492c8e3a72e13247922b59ff6ff8bb3af28967.
The base digest was read from anonymous GHCR registry API on 2026-10-08.
Gateway path /usr/local/bin/onecli-gateway is checked on the actual base in CI.
Alpine/musl OSS build uses Rust 1.94.0; original Cargo.lock is mandatory.
Builder index digest read from Docker Hub API on 2026-10-08.
Web, API, schema, entrypoint, volumes and non-gateway binaries remain from base.
LICENSE and this distribution's NOTICE are also copied into the image.

Publication: public GHCR package, public repository hosted Actions, no paid
resources or additional secrets. Only workflow GITHUB_TOKEN is used.
Human tag: 1.41.0-octocrew.refresh1. Installers MUST use registry-readback digest.
Once adopted, do not overwrite this tag; a different artifact requires refresh2.

Architecture: linux/amd64 ONLY. arm64 was not built/accepted; native arm64 fresh
install is unsupported. No transparent emulation fallback is authorized.
Limitations: upstream #438 remains unchanged and consciously accepted;
this backport does not fix revoked/invalid refresh tokens (provider login is
required). No policy migration, stand, real-token OAuth acceptance or client
rollout. A same-base image rollback restores the old refresh defect.
No upstream main merges or automatic additional fixes.
