DEST="/usr/local/bin/mir"
LIB="/usr/lib/mir"

#may need to create directory first. if so, probably also have to add it to PATH
#sudo mkdir ${LIB}

#uncomment to remove previous installation
sudo rm -rf ${LIB} ${DEST}

#comment out to not install (acts as a complete uninstall if paired with the above)
sudo cp -r ../algMirrorer ${LIB} 2>/dev/null
sudo ln -s ${LIB}/main.py ${DEST}
sudo chmod 755 ${DEST}
