# Log Health Tool (Git & GitHub Advanced Assignment)

## 📌 Project Overview
This project is a Python-based Log Analysis & Data Health Tool.  
It reads application logs from a CSV file, analyzes them, and prints:

- Total log count  
- Summary of log levels (INFO, WARNING, ERROR)  
- Logs grouped by hour  

The project was built to demonstrate advanced Git concepts such as:
- Branch isolation  
- Git stash  
- Hotfix workflow  
- Safe task switching  
- Controlled merging  

---

## 📁 Project Structure


log_health_tool/
data/
app_logs.csv
src/
loader.py
analyzer.py
reporter.py
README.md


---

## 🔹 Phase 1: Base Tool Setup
- Created project structure  
- Implemented CSV loader in `loader.py`  
- Printed total log count  
- Committed and pushed to main branch  

Output:


Total logs loaded: 200


---

## 🔹 Phase 2: Branch Isolation Proof
- Created feature branch: `feature-error-summary`  
- Added logic to count:
  - INFO  
  - WARNING  
  - ERROR  
- Verified that main branch did NOT contain this feature before merge  

Proof:
- Running `python src/analyzer.py` on `main` showed no summary  
- Feature existed only in `feature-error-summary` branch  

---

## 🔹 Phase 3: Git Stash (Task Interruption)
While working on the feature branch, time-based grouping logic was started but not completed.

To simulate task interruption:
- Unfinished work was saved using:



git stash
git stash list


- Switched to main branch  
- Created hotfix branch: `hotfix-log-loader`  
- Fixed CSV loader bug (handled empty CSV safely)  
- Committed and merged hotfix into main  

---

## 🔹 Phase 4: Restore Stashed Work
- Switched back to `feature-error-summary`  
- Restored unfinished work using:



git stash apply


- Completed time-based grouping feature  
- Committed feature branch  
- Merged feature branch into main  

---

## 🧠 Git Concepts Demonstrated
- Branch isolation  
- Git stash  
- Hotfix workflow  
- Safe task switching  
- Controlled merging  

---

## ✅ Final Result
Main branch contains:
- CSV loader  
- Log level summary  
- Logs grouped by hour  
- Hotfix for empty CSV  
- Clean Git history  

---

## 📦 Deliverables
- GitHub repository with:
  - Feature branch commits  
  - Hotfix branch commit  
  - Merge commits  
- README explanation  
- Proof of branch isolation and stash usage  

---

## 🚀 How to Run



python src/analyzer.py

python src/loader.py

✅ FINAL STEP (VERY IMPORTANT)

Run these commands:

git add README.md
git commit -m "Add README explaining git stash, branches, and workflow"
git push
