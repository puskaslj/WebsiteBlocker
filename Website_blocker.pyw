import time
from datetime import datetime

hosts_test = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

work_start = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8)
work_end = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16)
current_time = datetime.now()

while True:

    if work_start < current_time < work_end:
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        print("Working hours.")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Time off.")

    time.sleep(5)

#To complete the program, add the file to the Windows Task Schedule, set it to run on startup and give it the highest priveleges. 