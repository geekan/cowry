touch ~/.bashrc
cat RULES > ~/.bashrc.alexanderwu
grep alexanderwu ~/.bashrc || echo "source ~/.bashrc.alexanderwu" > ~/.bashrc
source ~/.bashrc
