
import tarfile
import urllib.request
import sys
import io

REPO_NAME = sys.argv[1]
REPO_URL = sys.argv[2] + "/" + sys.argv[3]
REPO_ARCH = sys.argv[3]
DB_URL = "%s/%s.db" % (REPO_URL, REPO_NAME)

db_response = urllib.request.urlopen(DB_URL)

db_response = io.BytesIO(db_response.read())

packages = []

with tarfile.open(fileobj=db_response) as db:
    packages = [name for name in db.getnames() if "/" not in name]

print(DB_URL)
for package in packages:
    print("%s/%s-%s.pkg.tar.xz" % (REPO_URL, package, REPO_ARCH));
    print("%s/%s-%s.pkg.tar.xz.sig" % (REPO_URL, package, REPO_ARCH));
