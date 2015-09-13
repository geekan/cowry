
set -e
GITPATH=~/git

cd $GITPATH
curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash # maybe you need sudo here
git clone https://github.com/torch/distro.git $GITPATH/torch --recursive
cd $GITPATH/torch; ./install.sh

# If you use zsh..
source ~/.zshrc

# compile and make install protobuf could do this trick.
sudo apt-get install libprotobuf-dev protobuf-compiler
luarocks install loadcaffe

cd $GITPATH
git clone https://github.com/jcjohnson/neural-style.git
cd neural-style

sh models/download_models.sh
th neural_style.lua -gpu -1 -print_iter -1

