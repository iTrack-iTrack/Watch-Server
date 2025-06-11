# Watch-Server

The Watch-Server repository is a project that collects sensor information from the watch that is has uploaded to, insert the data into the database, and gives the live data for websites that handle that.

## Setup

The following are required for this project.

- [Python](https://www.python.org/)
- [Systemd](https://systemd.io/)

## Usage

Before the Server can be run, there exists much setup to be done.

Firstly, a virtual environment will need to be created such that the current Python installation doesn't get corrupted by dependency issues, thus execute `python3 -m venv build` which will create a `build` directory that houses Python executables and binaries. Next, the necessary that are mandatory will need to be installed, thus execute `./build/bin/python3 -m pip install -r requirements.txt`. Finally, can the user be able to run the application by running `./build/bin/python3 ./src/main.py`.

In the case that the user wishes to have the Watch-Server always be in the background of the Operating System, a systemd service file exists from the user to use. To use it, use the command `sudo mv Watch-Server.service /etc/systemd/system/`, then run `sudo systemctl daemon-reload` to update the list of available services, execute `sudo systemctl enable Watch-Server.service` to have the service run on boot, and finally `sudo systemctl start Watch-Server.service` to execute the service and make it run in the background.
