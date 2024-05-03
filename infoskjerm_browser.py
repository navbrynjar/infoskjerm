# python file to keep infoskjerm running and swapping between tabs

import webbrowser
import time
import pyautogui


# quarto_infoskjerm = "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#infoskjerm"

nettsider = {
    "quarto_infoskjerm": "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#infoskjerm",
    # 'grafana_spenn': "https://grafana.nav.cloud.nais.io/d/d1961678-a775-469a-8718-92082ee6f3ba/airflow-profilering?orgId=1&var-namespace=team-spenn-vans&from=now-2d&to=now",
    "quarto_stonads": "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#stonadsmottakere",
    "yr_oslo": "https://www.yr.no/nb/v%C3%A6rvarsel/timetabell/1-72837/Noreg/Oslo/Oslo/Oslo?i=0",
}

mac = False
cmd = "command" if mac else "ctrl"

pause_tid = 10  # seconds

def main():

    # open the quarto to load the connection / login
    webbrowser.open(nettsider["quarto_infoskjerm"])
    time.sleep(30)

    # open all tabs
    for tab in nettsider.values():
        webbrowser.open(tab)
        time.sleep(.5)

    # on startup the default quarto page is opened, which we don't want
    with pyautogui.hold(cmd):
        pyautogui.press("1")
        time.sleep(1)
        pyautogui.press("w")

    loop = 0
    tab_numbers = [str(i) for i in range(1, len(nettsider) + 1)]

    try:
        while True:
            for number in tab_numbers:
                with pyautogui.hold(cmd):
                    pyautogui.press(number)  # switch tab
                    if loop % 10 == 0:
                        pyautogui.press("r")  # refresh
                time.sleep(pause_tid)
            loop += 1
    except KeyboardInterrupt:
        print("Exiting the loop")
        pass
    except Exception as e:
        print("An error occurred:", e)
        pass

    print("finito")


if __name__ == "__main__":
    main()
