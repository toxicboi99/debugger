import os
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Create a temp directory for code execution
os.makedirs("temp", exist_ok=True)

# Run the code based on language
def run_code(language, code):
    output = ""
    try:
        if language == "python":
            exec_globals = {}
            exec(code, {}, exec_globals)
            output = str(exec_globals)
        elif language == "javascript":
            with open("temp/code.js", "w") as f:
                f.write(code)
            output = subprocess.check_output(["node", "temp/code.js"], stderr=subprocess.STDOUT).decode()
        elif language == "php":
            with open("temp/code.php", "w") as f:
                f.write(code)
            output = subprocess.check_output(["php", "temp/code.php"], stderr=subprocess.STDOUT).decode()
        elif language == "cpp":
            with open("temp/code.cpp", "w") as f:
                f.write(code)
            subprocess.run(["g++", "temp/code.cpp", "-o", "temp/code"], check=True)
            output = subprocess.check_output(["./temp/code"], stderr=subprocess.STDOUT).decode()
        elif language == "java":
            with open("temp/Main.java", "w") as f:
                f.write(code)
            subprocess.run(["javac", "temp/Main.java"], check=True)
            output = subprocess.check_output(["java", "-cp", "temp", "Main"], stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    except Exception as e:
        output = str(e)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debug', methods=['POST'])
def debug():
    data = request.json
    language = data.get('language')
    code = data.get('code')

    output = run_code(language, code)

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
