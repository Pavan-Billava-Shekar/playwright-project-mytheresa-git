# 🧪 Playwright Mytheresa Automation Project

## 📖 Overview
This project is an **end-to-end (E2E) test automation framework** built with **Playwright**, **Python**, and **Pytest**, designed to validate key user journeys and functionalities on the **QA Engineer - Technical Challenge** for web application.

The goal of this framework is to provide a **scalable**, **modular**, and **maintainable** automation suite that supports:
- Functional and regression testing  
- Cross-browser and headless testing  
- HTML report generation and screenshots for failed tests  

The testcase covered in this automation are 

1.As a tester, I want to make sure there are no console errors when you visit
	https://pocketaces2.github.io/fashionhub/

2.As a tester, I want to check if a page is returning the expected status code
	○ Fetch each link (e.g. <a href=””/> on
	https://pocketaces2.github.io/fashionhub/) and visit that link to verify that:
	the page returns 200 or 30x status codes
	the page returns no 40x status codes

3.As a customer, I want to verify I can log in to
	https://pocketaces2.github.io/fashionhub/login.html
	
4.As a product owner, I want to see how many open pull requests are there for our product. You
	can use https://github.com/appwrite/appwrite/pulls as an example product
	Output is a list of PR in CSV format with PR name, created date and author

	Note:This testcase are covered in two ways (API and UI)


---

## 🧰 Tech Stack
- **Language:** Python 3.x  
- **Framework:** [Playwright for Python](https://playwright.dev/python/)  
- **Test Runner:** Pytest  
- **Reporting:** Pytest HTML / Allure / custom reports  
- **Design Pattern:** Page Object Model (POM)  
- **Version Control:** Git  

---

## 📂 Project Structure

```
playwright-project-mytheresa-git/
│
├── assets/                # Screenshots, attachments, and data files
├── config/                # Configuration files (e.g., env settings, base URLs)
├── pages/                 # Page Object Model classes
├── reports/               # Test results and reports (HTML, JSON, etc.)
├── tests/                 # Test cases grouped by feature or module
│   ├── api/ 
│   ├   └── test_login.py
│   ├── test_login.py
│   ├── test_console_errors.py
│   └── ...
│
├── conftest.py            # Global Pytest fixtures and hooks
├── requirements.txt       # Project dependencies
├── report.html            # Example HTML report (auto-generated)
└── README.md              # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash

git clone https://github.com/<your-username>/playwright-project-mytheresa.git
cd playwright-project-mytheresa-git
```

### 2️⃣ Create & Activate a Virtual Environment
```bash

python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash

pip install -r requirements.txt
```

### 4️⃣ Install Playwright Browsers
```bash

playwright install
```

---

## ▶️ Running the Tests

### Run All Tests
```bash

pytest
```

### Run Tests in Headless Mode (Default)
```bash

pytest --headed
```

### Run Specific Test File
```bash

pytest tests/test_login.py
```

### Generate HTML Report
```bash

pytest --html=reports/report.html --self-contained-html
```

---
### Run Test with Any environment and Any browser
```bash(eg: environment -production, browser - firefox)

pytest --env=production --browser_name=firefox --html=report.html -v
```

---
## 🧩 Configuration

All environment or project-specific settings are managed inside the **`config/`** directory.  
You can define:
- Base URLs
- Browser settings (Chromium, Firefox, WebKit)
- Timeout values
- Test environment details (e.g., `staging`, `production`)

Fixtures and reusable setup logic are defined in **`conftest.py`**.

---

## 📊 Reports & Logs

After execution, reports are generated under:

```
reports/
├── report.html       # Pytest HTML report
├── logs/             # Optional logs if configured
└── screenshots/      # Screenshots on failure
```

To open the report:
```bash
open reports/report.html
```

---

## 🧱 Page Object Model (POM)

Each page of the application is represented by a class under the **`pages/`** directory.  
This ensures **modularity** and **code reusability**.  

---

## 🚀 CI/CD Integration (Optional)

To run tests in CI environments (GitHub Actions, Jenkins, GitLab CI):
- Install dependencies using `pip install -r requirements.txt`
- Run tests via `pytest --html=reports/report.html`
- Optionally, upload the HTML report as a CI artifact

---

## 🧑‍💻 Contribution Guidelines

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/<feature-name>
   ```
2. Write and run tests locally.
3. Ensure linting and formatting are consistent.
4. Submit a pull request for review.

---

