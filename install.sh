clear

echo ""
echo "Bash Script For Preparing Environment for Face Recognition"
echo "__________________________________________________________"

echo ""
echo ""
echo "*************************************"
echo -n "Installing python-pip...          "
sudo apt-get install python3-pip -y >/dev/null 2>&1
if [[ $? > 0 ]]; then echo "Failed"; else echo "OK"; fi

echo "*************************************"
echo -n "Installing python3-pip...         "
sudo apt-get install python3-pip -y >/dev/null 2>&1
if [[ $? > 0 ]]; then echo "Failed"; else echo "OK"; fi

echo "*************************************"
echo -n "Installing python-opencv...       "
sudo apt-get install python-opencv -y >/dev/null 2>&1
if [[ $? > 0 ]]; then echo "Failed"; else echo "OK"; fi

echo "*************************************"
echo -n "Installing face_recognition...    "
pip3 install face_recognition >/dev/null 2>&1
if [[ $? > 0 ]]; then echo "Failed"; else echo "OK"; fi

echo "*************************************"
echo -n "Creating 'Face-Database' dir...   "
Directory="Face-Database"
if [ ! -d "$Directory" ]; then mkdir $Directory && echo "OK";
else echo "Failed - Directory exists"; fi

echo "*************************************"
echo Finalizado
