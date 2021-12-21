# print env variables (see also those inherited from project envs in settings)
export PATH=$PATH:/home/cdsw/conda/bin  # this has not yet been built
env


# install python modules
pip3 install -r requirements.txt


# download gazetteer data file
mkdir /home/cdsw/data/
wget --no-verbose -O /home/cdsw/data/gazetteers.zip https://filedn.com/lvxzpqbRuTkLnAjfFXe7FFu/Gazetteer%20DB/gazetteers%202021-12-03.zip
ls /home/cdsw/data/ -a
unzip /home/cdsw/data/gazetteers.zip -d /home/cdsw/data/
#rm /home/cdsw/data/gazetteers.zip
ls /home/cdsw/data/ -a


# install tesseract binaries via conda
cd

ls -a
ls /home/cdsw -a
ls /opt/conda/bin -a

/opt/conda/bin/conda install -y -c conda-forge -m --prefix /home/cdsw/conda python=3.6 tesseract

ls -a
ls /home/cdsw/ -a
ls /home/cdsw/conda/bin -a
ls /home/cdsw/conda/share -a
ls /home/cdsw/conda/share/tessdata -a


# test that it worked

/home/cdsw/conda/bin/tesseract --version
which /home/cdsw/conda/bin/tesseract
which tesseract

ls -a
ls /home/cdsw -a
