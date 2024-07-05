import mss
import os
from datetime import datetime,date,time
import cv2
import numpy as np
import time










def folder():
    path = r'C:\temp'
    os.chdir(path)
    data = datetime.now().strftime("%d-%m-%y")
    name_folder = data
    os.mkdir(name_folder)
    os.chdir(data)



def screenshot():
    while True:
        dt_atual = datetime.now().strftime("%H-%M-%S")
        nome_img = "screenshot" + dt_atual
        with mss.mss() as sct:
            mon = sct.monitors[0]

            # The screen part to capture
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": 0,
            }
            output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

            sct_img = sct.grab(monitor)
            img = np.array(sct.grab(monitor))

            cv2.imwrite( nome_img + ".jpg", img)
        time.sleep(5)



path = r'C:\temp'
os.chdir(path)
data = datetime.now().strftime("%d-%m-%y")
diretorio_procurado = data

if os.path.exists(diretorio_procurado) and os.path.isdir(diretorio_procurado):
    os.chdir(diretorio_procurado)
    screenshot()
else:
    folder()
    screenshot()



