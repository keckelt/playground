JDK_BUILD="22"
JDK_ARCHIVE="openjdk-11-ea+${JDK_BUILD}_linux-x64-musl_bin.tar.gz"

echo "Downloading ${JDK_ARCHIVE}"
wget https://download.java.net/java/early_access/alpine/${JDK_BUILD}/binaries/${JDK_ARCHIVE} --quiet --show-progress

echo "Downloading sha256 checksum"
wget https://download.java.net/java/early_access/alpine/${JDK_BUILD}/binaries/${JDK_ARCHIVE}.sha256 --quiet --show-progress

echo "Verify checksum"
# Two spaces bewteen hash & filename, as the output of 'sha256sum openjdk-11-...tar.gz'
echo "  ${JDK_ARCHIVE}" >> ${JDK_ARCHIVE}.sha256
sha256sum -c ${JDK_ARCHIVE}.sha256

echo "Checksum is correct"