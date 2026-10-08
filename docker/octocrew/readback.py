import json, os, urllib.request
repo = "octocrew-hq/onecli"
# Anonymous token: readback must prove the installer can pull without credentials.
token = json.load(urllib.request.urlopen("https://ghcr.io/token?scope=repository:" + repo + ":pull", timeout=30))["token"]
headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.oci.image.index.v1+json"}
req = urllib.request.Request("https://ghcr.io/v2/" + repo + "/manifests/1.41.0-octocrew.refresh1", headers=headers)
with urllib.request.urlopen(req, timeout=30) as response:
    digest = response.headers["Docker-Content-Digest"]
    assert digest == os.environ["EXPECTED_DIGEST"], (digest, os.environ["EXPECTED_DIGEST"])
    manifest = json.load(response)
    platforms = [m["platform"] for m in manifest["manifests"] if m["platform"]["os"] != "unknown"]
    assert platforms == [{"architecture": "amd64", "os": "linux"}], platforms
print("Public anonymous registry readback: ghcr.io/" + repo + "@" + digest)
