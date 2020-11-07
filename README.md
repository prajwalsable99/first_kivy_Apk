# first_kivy_Apk
building first  android Apk from kivy library of python


#
create a file with name main.py
add the overall code in main.py


# to create apk  for android
we have to use  buildozer module which runs only on linux base
use ubuntu 20.04 LTS 

install buildozer and its dependencies (command on official buildozer doc)

in project directory just add following commmands in terminal :

buildozer init
buildozer -v android debug

your apk is ready in:  project_dir/bin/
