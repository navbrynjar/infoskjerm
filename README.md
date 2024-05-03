Filer til infoskjermen på kontoret


For å kjøre .py fila på Raspberry Pien ved boot, kjør:

````
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
````

og legg til følgende over `exit 0`:

````
@lxterminal -e "bash -c 'cd ~/Desktop/infoskjerm; git pull; source ~/Desktop/infoskjerm/venv/bin/activate; python3 ~/Desktop/infoskjerm/infoskjerm.py; exec bash'"
````
