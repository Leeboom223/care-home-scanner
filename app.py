from flask import Flask, render_template, redirect, url_for
import os
import subprocess

app = Flask(__name__)
REPORT_FILE = "audit_results.txt"

@app.route('/')
def index():
    if not os.path.exists(REPORT_FILE):
        return "<h1>Error: Run a scan to generate report.</h1>"

    with open(REPORT_FILE, "r") as f:
        content = f.read()

    # Split using the delimiter from scanner.py
    sections = content.split("-" * 60)
    
    # Clean the summary and details for the browser
    summary = sections[1].strip() if len(sections) > 1 else "Awaiting Data..."
    details = [d.strip() for d in sections[2:] if d.strip()]

    return render_template('dashboard.html', summary=summary, details=details)

@app.route('/run-scan')
def run_scan():
    # Executes the updated targeted scanner
    subprocess.run(["python3", "scanner.py"])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)