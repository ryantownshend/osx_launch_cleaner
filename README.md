# osx_launch_cleaner
Ferret out all the launch plist files.

Polls the launch folders :

    /Library/LaunchAgents/
    /Library/LaunchDaemons/
    ~/Library/LaunchAgents/

Installs a command called `olc` if pip installed.

Requires python3.

Installation :

    pip3 install git+https://github.com/ryantownshend/osx_launch_cleaner --upgrade