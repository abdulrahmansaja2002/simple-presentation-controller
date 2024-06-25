# Simple Presentation Controller

This is a simple presentation controller that uses the arrow keys to navigate through slides. It is written in Python and uses the [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html) library to handle keyboard input.

## How to run
- Install Python 3
- Download and install all dependencies by running `pip install -r requirements.txt`
- Run the script by running `python main.py` or `python3 main.py` (depending on your system)

## How to use
- Connect your phone or tablet to the same network as the server (e.g. by connecting to the same Wi-Fi network)
- Find the server IP address by running `ipconfig` on Windows or `ifconfig` on Linux
![ipconfig](/images/ipconfig.png)

- Open a browser and navigate to `http://<server_ip>:5000` in your phone or tablet browser
![browser](/images/browser.png)
- In the server computer, open the presentation you want to control and press `F11` (or another way) to enter full screen mode
- By using your phone or tablet (that is connected to the server network), you can now navigate through the slides by clicking left or right arrows on the web page

## How it works
This aplication uses a simple client-server architecture. The server is a Python script that uses the [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html) library to handle keyboard input. The client is a web page that uses JavaScript to send arrow key presses to the server. The server then uses the arrow key presses to navigate through the slides.
