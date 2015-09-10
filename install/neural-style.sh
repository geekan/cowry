cd /git/
curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
git clone https://github.com/torch/distro.git /git/torch --recursive
cd /git/torch; ./install.sh
