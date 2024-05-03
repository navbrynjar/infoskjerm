Filer til infoskjermen på kontoret


For å kjøre .py fila på Raspberry Pien ved boot, kjør:

````
sudo nano /etc/rc.local
````

og legg til følgende over `exit 0`:

````
cd /path/to/your/repository
git pull
python3 /path/to/your/script.py &
````
