touch ~/.bashrc
cat rules/* > ~/.bashrc.alexanderwu
grep alexanderwu ~/.bashrc || echo "source ~/.bashrc.alexanderwu" > ~/.bashrc
source ~/.bashrc
