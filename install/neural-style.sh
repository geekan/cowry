cd /git/
curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
git clone https://github.com/torch/distro.git /git/torch --recursive
cd /git/torch; ./install.sh

source ~/.zshrc

sudo apt-get install libprotobuf-dev protobuf-compiler
luarocks install loadcaffe

cd /git/
git clone https://github.com/jcjohnson/neural-style.git
cd neural-style
