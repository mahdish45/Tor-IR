#!/bin/bash

echo "[+] نصب Tor در حال انجام است ..."
sudo apt update
sudo apt install -y tor

echo "[+] دادن دسترسی اجرای برنامه"
chmod +x tor_ir.py

echo "[+] ساخت symlink برای اجرای آسان از هر مسیر"
sudo ln -sf "$(pwd)/tor_ir.py" /usr/local/bin/tor-ir

echo "[✅] نصب با موفقیت انجام شد. برای اجرا کافیست بنویسید:"
echo "    tor-ir"
