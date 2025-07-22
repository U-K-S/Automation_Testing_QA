### 🧾 **Project Description**

A complete Selenium-based UI test automation framework for 
(https://automationexercise.com), built using Python and PyTest. The project covers critical e-commerce flows 
like login, signup, add to cart, search, and checkout, all structured using the Page Object Model (POM). 
It includes HTML test reporting, Jenkins CI integration, and webhook testing via Ngrok.

---

### ✅ **Project Summary: Selenium Automation for AutomationExercise.com

---

### 🔧 **Framework Setup**

* Configured **Python 3.10+** environment
* Installed and used **Selenium WebDriver** for browser automation
* Installed and configured **ChromeDriver** for testing in Google Chrome
* Used **PyTest** as the test runner and assertion library
* Followed the **Page Object Model (POM)** structure for better code organization
* Created:

  * `pages/` directory for page-level actions
  * `tests/` directory for PyTest scripts
  * `utilities/locators.py` for storing all page locators centrally
* Implemented a reusable **WebDriver fixture** in `conftest.py`

---

### 🧪 **Test Cases Implemented

1. ✅ Login – Valid credentials
2. ✅ Login – Invalid credentials
3. ✅ Login Out 
4. ✅ Signup– New user
5. ✅ Add to Cart 
6. ✅ Remove product from cart 
7. ✅ Checkout_after_login
8. ✅ Checkout Without Login 
9. ✅ Product Search – Valid keyword
10. ✅ Product Search – No match

---

### 🖥️ **Advanced Selenium Usage**

* Handled `ElementClickInterceptedException` by:

* Scrolling with `scrollIntoView`
* Using JavaScript click fallback
* Used `WebDriverWait` and `ExpectedConditions` to handle dynamic loading
* Ensured reliable element interaction even when ads or overlays were present
* Implemented conditional test logic based on test outcome

Sure! Here's a **bullet-point summary** of the **headless browser setup and screenshot capture on test failure** for your Selenium automation project:

---

### 🧪 **Headless Mode + Screenshot on Failure – Summary**

---

#### ✅ **Headless Browser Setup**

* Configured **Chrome in headless mode** using Selenium's `Options()` class
* Useful for running tests in:

  * CI tools (e.g., Jenkins, GitHub Actions)
  * Headless servers without a GUI
* Browser options used:

  * `--headless` – disables GUI
  * `--disable-gpu` – improves stability (especially on Windows)
  * `--window-size=1920,1080` – ensures full page is rendered even in headless mode

---

#### ✅ **Screenshot Capture on Test Failure**

* Automatically takes a **screenshot when a test fails**
* Screenshot is saved in the `/screenshots` directory with the test name
* Implemented using `pytest_runtest_makereport()` hook in `conftest.py`
* Screenshot is attached to the **HTML report** generated via `pytest-html`

---

#### ✅ **How It Works**

* If any test fails, the test hook:

  * Accesses the active `driver`
  * Captures a PNG screenshot
  * Saves it using the test’s name
  * Embeds it inside the HTML test report

---

#### 🧪 **How to Run Tests in Headless Mode**

* Make sure the ChromeDriver is configured with `--headless` in `conftest.py`

---

### 🌐 **Webhooks + Tunneling (Ngrok)**

* Integrated **Ngrok** to expose localhost to the public internet
* Used Ngrok to create a **temporary secure URL** to:

  * Allow Jenkins or external tools to trigger test jobs via **webhooks**
  * Test webhook-based automation flows end-to-end
* Verified webhook delivery by listening on Ngrok tunnel in real-time
* Enabled external tools (e.g., GitHub, Postman, Jenkins) to hit webhook endpoints during live tests

---

### 🔁 **CI/CD Integration with Jenkins**

* Installed Jenkins and created a test automation job
* Configured Jenkins to:

  * Pull code
  * Run PyTest commands
  * Generate HTML test reports using `pytest-html`
  * Archive and display test reports
* Sample `Jenkinsfile` created for pipeline-based execution

---

### 📊 **Test Reporting**

* Generated **detailed HTML reports** using `pytest-html`

  * Shows pass/fail status, duration, and test names
* Reports archived automatically in Jenkins builds

---

### 📂 **Test Execution**

* Run full suite: `pytest tests/`
* Run single file: `pytest tests/test_cart.py`
* Generate report: `pytest --html=reports/report.html`

---





