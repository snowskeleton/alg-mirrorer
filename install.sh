DEST="/usr/local/bin/mir"
LIB="/usr/lib/mir"

#may need to create directory first. if so, probably also have to add it to PATH
#sudo mkdir ${LIB}
sudo cp -r ../algMirrorer ${LIB}
sudo ln -s ${LIB}/main.py ${DEST}
sudo chmod 755 ${DEST}

##uncomment to uninstall
#sudo rm -rf ${LIB} ${DEST}
