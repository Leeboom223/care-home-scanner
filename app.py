from flask import Flask, render_template_string
import os

app = Flask(__name__)

# The path to the report your scanner creates
REPORT_FILE = 'audit_results.txt'

# Professional HTML template for the dashboard
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Care Home Security Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 20px; }
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        .meta { color: #7f8c8d; font-size: 0.9em; margin-bottom: 20px; }
        pre { background: #2d3436; color: #dfe6e9; padding: 20px; border-radius: 5px; overflow-x: auto; font-size: 1.1em; line-height: 1.5; }
        .alert { color: #ff7675; font-weight: bold; }
        .footer { margin-top: 30px; font-size: 0.8em; color: #bdc3c7; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Care Home IoT Security Audit</h1>
        <div class="meta">System Status: Active | Dashboard Version 1.0</div>
        
        <h3>Latest Audit Findings:</h3>
        <pre>{{ content }}</pre>

        <div class="footer">
            Developed by Chibuzor Nnoli | Teesside University MSc Cybersecurity | © 2026
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    if os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, 'r') as f:
            content = f.read()
    else:
        content = "No audit report found. Please run scanner.py first."
    
    return render_template_string(HTML_TEMPLATE, content=content)

if __name__ == '__main__':
    # Runs the server on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)