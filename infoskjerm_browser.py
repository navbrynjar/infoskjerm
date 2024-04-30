# python file to keep infoskjerm running and swapping between tabs

import webbrowser
import time
import pyautogui


quarto_infoskjerm = "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#infoskjerm"
grafana_spenn = "https://grafana.nav.cloud.nais.io/d/d1961678-a775-469a-8718-92082ee6f3ba/airflow-profilering?orgId=1&var-namespace=team-spenn-vans&from=now-2d&to=now"

mac = True
cmd = "command" if mac else "ctrl"


def main():

    # open a new tab with the infoskjerm
    webbrowser.open(quarto_infoskjerm)
    # close the first tab, which is the default tab
    time.sleep(2)
    with pyautogui.hold(cmd):
        pyautogui.press(["1", "w"])

    # open the remaining tabs
    webbrowser.open(grafana_spenn)

    # looping over the tabs to keep them alive
    tabs = ["1", "2"]
    # tab 1 is infoskjerm
    # tab 2 is grafana
  
    loop = 0

    try:
        while True:
            for tab in tabs:
                with pyautogui.hold(cmd):
                    pyautogui.press(tab)
                    if loop % 10 == 0:
                        pyautogui.press("r")
                time.sleep(10)
            loop += 1
    except KeyboardInterrupt:
        print("Exiting the loop")
        pass
    except Exception as e:
        print("An error occurred:", e)
        pass

    webbrowser.open(quarto_infoskjerm)
    print("finito")


if __name__ == "__main__":
    main()
