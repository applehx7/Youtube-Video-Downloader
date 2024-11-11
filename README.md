# YouTube Video Downloader

This is a **YouTube Video Downloader** built using **Python**, **Tkinter** for the graphical user interface (GUI), and **Pytube** for downloading videos from YouTube. The app allows users to easily input a YouTube URL and download videos to their local machine.


## Installation

### 1. Clone the Repository

If you haven't already cloned the repository, use the following command to clone it to your local machine:

```bash
git clone https://github.com/yourusername/Youtube-Video-Downloader.git
cd Youtube-Video-Downloader
```

### 2. Set Up the Virtual Environment

First, create and activate a virtual environment. This will isolate the dependencies required for this project from your system's Python environment.

- **On Windows**:
  Open Command Prompt (or PowerShell) and run:

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

- **On macOS/Linux**:
  Open a terminal and run:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Once the virtual environment is activated, install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all the required libraries, such as:

- `pytube`: A lightweight Python library for downloading videos from YouTube.
- `tkinter`: A built-in Python library for creating graphical user interfaces (GUIs).
- `pillow`: A Python Imaging Library (PIL) fork for handling images in the app.

---

## Usage

### Running the Application

Once your environment is set up and the dependencies are installed, you can run the application by executing the following command:

```bash
python app.py
```

This will launch the graphical user interface (GUI) of the YouTube Video Downloader. You can then:

1. Enter the YouTube video URL.
2. Choose the download quality (e.g., highest resolution).
3. Click the "Download" button to start downloading the video to your local machine.

---

## Project Details

### `app.py`

This is the main script that runs the **Tkinter** GUI and handles interactions with **Pytube** to download videos. It also utilizes **Pillow** to handle any image-related functionality in the GUI.

### `requirements.txt`

This file contains all the required libraries and their versions for this project, including:

- `pytube`: The library used to download videos from YouTube.
- `tkinter`: The standard library for creating the graphical user interface (GUI) in Python.
- `pillow`: A library for image processing and handling within the app.

---

## Notes

- **Tkinter** is used for the GUI, and it comes pre-installed with Python in most systems. However, on some Linux distributions (e.g., Ubuntu), it may need to be installed separately. You can install Tkinter by running:

  - **Ubuntu/Debian**:
    ```bash
    sudo apt install python3-tk
    ```

  - **Fedora**:
    ```bash
    sudo dnf install python3-tkinter
    ```

- **Pillow** is used for image processing. If you run into issues with Pillow installation, make sure you have the necessary dependencies for image handling.

- **Pytube**: If you encounter any issues with Pytube, check the official [Pytube GitHub repository](https://github.com/pytube/pytube) for the latest updates, as the library may be updated periodically due to changes on YouTube's side.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Additional Notes

If you want to **create a standalone executable** (like a `.exe` for Windows), you can use **PyInstaller** or a similar tool to bundle the app into an executable file. You may need to follow additional steps for packaging, especially for including external files (like images) within the executable.

