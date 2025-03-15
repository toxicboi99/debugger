# Multi-Language Debugger

A web-based debugger that allows you to write and execute code in multiple programming languages, including **Python, JavaScript, PHP, C++, and Java**. Built using **Flask for backend processing** and a **dynamic front-end UI**.

## 🌟 Features
- **Supports multiple languages:** Python, JavaScript, PHP, C++, Java
- **User-friendly interface:** Dynamic UI with animated language selection
- **Run code instantly:** Real-time debugging and execution
- **Easy to set up:** Simple installation and configuration

---

## 🛠️ Step 1: Set Up Your Environment
Ensure the following are installed on your system:

- **Python** (for Flask backend) → [Download](https://www.python.org/downloads/)
- **Node.js** (for JavaScript execution) → [Download](https://nodejs.org/)
- **PHP** (for PHP execution) → [Download](https://www.php.net/downloads)
- **G++ (GNU Compiler)** (for C++ execution) → Included in [MinGW](https://www.mingw-w64.org/)
- **Java (JDK)** (for Java execution) → [Download](https://www.oracle.com/java/technologies/javase-downloads.html)

### ✅ Check Installations:
Run the following commands in your terminal to verify installation:
```bash
python --version
node --version
php --version
g++ --version
javac -version
```

If any of the versions are missing, download and install them using the links above.

---

## 📂 Step 2: Create the Project
Open **VS Code** and run the following commands in the terminal:
```bash
# Create the project folder
mkdir multi-debugger
cd multi-debugger

# Create necessary files
touch app.py
mkdir templates static

# Create front-end files
touch templates/index.html static/style.css static/script.js
```

---

## 🚀 Step 3: Install Flask
We will use Flask to create the backend for our debugger.

Run the following command to install Flask:
```bash
pip install Flask
```

If `pip` is not recognized, try:
```bash
python -m pip install Flask
```

---

## 📝 Step 4: Set Up the Files
### 🔹 Backend - `app.py`
Handles debugging logic for different programming languages.

### 🔹 Frontend - `templates/index.html`
Provides the UI for users to select a language and input code.

### 🔹 Styling - `static/style.css`
Adds animations, layout, and responsive design.

### 🔹 Client-Side Logic - `static/script.js`
Handles user interactions and sends requests to the backend.

Copy your respective code into these files.

---

## ▶️ Step 5: Run the Debugger
In VS Code, open the **terminal (Ctrl + `)** and start the Flask server:
```bash
python app.py
```
If everything is correct, you should see:
```bash
 * Running on http://localhost:5000
```

---

## 🌍 Step 6: Test the Multi-Language Debugger
Open your browser and go to:
```bash
http://localhost:5000
```

- Select a **programming language** from the sidebar.
- Paste your **code** into the text editor.
- Click **Run Code** to execute and see the output.

---

## 🎯 Future Enhancements
- Add **more programming languages**.
- Improve **UI animations and user experience**.
- Implement **real-time collaboration** using WebSockets.

---

## ❤️ Contributing
If you'd like to contribute, feel free to **fork the repository** and submit a **pull request**. Feedback and suggestions are always welcome! 😊

---

## 📜 License
This project is licensed under the **MIT License**.

**Happy Coding! 🚀🎉**

