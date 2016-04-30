#! /bin/bash
mkdir $HOME/priscillafy
mkdir $HOME/priscillafy/bin
cp priscillafy.py $HOME/priscillafy/bin
ln -s $HOME/priscillafy/bin/priscillafy.py $HOME/priscillafy/bin/priscillafy
ln -s $HOME/priscillafy/bin/priscillafy.py $HOME/priscillafy/bin/p
chmod -R +x $HOME/priscillafy/bin
if ! hash priscillafy 2>/dev/null; then
    echo "PATH=$PATH:$HOME/priscillafy/bin" >> ~/.bash_profile
    source ~/.bash_profile
fi
echo "Installed"
