Всё ниже написанное взято чисто из документации Kivy и buildozer. Вот ссылки:
https://kivy.org/doc/stable/guide/packaging-android.html#packaging-android
https://github.com/kivy/buildozer


Установка buildozer:
# via pip (latest stable, recommended)
# if you use a virtualenv, don't use the `--user` option
`pip install --user buildozer`

# latest dev version
# if you use a virtualenv, don't use the `--user` option
`pip install --user https://github.com/kivy/buildozer/archive/master.zip`

# git clone, for working on buildozer
`git clone https://github.com/kivy/buildozer
cd buildozer
python setup.py build
pip install -e .`

После этого buildozer будет установлен в вашей системе. После этого перейдите в каталог вашего проекта и запустите:
`buildozer init`

При этом создается файл buildozer.spec, управляющий конфигурацией сборки. 
Вы должны соответствующим образом отредактировать его, указав название вашего приложения и т. д. 
Вы можете установить переменные для управления большинством или всеми параметрами, передаваемыми в python для Android.

Установите зависимости buildozer: https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android

Вот команды для Ubuntu из ссылки выше:
`sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv`

# add the following line at the end of your ~/.bashrc file
`export PATH=$PATH:~/.local/bin/`

Наконец, подключите свое Android-устройство и запустите:
`buildozer android debug deploy run`