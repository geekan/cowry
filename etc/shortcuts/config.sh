# coding: utf-8

# touch ~/.bashrc

#######
# MAC #
#######
cat alias.rules/* > ~/.bashrc.alexanderwu
grep bashrc ~/.bash_profile || echo '[ -r ~/.bashrc ] && source ~/.bashrc' >> ~/.bash_profile
grep alexanderwu ~/.bashrc || echo "source ~/.bashrc.alexanderwu" >> ~/.bashrc
source ~/.bashrc
