# coding: utf-8

config_mac()
{
    curl -L http://install.ohmyz.sh | sh
    cat alias.rules/*.rules > ~/.oh-my-zsh/custom/alexanderwu.zsh
}

config_linux()
{
    echo 'not done yet..'
}

config_windows()
{
    echo 'not done yet..'
}

[ "$(uname)" == "Darwin" ] && config_mac()
[ "$(expr substr $(uname -s 1 5))" == "Linux" ] && config_linux()
[ "$(expr substr $(uname -s 1 10))" == "MINGW32_NT" ] && config_windows()
[ "$(expr substr $(uname -s 1 6))" == "CYGWIN" ] && config_windows()

