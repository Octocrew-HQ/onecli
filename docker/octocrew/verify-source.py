import subprocess
base = "fe0981f09122358d4b3c721ef3e141026a2fdc46"
patch = "f8179ac80e003dacd16a0e4dfee2f0db330211bb"
def git(*args):
    return subprocess.check_output(["git", *args])
# checkout's shallow tree suffices: fetch only reviewed upstream commits.
subprocess.run(["git", "fetch", "--no-tags", "https://github.com/onecli/onecli.git", base, patch], check=True)
allowed = {"apps/gateway/src/secret_inject.rs"}
changed = set(git("diff", "--name-only", base, "HEAD", "--", "apps/gateway").decode().splitlines())
assert changed == allowed, changed
assert git("show", base + ":apps/gateway/Cargo.lock") == git("show", "HEAD:apps/gateway/Cargo.lock")
# Apply precisely the upstream diff to a temporary base file to verify all bytes.
import tempfile, pathlib
with tempfile.TemporaryDirectory() as tmp:
    p = pathlib.Path(tmp) / "apps/gateway/src"
    p.mkdir(parents=True)
    (p / "secret_inject.rs").write_bytes(git("show", base + ":apps/gateway/src/secret_inject.rs"))
    subprocess.run(["git", "apply", "--unsafe-paths", "--directory=" + tmp], input=git("diff", patch + "^", patch, "--", "apps/gateway/src/secret_inject.rs"), check=True)
    assert (p / "secret_inject.rs").read_bytes() == git("show", "HEAD:apps/gateway/src/secret_inject.rs")
print("Exact 1.41.0 + f8179ac source and original lockfile: PASS")
