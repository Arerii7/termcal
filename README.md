# Termcal

**Termcal** is a minimal, dependency-free terminal calendar written in pure Python.  
It displays a monthly calendar in the terminal, highlights today’s date, and supports adding simple notes per day.  
All without any external libraries — just Python and your terminal.

---

## ✨ Features

- ✅ **No dependencies** — only standard Python libraries
- 📅 **Monthly calendar** — clean and aligned terminal view
- 🟥 **Highlight today** — today’s date shown in red
- 📝 **Notes per date** — add, list, or delete notes for specific days
- 📤 **Persistent storage** — notes are saved in `~/.termcal/notes.json`
- ⏪⏩ **Month navigation** — view previous or next months

---

## 🖥️ Demo

```bash
$ termcal
      August 2025
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

Today: 02 August 2025

## ⚙️ Installation

```bash
git clone https://github.com/Arerii7/termcal.git
cd termcal
chmod +x termcal.py

## 📚 Usage
Command	Description
./termcal.py	Show calendar for current month
./termcal.py --next	Next month
./termcal.py --prev	Previous month
./termcal.py --year 2026 --month 1	Show specific month/year
./termcal.py --add YYYY-MM-DD "text"	Add note to a date
./termcal.py --delete YYYY-MM-DD	Delete note from a date
./termcal.py --list	List all saved notes

📄 License
This project is licensed under the MIT License.

🤝 Contributions
Feel free to submit issues or pull requests.
This project is small by design — ideal for learning, forking, or building on top of.

💡 Author
Made with ❤️ by Arerii7
GitHub: https://github.com/Arerii7
