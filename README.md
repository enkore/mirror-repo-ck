mirror-repo-ck
==============

[![Build Status](http://golem.enkore.de/buildStatus/icon?job=mirror-repo-ck)](http://golem.enkore.de/job/mirror-repo-ck/)

Mirrors [repo-ck](http://repo-ck.com/) every night (around 05:00 UTC). Add this to your pacman.conf to use this mirror:

    [repo-ck]
    Server = http://pstore.enkore.de/mirrors/repo-ck/$arch
    
## Arch mirroring tooling

- `dblist.py` outputs a list of URLs for a given Arch repository. It takes three command line arguments:
  1. Repository name (e.g. `repo-ck`)
  2. Repository base URL (e.g. `http://repo-ck.com`)
  3. Architecture (e.g. `x86_64`)
- `clean.py` takes such a list and removes all packages that are not on that list from a directory.
  - Thus it removes old versions of packages from the mirror
- Then `wget` (or `curl`) can be used to download all new packages using a command like this
  (assuming the output of `dblist.py` was saved to a file named `index`):
  
      wget --input-file=index --directory-prefix=<output dir> --tries=inf --limit-rate=500k --no-verbose --no-clobber
  
  When using this command you need to remove the `<repo-name>.db` file from the output directory first,
  so that it is always up to date. It is not removed by `clean.py` ; `clean.py` only removes packages and
  package signatures.
