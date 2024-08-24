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
    name = entry_string_var_3.get()
    video_format = file_format_var.get()
    platform = platform_var.get()  


    ydl_opts = {
        'outtmpl': f'{directory}/{name}.%(ext)s',
        'progress_hooks': [progress_hook],
        'ffmpeg_location': "C:\\lat_vat\\ffmpeg-2024-08-15-git-1f801dfdb5-essentials_build\\bin\\ffmpeg.exe",  # tùy đường dẫn người dùng tải
    }
    
 # Định dạng và chất lượng video
   
    if resolution:
        ydl_opts["format"] = 'bestvideo[height<=' + resolution.replace("p","") + "]"
    else:
        ydl_opts["format"] = 'bestvideo'

    if video_format == "mp4":
        ydl_opts["format"] += "[ext=mp4]+bestaudio[ext=m4a]/best"
    else:
        ydl_opts["format"] += "[ext=webm]+bestaudio[ext=webm]/best"

    # if video_format == 'mp4':
    #     if resolution == '360p':
    #         ydl_opts['format'] = 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best'
    #     elif resolution == '480p':
    #         ydl_opts['format'] = 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best'
    #     elif resolution == '720p':
    #         ydl_opts['format'] = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best'
    #     else:
    #         ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'
    # else:
    #     if resolution == '360p':
    #         ydl_opts['format'] = 'bestvideo[height<=360][ext=webm]+bestaudio/best'
    #     elif resolution == '480p':
    #         ydl_opts['format'] = 'bestvideo[height<=480][ext=webm]+bestaudio/best'
    #     elif resolution == '720p':
    #         ydl_opts['format'] = 'bestvideo[height<=720][ext=webm]+bestaudio/best'
    #     else:
    #         ydl_opts['format'] = 'bestvideo[ext=webm]+bestaudio/best'
    
    
    
    
    # Hiển thị thông tin nền tảng nếu cần
    if platform == "YouTube":
        info_label.config(text="YouTube: Videos will be downloaded from YouTube.")
    elif platform == "Tiktok":
        info_label.config(text="Tiktok: Videos will be downloaded from Tiktok.")
    elif platform == "Dailymotion":
        info_label.config(text="Dailymotion: Videos will be downloaded from Dailymotion.")
    elif platform == "Facebook":
        info_label.config(text="Facebook: Videos will be downloaded from Facebook.")
    else:
        info_label.config(text="Unknown platform.")
    
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
window.title('Save video')
font_sytle = ("Helvetica", 12, "bold")



# URL_Entry
URL_label = Label(window, text="URL: ", font=font_sytle)
URL_label.grid(column=1, row=1, sticky='W')
entry_string_var_1 = StringVar()
URL_entry = Entry(window, textvariable=entry_string_var_1, width=45)
URL_entry.grid(column=2, row=1)

# Resolution_Entry
resolution_label = Label(window, text="Choose resolution: ", font=font_sytle)
resolution_label.grid(column=1, row=2, sticky='W')
entry_string_var_2 = StringVar()
res_entry = Entry(window, textvariable=entry_string_var_2, width=45)
res_entry.grid(column=2, row=2)

# Video_Name_Entry
name_label = Label(window, text='Video name:', font=font_sytle)
name_label.grid(column=1, row=3, sticky='W')
entry_string_var_3 = StringVar()
name_entry = Entry(window, textvariable=entry_string_var_3, width=45)
name_entry.grid(column=2, row=3)

# Directory_Entry
diraction_label = Label(window, text="Save to directory:", font=font_sytle)
diraction_label.grid(column=1, row=4, sticky='W')
diraction_entry = StringVar()
dir_entry = Entry(window, textvariable=diraction_entry, width=45)
dir_entry.grid(column=2, row=4, sticky='W')
select_dir_button = Button(window, text="Browse", font=font_sytle, width=10, relief='raised', command=select_directory)
select_dir_button.grid(column=3, row=4, sticky='W')

# Resolution_Buttons
res_360p_button = Button(window, text="360p", font=font_sytle, relief='raised', width=10, command=res_360p)
res_360p_button.grid(column=1, row=5, sticky='W')

res_480p_button = Button(window, text="480p", font=font_sytle, relief='raised', width=10, command=res_480p)
res_480p_button.grid(column=2, row=5)

res_720p_button = Button(window, text="720p", font=font_sytle, relief='raised', width=10, command=res_720p)
res_720p_button.grid(column=3, row=5, sticky='E')

# Download_Button
download_button = Button(window, text='Download', font=font_sytle, relief='raised', width=10, command=download_video)
download_button.grid(column=2, row=9)

# Success_and_Error_Labels
success_label = Label(window, text="", fg="green", font=font_sytle)
success_label.grid(column=1, row=12, columnspan=3, pady=10)

error_label = Label(window, text="", fg="red", font=font_sytle)
error_label.grid(column=1, row=12, columnspan=3)

# Progress_Bar
progress_bar = Progressbar(window, orient=HORIZONTAL, length=500, mode='determinate')
progress_bar.grid(column=1, row=13, columnspan=3, pady=10)


# Video_Type
file_format_label = Label(window, text="Select format:", font=font_sytle)
file_format_label.grid(column=1, row=6, sticky='W')

file_format_var = StringVar(value="mp4")  # Biến lưu định dạng được chọn, mặc định là mp4
file_format_menu = OptionMenu(window, file_format_var, "mp4", "webm")
file_format_menu.config(width=11)
file_format_menu.grid(column=2, row=6)

# Thêm lựa chọn nền tảng
platform_label = Label(window, text="Select Platform:", font=font_sytle)
platform_label.grid(column=1, row=8, sticky='W')

platform_var = StringVar(value="YouTube")  # Biến lưu nền tảng được chọn, mặc định là YouTube
platform_menu = OptionMenu(window, platform_var, "YouTube", "Tiktok", "Dailymotion", "Facebook")
platform_menu.config(width=11)
platform_menu.grid(column=2, row=8)

# Thêm thông tin nền tảng
info_label = Label(window, text="", font=font_sytle)
info_label.grid(column=1, row=11, columnspan=3)



window.mainloop()
