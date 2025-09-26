# simple-ai-interviewer

A minimal, easy-to-use AI-powered interview simulator that helps users practice interviews, receive real-time feedback, and improve interview skills.


## 📋 Project Overview
`simple-ai-interviewer` is a lightweight multi-agent system built with Autogen. It simulates a complete interview process with three core roles:
- **Interviewer**: Asks targeted questions (technical skills, problem-solving, cultural fit) based on the job position.
- **Candidate**: You (the user) respond to interview questions interactively.
- **Career Coach**: Provides constructive feedback on your answers and summarizes performance after the interview.

Designed for simplicity and learnability—perfect for students, job seekers, or anyone looking to practice interview skills.


## ✨ Key Features
- **Multi-Role Collaboration**: Automated interviewer + real user candidate + AI career coach.
- **Lightweight & Fast**: Uses `gpt-4o-mini` for balance of performance and cost.
- **Real-Time Feedback**: Career coach offers instant suggestions after each response.
- **Controlled Flow**: Automatically ends after 3 interview questions (via `TERMINATE` signal).
- **Easy Customization**: Modify job position, interview questions, or model with minimal code changes.


## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- An OpenAI API key (sign up [here](https://platform.openai.com/))
- `git` (for cloning the repo)


### 1. Clone the Repository
```bash
git clone https://github.com/XiaomingX/simple-ai-interviewer.git
cd simple-ai-interviewer
```


### 2. Install Dependencies
Create a virtual environment (optional but recommended) and install required packages:
```bash
# Create virtual env (Windows)
python -m venv venv
venv\Scripts\activate

# Create virtual env (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `requirements.txt` file in the project root with these dependencies:
```txt
autogen>=0.2.0
python-dotenv>=1.0.0
asyncio>=3.4.3
```


### 3. Configure Environment Variables
Create a `.env` file in the project root to store your OpenAI API key (never commit this file to GitHub!):
```env
# .env file
OPENAI_API_KEY=your-openai-api-key-here
```


## 🎯 How to Use
1. **Run the Interview**
   ```bash
   python main.py
   ```

2. **Interview Flow**
   1. The interview starts automatically with the interviewer asking the first question.
   2. Type your answer when prompted (as the candidate) and press Enter.
   3. The career coach will provide feedback on your answer.
   4. Repeat until the interviewer asks 3 questions and ends with `TERMINATE`.
   5. The career coach will then summarize your overall performance.


## ⚙️ Customization
Tweak the tool to fit your needs by modifying `main.py`:

| Customization Item       | How to Modify                                                                 |
|--------------------------|-------------------------------------------------------------------------------|
| **Job Position**         | Change the `job_position` variable (e.g., "Data Analyst", "Frontend Developer"). |
| **AI Model**             | Update `model="gpt-4o-mini"` to another model (e.g., "gpt-4o" for better performance). |
| **Number of Questions**  | Adjust the interviewer's system prompt (look for "总共问3个问题").              |
| **Feedback Length**      | Modify the career coach's system prompt (look for "内容控制在100字以内").        |


## 🛠️ Tech Stack
- **Core Framework**: [Autogen](https://microsoft.github.io/autogen/) (multi-agent collaboration)
- **LLM**: OpenAI GPT-4o-mini (configurable)
- **Environment Management**: `python-dotenv`
- **Async Handling**: `asyncio`


## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.


## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 📞 Support
If you run into issues:
1. Check the [Autogen Documentation](https://microsoft.github.io/autogen/) for common problems.
2. Open an [Issue](https://github.com/your-username/simple-ai-interviewer/issues) in the repo with details about your problem.
