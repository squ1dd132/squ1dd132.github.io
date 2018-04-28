#!/bin/bash
dpkg-deb -b ./debs/com.squ1dd13.redditrandom_0.0.1-9+debug_iphoneos-arm.deb

dpkg-scanpackages -m ./ /dev/null | gzip > Packages.gz;

dpkg-scanpackages -m ./ /dev/null | bzip2 > Packages.bz2;

dpkg-scanpackages -m ./ /dev/null > Packages;
