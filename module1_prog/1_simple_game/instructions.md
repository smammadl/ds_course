Instructions for the simple game project:
1. Press windows key and type *anaconda powershell* and open it.
2. Copy and paste following after `>`:
```bash
conda create -n pygame_env python=3.11
```
3. Press Enter.
>**Note:** Here we are simply creating a new environment named `pygame_env` (for pygame) and installing Python 3.11 in it. If prompted, press `y` and then press Enter.
4. Copy and paste following after `>`:
```bash
conda activate pygame_env
```
5. Press Enter.
>**Note:** Or choose one of your existing environments and activate it. Anything other than `base` is fine.
6. Copy and paste following after `>`:
```bash
pip install pygame
```
7. Press Enter.
8. Create a new folder in your workspace and name it `simple_game`.
9. Inside the `simple_game` folder, create a new file and name it `snake_game.py`. Pay attention to the file extension.
10. Start writing the code for the game.
11. Save the file.
12. Navigate to the `simple_game` folder in the anaconda powershell terminal by typing `cd C:\Users\your_username\Desktop\div\simple_game`. Make sure to replace `your_username` with your actual username.
13. Run the game by typing `python snake_game.py`.