Instructions for the desktop app project:
1. Press windows key and type *anaconda powershell* and open it.
2. Copy and paste following after `>`:
```bash
conda create -n tk python=3.11
```
3. Press Enter.
>**Note:** Here we are simply creating a new environment named `tk` (for tkinter) and installing Python 3.11 in it. If prompted, press `y` and then press Enter.
4. Copy and paste following after `>`:
```bash
conda activate tk
```
5. Press Enter.
>**Note:** Or choose one of your existing environments and activate it. Anything other than `base` is fine.
6. Copy and paste following after `>`:
```bash
pip install ttkbootstrap, pyinstaller
```
7. Press Enter.
>**Note:** Python comes with tkinter library. So there is no need to install it. `ttkbootstrap` is a library that provides a modern and customizable theme for tkinter. `pyinstaller` is a tool that converts Python scripts into executable files.
8. Create a new folder in your workspace and name it `simple_desktop_app`.
9. Inside the `simple_desktop_app` folder, create a new file and name it `miles_to_km.py`. Pay attention to the file extension.
10. Start writing the code for the app.
11. Save the file.
12. Navigate to the `simple_desktop_app` folder in the anaconda powershell terminal by typing `cd C:\Users\your_username\Desktop\div\simple_desktop_app`. Make sure to replace `your_username` with your actual username.
13. Run the app by typing `python miles_to_km.py`.
14. To build the app, type `pyinstaller --onefile --windowed .\miles_to_km.py`.
>**Note:** `--onefile` option creates a single executable file. `--windowed` option creates a windowed application.
15. Navigate to the `dist` folder in explorer and double click on the executable file to run the app.