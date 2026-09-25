# Church Python OBS- Windows Quick Start Guide 
----------------------------------------------------------------------------------------------- 
## Installation and First Script Run 
1. Download Python from it's website: https://www.python.org/downloads/release/python-368/ 
    - Only versions 3.6 - 3.12 are compatible with OBS 
2. For instance, I downloaded version 3.6.8 and selected "Windows x86-64 executable installer" 
3. When the install wizard window pops up select _Add Python 3.6 to PATH_ 
    - If you downloaded a different version, then whatever version you downloaded will appear in place of _3.6_ 
4. Once the installation is done, select the _Close_ button on the bottom-left of the window 
5. Open up the OBS Studio application 
6. On the top bar, select _Tools > Scripts_ and then select _Python Settings_ 
7. Select _Browse_ and navigate to _C:\Users\\[username]\AppData\Local\Programs\Python\Python36_ 
    - If your version is different then you'll see a diffrent number instead of _Python##_ 
8. Once you select the proper folder for your installation, don't open it, just hit _Select_ in the bottom left 
9. Create a new text file on your Desktop named _Hello_World.py_ and in it, type the following: 
    print("Hello World")
10. Save the file, open the Scripts window in OBS and click the _**+**_ icon 
11. Copy the absolute path from there, open a new instance of File Explorer, and paste the path in the address bar 
    - The absolute path is the complete location in which a file or directory (folder) resides, beginning with the root directory ( _**/**_ ) 
12. Drag the _Hello_World.py_ file from the _Desktop_ to the _scripts_ folder 
13. In the _Scripts_ window, select _Script Log_ and you should now see your message 
    - If this doesn't work, try right-clicking the _Hello_World.py_ script, selecting _Reload_, and opening _Script Log_ again 
14. Congratulations, you just sucessfully ran your first Python script inside of OBS Studio!! 
<br><br><br><br><br><br>




## Package Installation and Basic Tests 
1. Open up PowerShell as administrator 
2. Check to see if you have multiple versions of Python on your computer: 
    > py -0p
3. If you do, then make sure you download the packages to the proper Python installation: 
    > py -3.6 -m pip install python-obs

    > py -3.6 -m pip install websockets==9.1

    > pip install obs-websocket-py

    - Make sure the installation number matches your own 


Scripts location: C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts
Python install location: C:\Users\evans\AppData\Local\Programs\Python



























WSL- Not Using 
1. Install WSL Ubuntu from the Microsoft Store 
2. WSL will require you to make an account 
3. Once this is done try running WSL by typing "wsl" 
4. Make sure WSL is up to date: wsl --update 
5. If it opends with a new prompt such as "samevans@DESKTOP-ELS67E4:~$ [Cursor here]", you're good to move on 
6. If not, troubleshoot: 
    6.1. End the task forcefully: "taskkill /IM wslservice.exe /F" 
    6.2. Shut down WSL: "wsl --shutdown" 
    6.3. Type: "wsl --set-version <DistroName> 2" 
    6.4. Type: "wsl --set-default-version 2" 
    6.5. Wait for these to finish, which could take a few minutes 
    6.6. Make sure it's shut down: "wsl --shutdown" 
    6.7. Make sure of WSL's version and status info: 
        6.7.1. Type: "wsl --status" 
        6.7.2. Type: "wsl --list --verbose" 
    6.8. Start WSL: "wsl -d Ubuntu" 
    6.9. Hopefully it's working now, if not give up (jk, I'll add more) 
7. Open either the Ubuntu app or type use "wsl -d Ubuntu"/"wsl" to open a WSL instance in PowerShell (Admin) 
8. Check if Python is installed: "python3 --version"/"which python3" 
9. Install PIP (Python Installs PIP): "sudo apt install python3-pip" 
10. 


sudo apt install python3-venv
cd /mnt/c/Users/colum/Desktop
mkdir obs-python
cd obs-project
python3 -m venv .venv
source .venv/bin/activate
python -m pip install python-obs
python -m pip install obsws-python
