# AutoPaint

**AutoPaint** is a simple and intuitive tool to automatically color rows in Excel spreadsheets (`.xlsx`) based on the value of a column. It features a graphical user interface with **drag and drop** support and is bundled as a standalone `.exe` file for Windows — no Python installation required.

---

## How to Use

1. **Open the `auto-paint.exe` file** and trust antivirus.
2. **Drag and drop a `.xlsx` file** into the window, or **click the central icon** to manually select a file.
3. The file will be automatically processed.
4. A message will appear showing the name of the newly generated file.

---

## Features

- ✔️ Modern GUI built with `Tkinter`
- ✔️ Drag and drop support using `tkinterdnd2`
- ✔️ Custom window and taskbar icon
- ✔️ Compatible with Excel and LibreOffice `.xlsx` files
- ✔️ Bundled into a single executable using `PyInstaller`

---

## Requirements (for development only)

If you want to run the project from the source code:

- Python 3.10 or newer
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## How to Build the Executable

To create the `.exe` file, run:

```bash
pyinstaller --onefile --windowed ^
--icon=assets/icon.ico ^
--add-data "assets;assets" ^
--add-data "C:/Users/YOUR_USERNAME/AppData/Roaming/Python/Python311/site-packages/tkinterdnd2/tkdnd;tkinterdnd2/tkdnd" ^
main.py
```

> Replace the path to the `tkdnd` library with the correct one for your environment.

---

## Project Structure

```
auto-paint/
├── auto_paint/
│   ├── AutoPaint.py
│   ├── AutoPaintWindow.py
│   └── ...
├── assets/
│   ├── icon.ico
│   └── drop_icon.png
├── main.py
└── README.md
```

---

## License

This project is intended for personal and educational use only. No license has been defined.

---

## Author

Developed by **Eduardo Pinheiro** — Computer Science student at UERJ.<br>
developed to my mother <3
