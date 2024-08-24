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
        diraction_entry.set(directory)

def download_video():
    link = entry_string_var_1.get()
    resolution = entry_string_var_2.get()
    directory = diraction_entry.get()

    ydl_opts = {
        'outtmpl': f'{directory}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'ffmpeg_location': "C:\\lat_vat\\ffmpeg-2024-08-15-git-1f801dfdb5-essentials_build\\bin\\ffmpeg.exe",  # tùy đường dẫn người dùng tải
    }


    if resolution == '360p':
        ydl_opts['format'] = 'bestvideo[height<=360][ext = mp4]+bestaudio[ext = m4a]/best'
    elif resolution == '480p':
        ydl_opts['format'] = 'bestvideo[height<=480][ext = mp4]+bestaudio[ext = m4a]/best'
    elif resolution == '720p':
        ydl_opts['format'] = 'bestvideo[height<=720][ext = mp4]+bestaudio[ext = m4a]/best'
    else:
        ydl_opts['format'] = 'bestvideo[ext = mp4]+bestaudio[ext = m4a]/best'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            title = info.get('title', 'No title found')
            success_label.config(text=f"Downloaded: {title}")
            error_label.config(text="")

    except Exception as e:
        error_label.config(text=f"An error occurred: {e}")
        success_label.config(text="")




# tạo cái thanh process
def progress_hook(d):
    if d['status'] == 'downloading':
        percent_complete = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        progress_bar['value'] = percent_complete
        window.update_idletasks()


# Giao diện
window = Tk()
window.title('P.Save video')
font_sytle = ("Helvetica", 12, "bold")
URL_label = Label(window, text="URL from YouTube: ", font=font_sytle)
URL_label.grid(column=1, row=1)

resolution_label = Label(window, text="Choose resolution: ", font=font_sytle)
resolution_label.grid(column=1, row=2)

entry_string_var_1 = StringVar()
URL_entry = Entry(window, textvariable=entry_string_var_1, width=45)
URL_entry.grid(column=2, row=1)

entry_string_var_2 = StringVar()
res_entry = Entry(window, textvariable=entry_string_var_2, width=45)
res_entry.grid(column=2, row=2)

diraction_entry = StringVar()
dir_entry = Entry(window, textvariable=diraction_entry, width=45)
dir_entry.grid(column=2, row=3, sticky='W')

select_dir_button = Button(window, text="Browse", font=font_sytle, width=10, relief='raised',command=select_directory)
select_dir_button.grid(column=3, row=3, padx=5, pady=5)

res_360p_button = Button(window, text="360p", font=font_sytle, relief='raised', width=10, command=res_360p)
res_360p_button.grid(column=1, row=4, sticky='W')

res_480p_button = Button(window, text="480p", font=font_sytle, relief='raised', width=10, command=res_480p)
res_480p_button.grid(column=2, row=4)

res_720p_button = Button(window, text="720p", font=font_sytle, relief='raised', width=10, command=res_720p)
res_720p_button.grid(column=3, row=4)

download_button = Button(window, text='Download', font=font_sytle, relief='raised', width=15, command=download_video)
download_button.grid(column=2, row=5)

success_label = Label(window, text="", fg="green", font=font_sytle)
success_label.grid(column=1, row=6, columnspan=3, pady=10)

error_label = Label(window, text="", fg="red")
error_label.grid(column=1, row=7, columnspan=3)

progress_bar = Progressbar(window, orient=HORIZONTAL, length=500, mode='determinate')
progress_bar.grid(column=1, row=8, columnspan=3, pady=10)

diraction_label = Label(window, text="Save to directory:", font=font_sytle)
diraction_label.grid(column=1, row=3)

window.mainloop()
