
#!/usr/bin/env python3

import os
import time
import subprocess

def restart_tor():
    print("[*] در حال راه‌اندازی مجدد سرویس Tor ...")
    os.system("sudo systemctl restart tor")
    time.sleep(2)
    print("[+] Tor راه‌اندازی شد.")

def change_identity():
    print("[*] در حال ارسال سیگنال NEWNYM ...")
    subprocess.call(['sudo', 'killall', '-HUP', 'tor'])
    print("[+] آدرس IP تغییر کرد (اگر Tor به‌درستی پیکربندی شده باشد).")

def main():
    while True:
        print("
1. راه‌اندازی مجدد Tor")
        print("2. تغییر IP (NEWNYM)")
        print("3. خروج")
        choice = input("یک گزینه را انتخاب کن: ")
        if choice == "1":
            restart_tor()
        elif choice == "2":
            change_identity()
        elif choice == "3":
            break
        else:
            print("گزینه نامعتبر!")

if __name__ == "__main__":
    main()
