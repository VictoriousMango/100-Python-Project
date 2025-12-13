import os
import subprocess
import pandas as pd
import json
from dotenv import load_dotenv
load_dotenv()
# --- Configuration ---
# The folder where your Matplotlib plots are saved
DATA_FOLDER = os.getenv('dataFolder')
PYTHON_FILE = os.getenv('playGround')
OUTPUT_FOLDER = os.getenv('outputFolder')
TEMPLATE_HTML_FILE = os.getenv('template')
print("#"*10+"Removing Existing png files")
OUTPUT_HTML_FILE = "gallery.html"
TOPIC = "Testing Period"
ABSTRACT = '''
Aim - Testing this Program
'''
CONCLUSION = '''
Demonstraiton Completed Successfully
'''
for file in os.listdir(DATA_FOLDER):
    if file.endswith(".png") or file.endswith(".csv") or file.endswith(".json") or file.endswith(".txt"):
        os.remove(os.path.join(DATA_FOLDER, file))
        print(f"Removed: {file},", end=" ")
print()
# The name of the HTML file to create
def fillPNGfiles(data):
    imgFiles = [f'<div class="image-item"><a href="{os.path.join(DATA_FOLDER, img).replace("pages/", "")}" target="_blank"><img src="{os.path.join(DATA_FOLDER, img).replace("pages/", "")}" alt="{img}"></a><p>{img.replace(".png", "")}</p></div>' for img in os.listdir(DATA_FOLDER) if img.endswith(".png")]
    csvFiles = [os.path.join(DATA_FOLDER, csv) for csv in os.listdir(DATA_FOLDER) if csv.endswith(".csv")]
    jsonFiles = [os.path.join(DATA_FOLDER, csv) for csv in os.listdir(DATA_FOLDER) if csv.endswith(".json")]
    txtFiles = [os.path.join(DATA_FOLDER, csv) for csv in os.listdir(DATA_FOLDER) if csv.endswith(".txt")]
    imgFiles = "\n".join(imgFiles)
    imgFiles_wrapper = f'''
        <div class="section">
            <div class="section-header">
                <div class="section-icon">🖼️</div>
                <h2 class="section-title">Visual Assets</h2>
            </div>
            <button class="toggle-btn" onclick="toggleImageLayout()">Toggle Layout</button>
            <div class="image-grid" id="imageGrid">
                {imgFiles}
            </div>
        </div>
        ''' if imgFiles else ''
    with open(PYTHON_FILE, 'r') as f:
        code = f.read()
    commentHighlighter = [f'<div class="comment block">{code_line}</div>' if "#" in code_line else code_line for code_line in code.split("\n")]
    code = "\n".join(commentHighlighter)
    if '"""' in code:
        code = code.replace('"""', "'''")
    if "'''" in code:
        multiLineComment = [f'<div class="comment block">{code_segment}</div>' if index%2 else code_segment for index, code_segment in enumerate(code.split("'''"))]
        code = "'''".join(multiLineComment)
    code_wrapper = f'''
        <div class="section">
            <div class="section-header">
                <div class="section-icon">💻</div>
                <h2 class="section-title">Python Implementation</h2>
            </div>
            <div class="code-container">
                <div class="code-header">
                    🐍 Python Code
                </div>
                <div class="code-block">
                <pre><code>{code}</code></pre>
                </div>
            </div>
        </div>''' if len(code) else ''
    # code = code.replace("'''", "<hr>'''<hr>")
    # code = code.replace('"""', '<hr>"""<hr>')
    csv_Data = ''
    for index, file in enumerate(csvFiles):
        df = pd.read_csv(file)
        csv_Data += f'''
        <div class="table-container">
            {df.to_html()}
            <p>Table {index+1}: {file.split("/")[-1].replace(".csv", "")}</p>
        </div>
        <br>
        '''
    csv_Data_wrapper = f'''
    <div class="section">
        <div class="section-header">
            <div class="section-icon">📊</div>
            <h2 class="section-title">Data Tables</h2>
        </div>
        {csv_Data}
    </div>
    <hr>''' if len(csv_Data) else ''
    json_data = ''
    def json_formatter(raw_json):
        if isinstance(raw_json, dict):
            for key in raw_json:
                raw_json[key] = json_formatter(raw_json[key])
        elif isinstance(raw_json, list):
            for key in range(len(raw_json)):
                raw_json[key] = json_formatter(raw_json[key])
        elif isinstance(raw_json, str):
            raw_json = f"<div class='json-string'>{raw_json}</div>"
        elif isinstance(raw_json, (int, float)):
            raw_json = f"<div class='json-number'>{raw_json}</div>"
        return raw_json
    for index, file in enumerate(jsonFiles):
        with open(file, 'r') as f:
            json_raw_data = json.load(f)
            print(json.dumps(json_raw_data, indent=4))
            json_formated_data = json.dumps(json_formatter(json_raw_data), indent=4)
            json_data += f"""
            <div class="json-container">
                <pre><code>{json_formated_data}</code></pre>
            </div>
            """
    JSON_wapper = f'''
    <div class="section">
        <div class="section-header">
            <div class="section-icon">🔧</div>
            <h2 class="section-title">Configuration Data</h2>
        </div>
        {json_data}
    </div>
    '''

    terminal_Data = ''
    for index, file in enumerate(jsonFiles):
        with open(file, 'r') as f:
            terminal_Data += f"<pre><code>{f.read()}</pre></code>"
    for index, file in enumerate(txtFiles):
        with open(file, 'r') as f:
            terminal_Data += f"<pre><code>{f.read()}</pre></code>"
    terminal_Data_wrapper = f'''
    <h3>Terminal/JSON Data</h3>
    <hr>
    <div class="json-container">
        {terminal_Data}
    </div>
    <hr>''' if len(terminal_Data) else ''
    data = data.replace("Placeholder_TOPIC", TOPIC)
    data = data.replace("Placeholder_ABSTRACT", ABSTRACT)
    data = data.replace("Placeholder_ImageGrid", imgFiles_wrapper)
    data = data.replace("Placeholder_Code", code_wrapper)
    data = data.replace("Placeholder_Table", csv_Data_wrapper)
    data = data.replace("Placeholder_JSON", JSON_wapper)
    data = data.replace("Placeholder_Terminal", terminal_Data_wrapper)
    data = data.replace("Placeholder_CONCLUSION", CONCLUSION)
    return data
print("#"*10+"Reading Template")
with open(TEMPLATE_HTML_FILE, 'r', encoding='utf-8') as f:
    data = f.read()
print("#"*10+"Running Simulation")
subprocess.run(["python", PYTHON_FILE])
print("#"*10+"Generating HTML Report")
with open(os.path.join(OUTPUT_FOLDER, OUTPUT_HTML_FILE), 'w', encoding='utf-8') as f:
    f.write(fillPNGfiles(data))
