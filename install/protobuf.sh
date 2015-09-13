git clone https://github.com/google/protobuf
cd protobuf

./autogen.sh
./configure
make
make check
make install
