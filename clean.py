
import os
import os.path
import sys

current_files = [os.path.basename(url) for url in sys.stdin]
saved_bytes = 0

for path in os.listdir(sys.argv[1]):
    path = os.path.join(sys.argv[1], path)
    if (path not in current_files and
        (path.endswith(".tar.xz") or path.endswith(".tar.xz.sig"))):
        print("Removing old file '%s'" % os.path.basename(path))
        saved_bytes += os.stat(path).st_size
        os.remove(path)

if saved_bytes:
    print("Reclaimed %d kilobytes disk space" % (saved_bytes / 1024))
