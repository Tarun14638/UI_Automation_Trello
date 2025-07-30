# UI_Automation_Trello
This Selenium-based automation script performs end-to-end actions on Trello to simulate a basic QA workflow. It includes board creation, list and card setup, labeling, attachment handling, card movement, and validation — all while ensuring reliability and repeatability.

# Trello UI Automation – Python + Selenium

This script automates the process of logging into Trello, creating a new Scrum board with the current timestamp, adding three default lists (`To Do`, `In Progress`, and `Done`), creating cards in each list, attaching a PDF to a card, labeling the card, and finally moving the card between lists using the quick card editor.

---

## ✅ Features Covered

- Trello Login (Email/Password)
- Scrum Board Creation
- List and Card Creation
- Adding Descriptions and Labels
- Attaching Files (PDF)
- Drag & Drop Simulation with Click-based Move
- Automated Card Movement Across Lists

---

## 🔧 Requirements

- Python 3.8+
- Firefox browser installed
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) installed and available in system PATH
- Internet connection

### 🧪 Python Packages

Install required packages using `pip`:

```bash
pip install selenium

Folder Structure
TrelloAutomation/
├── UI_Automation_Code_Trello.py
├── Get_Started_With_Smallpdf.pdf
├── README.md


