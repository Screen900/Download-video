import subprocess
import os
import pyfiglet
import socket  # للتحقق من الاتصال بالإنترنت
import re  # للتحقق من صحة URL

# دالة للتحقق من الاتصال بالإنترنت
def check_internet():
    try:
        socket.create_connection(("www.google.com", 80))  # محاولة الاتصال بـ Google
        return True
    except OSError:
        return False

# دالة للتحقق من صحة URL
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # تحقق من البروتوكول (http, https)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]*[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # تحقق من النطاق
        r'localhost|' # أو localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # أو عنوان IP
        r'?[A-F0-9]*:[A-F0-9:]+?)' # أو عنوان IPv6
        r'(?::\d+)?' # تحقق من رقم المنفذ (اختياري)
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

# دالة لتحميل الفيديو
def download_video(url):
    try:
        # مسح الشاشة
        os.system("clear")

        # التأكد من أن الإنترنت متصل
        if not check_internet():
            print(f"{bcolors.RED}❌ No internet connection. Please check your connection.{bcolors.RESET}\n")
            return
        
        # التحقق من صحة الرابط
        if not is_valid_url(url):
            print(f"{bcolors.RED}❌ Invalid URL. Please check the URL and try again.{bcolors.RESET}\n")
            return

        # تحديد مسار مجلد "Download" في جهازك
        download_folder = "/storage/emulated/0/Download"  # مسار مجلد "Download"
        
        # التأكد من أن المجلد موجود
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        # تحميل الفيديو وحفظه في المجلد المحدد
        print("\n⬇️ Downloading video... Please wait ⬇️\n")
        result = subprocess.run(["yt-dlp", "-o", os.path.join(download_folder, "%(title)s.%(ext)s"), url], check=True)
        
        # الحصول على اسم الفيديو المحفوظ
        video_name = result.args[-1].split('/')[-1]
        print(f"\n✅ Video downloaded successfully!\n")
        
        # إضافة ملاحظة للمستخدم
        print(f"{bcolors.GREEN}🎥 Your video has been saved in the folder:{bcolors.RESET}\n")
        print(f"{bcolors.CYAN}📁 {download_folder}{bcolors.RESET}\n")
        print(f"{bcolors.YELLOW}🔹 Video name: {video_name}{bcolors.RESET}\n")
        print(f"\n{bcolors.MAGENTA}Thank you for using the Video Downloader! 😊{bcolors.RESET}\n")

    except Exception as e:
        print(f"{bcolors.RED}❌ Error: {e}{bcolors.RESET}\n")

# تعريف الألوان
class bcolors:
    GREEN = '\033[32m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    RED = '\033[31m'
    RESET = '\033[0m'

# دالة لطلب إدخال الرقم 1 أو 2 بشكل صحيح
def get_valid_choice():
    while True:
        try:
            choice = input(f"\n{bcolors.YELLOW}Choose an option (1/2): {bcolors.RESET}")
            if choice not in ['1', '2']:
                print(f"{bcolors.RED}❗ Invalid choice! Please choose either 1 or 2.{bcolors.RESET}\n")
            else:
                return choice
        except ValueError:
            print(f"{bcolors.RED}❗ Please enter a valid number (1 or 2).{bcolors.RESET}\n")

# دالة الرئيسة
def main():
    # مسح الشاشة قبل بداية التشغيل
    os.system("clear")
    
    # استخدام pyfiglet لكتابة اسم الأداة بشكل جميل
    ascii_art = pyfiglet.figlet_format("Video Downloader")
    print(f"{bcolors.MAGENTA}{ascii_art}{bcolors.RESET}")
    
    # إضافة النص "by Screen" تحت اسم الأداة
    print(f"{bcolors.CYAN}by Screen{bcolors.RESET}")
    
    print(f"{bcolors.CYAN}===================================={bcolors.RESET}")
    print(f"{bcolors.GREEN}1. Download YouTube video{bcolors.RESET}")
    print(f"{bcolors.GREEN}2. Download TikTok video{bcolors.RESET}")

    choice = get_valid_choice()

    try:
        url = input(f"\n{bcolors.YELLOW}Enter the video URL: {bcolors.RESET}")

        if choice == "1":
            print(f"\n{bcolors.CYAN}🚀 Downloading YouTube video...{bcolors.RESET}")
            download_video(url)
        elif choice == "2":
            print(f"\n{bcolors.CYAN}🚀 Downloading TikTok video...{bcolors.RESET}")
            download_video(url)

    except Exception as e:
        print(f"{bcolors.RED}❌ Error: {e}{bcolors.RESET}\n")

if __name__ == "__main__":
    main()