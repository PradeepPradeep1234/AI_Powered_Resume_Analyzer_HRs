import os
import pdfplumber
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'resume_uploads'
API_KEY = os.getenv("DEEPSEEK_API_KEY")  # Replace with your OpenRouter key

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def analyze_resume_with_ai(resume_text, job_desc):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Resume: {resume_text}
    
    Job Description: {job_desc}

    As an HR AI assistant:
    1. Extract the candidate's key skills.
    2. Rate how impactful the projects are (score 1 to 10).
    3. Check how well the resume aligns with the job description (score out of 100).
    4. Suggest resume improvements.
    5. List 5 job titles this person is suitable for.
    """

    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {"role": "system", "content": "You are an expert HR resume evaluator."},
            {"role": "user", "content": prompt}
        ]
    }

    res = requests.post(url, headers=headers, json=data)
    if res.status_code == 200:
        return res.json()['choices'][0]['message']['content']
    else:
        return f"Error: {res.status_code}\n{res.text}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        job_desc = request.form['job_desc']
        file = request.files['resume']

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            resume_text = extract_text_from_pdf(file_path)
            result = analyze_resume_with_ai(resume_text, job_desc)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    os.makedirs('resume_uploads', exist_ok=True)
    app.run(debug=True)
