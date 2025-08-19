# 📄 AI-Powered Resume Analyzer

An **AI Resume Analyzer** built with **Flask** and **OpenRouter (DeepSeek/GPT-4o-mini)**.  
Upload a PDF resume along with a job description, and the app will analyze it using AI:

- ✅ Extract key skills from the resume  
- ✅ Rate how impactful the projects are (score 1–10)  
- ✅ Check alignment with the job description (score out of 100)  
- ✅ Suggest improvements to the resume  
- ✅ Recommend 5 job titles suitable for the candidate  

---

## 🚀 Live Demo
🔗 [Click Here to Try the Demo](https://ai-powered-resume-analyzer-hrs-1.onrender.com)  

---



## 🛠️ Tech Stack
- **Backend**: Flask (Python)  
- **AI Model**: [OpenRouter](https://openrouter.ai/) – using `gpt-4o-mini`  
- **PDF Processing**: [pdfplumber](https://github.com/jsvine/pdfplumber)  
- **Frontend**: HTML + Jinja Templates  
- **Environment**: Python-dotenv for API key handling  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/PradeepPradeep1234/AI_Powered_Resume_Analyzer_HRs.git
cd AI_Powered_Resume_Analyzer_HRs
