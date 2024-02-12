<div align="center">
  <a href="#">
    <img src="./password-inspector-logo.png" alt="logo" height="135px">
  </a>
  <p align="center">
    <a
      href="https://github.com/bhaskar-soni/password-inspector/issues/new?assignees=&labels=bug">Report
      Bug</a>
    ·
    <a href="https://github.com/bhaskar-soni/password-inspector/issues">Request Feature</a>
  </p>

  <img alt="informer" src="https://img.shields.io/github/stars/bhaskar-soni/password-inspector">
  <img alt="informer" src="https://img.shields.io/github/issues/bhaskar-soni/password-inspector">
  <img alt="informer" src="https://img.shields.io/github/languages/code-size/bhaskar-soni/password-inspector">
  <img alt="informer" src="https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs">
  

</div>

<h3 align="center">Password Inspector: Test how much secure your password is</h3>

Welcome to the Password Inspector!, a tool that helps you evaluate the strength of your passwords and ensure they meet security standards.

## Features

- **Password Strength Assessment:** Evaluate the strength of your password based on various criteria.
- **Character Checkmarks:** Visual representation of password characteristics (uppercase, lowercase, numbers, symbols).
- **Time to Crack Estimation:** Estimate the time it would take for an attacker to crack your password.
- **Password Breach Check:** Check if your password has been previously leaked in breaches.

## Usage

**Clone Repository:**
   ```bash
   git clone https://github.com/bhaskar-soni/password-inspector.git
   cd password-inspector
  ```

**Install Dependencies:**
 ```bash
pip install -r requirements.txt
```
**Run Password Strength Checker:**
```bash
python3 password-inspector.py
```
**Follow On-Screen Instructions:**

Enter your password when prompted.
Review the assessment, checkmarks, and time-to-crack information.
Make adjustments to strengthen your password if needed.

**Example Output:**
```bash
Enter Password: mySecureP@ssw0rd

This password has not been previously leaked.

Audit: Pass

Password Strength: Strong
Password Length: 16 characters

Character Checkmarks:
Uppercase: ✔
Lowercase: ✔
Numbers: ✔
Symbols: ✔

Time to Crack: 2 years, 4 months, 15 days
```

## Contributing 💡

You can propose a feature request opening an issue or a pull request.
Bhaskar Soni (GitHub: @bhaskar-soni)
