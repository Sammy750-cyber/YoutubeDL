import sys
import os
import yt_dlp
import time
os.system("clear || cls")
class color:
    RED='\033[91m'
    YELLOW='\033[93m'
    UNDERLINE='\033[4m'
    GREEN='\033[92m'
    BLUE='\033[94m'
    PURPLE='\033[95m'
    BOLD='\033[1m'
    DARKCYAN='\033[36m'
    END='\033[0m'
def downloadV():
    print(f"{color.BOLD}{color.BLUE}==============================================={color.END}")
    url = input(f"{color.PURPLE}[{color.BOLD}{color.GREEN}>>{color.END}{color.PURPLE}] {color.DARKCYAN}URL {color.END}{color.GREEN}>")
    ydl_opts ={}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
       try:
        print(f"{color.BOLD}{color.BLUE}==============================================={color.END}")
        print(f"{color.PURPLE}[{color.BOLD}{color.GREEN}+{color.END}{color.PURPLE}] {color.GREEN}Download In Progress...{color.END}{color.GREEN}")
        ydl.download(url)
       except:
          print(f"{color.RED}An Error occured....!!!{color.END}")

logo= (f"""{color.GREEN}
███████╗ ██████╗██╗    ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔════╝██╔════╝██║    ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████╗██║     ██║ █╗ ██║███████║███████║██║     █████╔╝ 
╚════██║██║     ██║███╗██║██╔══██║██╔══██║██║     ██╔═██╗ 
███████║╚██████╗╚███╔███╔╝██║  ██║██║  ██║╚██████╗██║  ██╗
╚══════╝ ╚═════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}DEVELOPER{color.END}     {color.BOLD}:{color.END}  {color.GREEN} SCWhack {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}GITHUB{color.END}        {color.BOLD}:{color.END}  {color.GREEN} Sammy750-cyber {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}VERSION{color.END}       {color.BOLD}:{color.END}  {color.GREEN} 1.0 {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}TELEGRAM{color.END}      {color.BOLD}:{color.END}  {color.GREEN} NOGROUPYET {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}TOOL'S NAME{color.END}   {color.BOLD}:{color.END}  {color.GREEN} Youtube_Video_Downloader {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}STATUS{color.END}        {color.BOLD}:{color.END}  {color.GREEN} FREE {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
{color.BLUE}[{color.END}{color.PURPLE}01/A{color.END}{color.BLUE}]{color.END} {color.GREEN} Download Video {color.END}
{color.BLUE}[{color.END}{color.PURPLE}02/B{color.END}{color.BLUE}]{color.END} {color.GREEN} Contact Developer {color.END}
{color.BLUE}[{color.END}{color.PURPLE}03/C{color.END}{color.BLUE}]{color.END} {color.GREEN} More Tools {color.END}
{color.BLUE}[{color.END}{color.PURPLE}{color.RED}04/X{color.END}{color.BLUE}]{color.END} {color.GREEN} {color.RED}Exit Programme {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
""")

for i in logo:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.0001) 
user_input=input(f"{color.BLUE}{color.BOLD}[{color.GREEN}>{color.BLUE}]{color.END} {color.GREEN}CHOOSE: ")
user_input=user_input.replace(' ','')
if user_input == "01" or user_input == "a" or user_input == "A" or user_input == "1":
   downloadV()
elif user_input == "02" or user_input == "b" or user_input == "B" or user_input == "2":
   os.system("xdg-open https://t.me/redwaren5")
elif user_input == "03" or user_input == "c" or user_input == "C" or user_input == "3":
   os.system("xdg-open https://Github.com/sammy750-cyber")
elif user_input ==  "04" or user_input == "x" or user_input == "X" or user_input == "4":
   sys.exit()
else:
   print(f"{color.RED}Invalid Input!!! {color.END}")
   sys.exit()
