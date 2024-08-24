import yt_dlp
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar

def res_360p():
    entry_string_var_2.set('360p')


def res_480p():
    entry_string_var_2.set('480p')


def res_720p():
    entry_string_var_2.set('720p')


def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_string_var.set(directory)


def download_video():
    link = entry_string_var_1.get()
    resolution = entry_string_var_2.get()
    directory = dir_string_var.get()

    if not directory:
        error_label.config(text="Please select a directory to save the video.")
        return

    ydl_opts = {
        'outtmpl': f'{directory}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook]
    }

    try:
        # Configure download options for specific resolution
        if resolution == '360p':
            ydl_opts['format'] = 'best[height<=360]'
        elif resolution == '480p':
            ydl_opts['format'] = 'best[height<=480]'
        elif resolution == '720p':
            ydl_opts['format'] = 'best[height<=720]'
        else:
            ydl_opts['format'] = 'best'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)  # link will be processed here
            title = info.get('title', 'No title found')
            success_label.config(text=f"Downloaded: {title}")
            error_label.config(text="")  # Clear error message
    except Exception as e:
        error_label.config(text=f"An error occurred: {e}")
        success_label.config(text="")  # Clear success message


def progress_hook(d):
    if d['status'] == 'downloading':
        percent_complete = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        progress_bar['value'] = percent_complete
        window.update_idletasks()  # Update the GUI

window = Tk()
window.geometry('400x500')

# Styling the labels
URL_label = Label(window, text="URL from YouTube:", font=("Helvetica", 12, "bold"))
URL_label.grid(column=1, row=1, padx=10, pady=5, sticky=W)

resolution_label = Label(window, text="Choose resolution:", font=("Helvetica", 12, "bold"))
resolution_label.grid(column=1, row=2, padx=10, pady=5, sticky=W)

dir_label = Label(window, text="Save to directory:", font=("Helvetica", 12, "bold"))
dir_label.grid(column=1, row=3, padx=10, pady=5, sticky=W)

entry_string_var_1 = StringVar()
URL_entry = Entry(window, textvariable=entry_string_var_1, width=35, font=("Helvetica", 12))
URL_entry.grid(column=2, row=1, padx=10, pady=5)

entry_string_var_2 = StringVar()
res_entry = Entry(window, textvariable=entry_string_var_2, width=35, font=("Helvetica", 12))
res_entry.grid(column=2, row=2, padx=10, pady=5)

dir_string_var = StringVar()
dir_entry = Entry(window, textvariable=dir_string_var, width=35, font=("Helvetica", 12))
dir_entry.grid(column=2, row=3, padx=10, pady=5)

select_dir_button = Button(window, text="Browse...", font=("Helvetica", 10, "bold"), width=10, relief='raised', command=select_directory)
select_dir_button.grid(column=3, row=3, padx=5, pady=5)

# Styled Buttons
button_style = {'font': ("Helvetica", 10, "bold"), 'width': 10, 'relief': 'raised', 'padx': 5, 'pady': 5}

res_360p_button = Button(window, text="360p", **button_style, command=res_360p)
res_360p_button.grid(column=1, row=4, padx=5, pady=5)

res_480p_button = Button(window, text="480p", **button_style, command=res_480p)
res_480p_button.grid(column=2, row=4, padx=5, pady=5)

res_720p_button = Button(window, text="720p", **button_style, command=res_720p)
res_720p_button.grid(column=3, row=4, padx=5, pady=5)

download_button = Button(window, text='Download', font=("Helvetica", 12, "bold"), width=15, relief='raised', padx=10, pady=5, command=download_video)
download_button.grid(column=1, row=5, columnspan=3, pady=15)

# Labels for displaying success and error messages
success_label = Label(window, text="", fg="green", font=("Helvetica", 12))
success_label.grid(column=1, row=6, columnspan=3, pady=10)

error_label = Label(window, text="", fg="red", font=("Helvetica", 12))
error_label.grid(column=1, row=7, columnspan=3)

# Progress bar for displaying download progress
progress_bar = Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.grid(column=1, row=8, columnspan=3, pady=10)

window.mainloop()
