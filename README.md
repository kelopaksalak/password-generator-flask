
## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kelopaksalak/password-generator-flask.git
   cd password-generator-flask
   ```

2. **(Optional but recommended) Create and activate a virtual environment**

   On Windows (PowerShell):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   On macOS / Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the app

1. Make sure your virtual environment is activated (if you created one).
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to:
   ```text
   http://127.0.0.1:5000
   ```

## How to use

1. Open the app in your browser.
2. Choose the **password length** using the slider.
3. Select the **password settings** you want (lowercase, uppercase, numbers, symbols).
4. Click **Generate** to create a new password.
5. Click the **copy button** next to the password field to copy the generated password to your clipboard.