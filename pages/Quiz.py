import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
import base64
from io import BytesIO
import json

# Page configuration
st.set_page_config(
    page_title="Exam Quiz System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .timer-display {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    # .quiz-container {
    #     background: #f8f9ff;
    #     padding: 2rem;
    #     border-radius: 15px;
    #     border-left: 5px solid #667eea;
    #     margin: 1rem 0;
    # }
    .question-card {
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0px 0px 5px rgba(255, 187, 175, 0.5);
        margin: 1rem 0;
    }
    
    .option-label {
        background: #e9ecef;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0.2rem 0;
        border-left: 3px solid #667eea;
    }
    
    .settings-panel {
        background: #f1f3f4;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
def init_session_state():
    if 'quiz_data' not in st.session_state:
        st.session_state.quiz_data = None
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'quiz_finished' not in st.session_state:
        st.session_state.quiz_finished = False
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'quiz_settings' not in st.session_state:
        st.session_state.quiz_settings = {}

init_session_state()

def load_html_template():
    """Load the HTML template for report generation"""
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Report Card</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .report-container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            font-weight: 300;
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .content {
            padding: 40px;
        }

        .score-section {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 15px;
            color: white;
        }

        .total-score {
            font-size: 4rem;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .score-details {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
        }

        .score-item {
            text-align: center;
        }

        .score-item h3 {
            font-size: 2rem;
            margin-bottom: 5px;
        }

        .score-item p {
            opacity: 0.9;
        }

        .performance-tables {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }

        .table-container {
            background: #f8f9ff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }

        .table-container h3 {
            margin-bottom: 20px;
            color: #333;
            font-size: 1.3rem;
            text-align: center;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            border-radius: 10px;
            overflow: hidden;
        }

        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }

        th {
            background: #667eea;
            color: white;
            font-weight: 600;
        }

        .excellent { background-color: #d4edda; color: #155724; }
        .good { background-color: #d1ecf1; color: #0c5460; }
        .average { background-color: #fff3cd; color: #856404; }
        .poor { background-color: #f8d7da; color: #721c24; }

        .questions-section {
            margin-top: 40px;
        }

        .questions-section h2 {
            color: #333;
            margin-bottom: 25px;
            font-size: 1.8rem;
            text-align: center;
        }

        .question-item {
            background: #f8f9ff;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            border-left: 5px solid #667eea;
        }

        .question-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .question-number {
            background: #667eea;
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
        }

        .question-status {
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.85rem;
            font-weight: bold;
        }

        .correct { background-color: #d4edda; color: #155724; }
        .incorrect { background-color: #f8d7da; color: #721c24; }
        .not-attempted { background-color: #e2e3e5; color: #495057; }

        .question-text {
            font-size: 1.1rem;
            margin-bottom: 15px;
            color: #333;
            line-height: 1.6;
        }

        .options {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 15px;
        }

        .option {
            padding: 12px 15px;
            border-radius: 8px;
            border: 2px solid #e9ecef;
        }

        .option.correct-answer {
            background-color: #d4edda;
            border-color: #28a745;
            font-weight: bold;
        }

        .option.user-answer {
            background-color: #f8d7da;
            border-color: #dc3545;
        }

        .option.user-answer.correct-answer {
            background-color: #d4edda;
            border-color: #28a745;
        }

        .explanation {
            background: #e9f7ff;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #007bff;
            margin-top: 15px;
        }

        @media (max-width: 768px) {
            .performance-tables {
                grid-template-columns: 1fr;
            }
            
            .score-details {
                flex-direction: column;
                gap: 20px;
            }
            
            .options {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="report-container">
        <div class="header">
            <h1>Quiz Performance Report</h1>
            <p>{{EXAM_NAME}} - {{SUBJECT_NAME}} {{TOPIC_NAME}}</p>
            <p>Completed on: {{DATE_TIME}}</p>
        </div>

        <div class="content">
            <div class="score-section">
                <div class="total-score">{{TOTAL_MARKS}}/{{MAX_MARKS}}</div>
                <p>Your Overall Score: {{PERCENTAGE}}%</p>
                <div class="score-details">
                    <div class="score-item">
                        <h3>{{CORRECT_COUNT}}</h3>
                        <p>Correct</p>
                    </div>
                    <div class="score-item">
                        <h3>{{INCORRECT_COUNT}}</h3>
                        <p>Incorrect</p>
                    </div>
                    <div class="score-item">
                        <h3>{{NOT_ATTEMPTED_COUNT}}</h3>
                        <p>Not Attempted</p>
                    </div>
                    <div class="score-item">
                        <h3>{{TIME_TAKEN}}</h3>
                        <p>Time Taken</p>
                    </div>
                </div>
            </div>

            <div class="performance-tables">
                <div class="table-container">
                    <h3>📚 Subject-wise Performance</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Subject</th>
                                <th>Score</th>
                                <th>Accuracy</th>
                            </tr>
                        </thead>
                        <tbody>
                            {{SUBJECT_PERFORMANCE_ROWS}}
                        </tbody>
                    </table>
                </div>

                <div class="table-container">
                    <h3>📖 Topic-wise Performance</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Topic</th>
                                <th>Score</th>
                                <th>Accuracy</th>
                            </tr>
                        </thead>
                        <tbody>
                            {{TOPIC_PERFORMANCE_ROWS}}
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="questions-section">
                <h2>📝 Detailed Question Analysis</h2>
                <div id="questions-container">
                    {{QUESTIONS_HTML}}
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""
    return template

def calculate_performance(df, user_answers, pos_marks, neg_marks):
    """Calculate quiz performance metrics"""
    results = {
        'total_questions': len(df),
        'attempted': len([ans for ans in user_answers.values() if ans is not None]),
        'correct': 0,
        'incorrect': 0,
        'total_marks': 0,
        'max_marks': len(df) * pos_marks,
        'subject_performance': {},
        'topic_performance': {}
    }
    
    for idx in range(len(df)):
        question = df.iloc[idx]
        user_answer = user_answers.get(idx)
        correct_answer = question['correct_option']
        
        subject = question['subject_name']
        topic = question['topic_name']
        
        # Initialize subject and topic tracking
        if subject not in results['subject_performance']:
            results['subject_performance'][subject] = {'total': 0, 'correct': 0, 'marks': 0}
        if topic not in results['topic_performance']:
            results['topic_performance'][topic] = {'total': 0, 'correct': 0, 'marks': 0}
        
        results['subject_performance'][subject]['total'] += 1
        results['topic_performance'][topic]['total'] += 1
        
        if user_answer is not None:
            if user_answer == correct_answer:
                results['correct'] += 1
                results['total_marks'] += pos_marks
                results['subject_performance'][subject]['correct'] += 1
                results['subject_performance'][subject]['marks'] += pos_marks
                results['topic_performance'][topic]['correct'] += 1
                results['topic_performance'][topic]['marks'] += pos_marks
            else:
                results['incorrect'] += 1
                results['total_marks'] += neg_marks
                results['subject_performance'][subject]['marks'] += neg_marks
                results['topic_performance'][topic]['marks'] += neg_marks
    
    results['not_attempted'] = results['total_questions'] - results['attempted']
    results['percentage'] = round((results['correct'] / results['total_questions']) * 100, 2)
    
    return results

def get_performance_class(accuracy):
    """Get CSS class based on accuracy percentage"""
    if accuracy >= 80:
        return 'excellent'
    elif accuracy >= 60:
        return 'good'
    elif accuracy >= 40:
        return 'average'
    else:
        return 'poor'

def generate_report_html(df, user_answers, quiz_settings, results, time_taken):
    """Generate complete HTML report"""
    template = load_html_template()
    
    # Get exam details
    exam_name = df['exam_name'].iloc[0] if 'exam_name' in df.columns else "Exam"
    subject_name = df['subject_name'].iloc[0] if len(df['subject_name'].unique()) == 1 else "Multiple Subjects"
    topic_name = df['topic_name'].iloc[0] if len(df['topic_name'].unique()) == 1 else "Multiple Topics"
    
    # Replace basic placeholders
    replacements = {
        '{{EXAM_NAME}}': exam_name,
        '{{SUBJECT_NAME}}': subject_name,
        '{{TOPIC_NAME}}': topic_name,
        '{{DATE_TIME}}': datetime.now().strftime("%B %d, %Y at %I:%M %p"),
        '{{TOTAL_MARKS}}': str(results['total_marks']),
        '{{MAX_MARKS}}': str(results['max_marks']),
        '{{PERCENTAGE}}': str(results['percentage']),
        '{{CORRECT_COUNT}}': str(results['correct']),
        '{{INCORRECT_COUNT}}': str(results['incorrect']),
        '{{NOT_ATTEMPTED_COUNT}}': str(results['not_attempted']),
        '{{TIME_TAKEN}}': time_taken
    }
    
    # Generate subject performance rows
    subject_rows = ""
    for subject, perf in results['subject_performance'].items():
        accuracy = round((perf['correct'] / perf['total']) * 100, 2) if perf['total'] > 0 else 0
        css_class = get_performance_class(accuracy)
        subject_rows += f"""
            <tr class="{css_class}">
                <td>{subject}</td>
                <td>{perf['marks']}/{perf['total'] * quiz_settings['pos_marks']}</td>
                <td>{accuracy}%</td>
            </tr>
        """
    
    # Generate topic performance rows
    topic_rows = ""
    for topic, perf in results['topic_performance'].items():
        accuracy = round((perf['correct'] / perf['total']) * 100, 2) if perf['total'] > 0 else 0
        css_class = get_performance_class(accuracy)
        topic_rows += f"""
            <tr class="{css_class}">
                <td>{topic}</td>
                <td>{perf['marks']}/{perf['total'] * quiz_settings['pos_marks']}</td>
                <td>{accuracy}%</td>
            </tr>
        """
    
    # Generate questions HTML
    questions_html = ""
    for idx in range(len(df)):
        question = df.iloc[idx]
        user_answer = user_answers.get(idx)
        correct_answer = question['correct_option']
        
        if user_answer is None:
            status = "not-attempted"
            status_text = "Not Attempted"
        elif user_answer == correct_answer:
            status = "correct"
            status_text = "Correct"
        else:
            status = "incorrect"
            status_text = "Incorrect"
        
        # Generate options HTML
        options_html = ""
        for opt in ['A', 'B', 'C', 'D']:
            option_text = question[f'option_{opt.lower()}']
            option_classes = ["option"]
            
            if opt == correct_answer:
                option_classes.append("correct-answer")
            if opt == user_answer:
                option_classes.append("user-answer")
            
            options_html += f"""
                <div class="{' '.join(option_classes)}">
                    <strong>{opt}.</strong> {option_text}
                </div>
            """
        
        explanation_html = ""
        if 'explanation' in question and pd.notna(question['explanation']):
            explanation_html = f"""
                <div class="explanation">
                    <strong>Explanation:</strong> {question['explanation']}
                </div>
            """
        
        questions_html += f"""
            <div class="question-item">
                <div class="question-header">
                    <span class="question-number">Q{idx + 1}</span>
                    <span class="question-status {status}">{status_text}</span>
                </div>
                <div class="question-text">{question['question']}</div>
                <div class="options">
                    {options_html}
                </div>
                {explanation_html}
            </div>
        """
    
    replacements['{{SUBJECT_PERFORMANCE_ROWS}}'] = subject_rows
    replacements['{{TOPIC_PERFORMANCE_ROWS}}'] = topic_rows
    replacements['{{QUESTIONS_HTML}}'] = questions_html
    
    # Apply all replacements
    html_content = template
    for placeholder, value in replacements.items():
        html_content = html_content.replace(placeholder, value)
    
    return html_content

def get_download_link(html_content, filename):
    """Generate download link for HTML file"""
    b64 = base64.b64encode(html_content.encode()).decode()
    return f'<a href="data:text/html;base64,{b64}" download="{filename}">📥 Download Report</a>'

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📚 Exam Quiz System</h1>
        <p>Upload questions, take quiz, and get detailed performance reports</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation
    with st.sidebar:
        st.header("Navigation")
        if not st.session_state.quiz_started:
            page = st.selectbox("Choose Section", ["📤 Upload & Settings", "ℹ️ Instructions"])
        elif st.session_state.quiz_started and not st.session_state.quiz_finished:
            page = "🎯 Quiz"
            st.info(f"Quiz in progress...")
        else:
            page = "📊 Results"
    
    if page == "📤 Upload & Settings" or (not st.session_state.quiz_started and page != "ℹ️ Instructions"):
        st.header("📤 Upload Questions & Configure Settings")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload your CSV file with questions",
            type=['csv'],
            help="CSV should contain: exam_name, subject_name, topic_name, question, option_a, option_b, option_c, option_d, correct_option"
        )
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                
                # Validate required columns
                required_columns = ['exam_name', 'subject_name', 'topic_name', 'question', 
                                  'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']
                
                missing_columns = [col for col in required_columns if col not in df.columns]
                
                if missing_columns:
                    st.error(f"Missing required columns: {', '.join(missing_columns)}")
                    st.info("Please ensure your CSV has all required columns.")
                else:
                    st.success(f"✅ Successfully loaded {len(df)} questions!")
                    
                    # Show preview
                    with st.expander("📋 Preview Questions"):
                        st.dataframe(df.head())
                    
                    # Settings panel
                    st.markdown('<div class="settings-panel">', unsafe_allow_html=True)
                    st.subheader("⚙️ Quiz Settings")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        pos_marks = st.number_input(
                            "Marks for correct answer",
                            min_value=1,
                            max_value=10,
                            value=4,
                            help="Points awarded for each correct answer"
                        )
                    
                    with col2:
                        neg_marks = st.number_input(
                            "Negative marks for wrong answer",
                            min_value=-5,
                            max_value=0,
                            value=-1,
                            help="Points deducted for each wrong answer"
                        )
                    
                    with col3:
                        time_limit = st.number_input(
                            "Time limit (minutes)",
                            min_value=5,
                            max_value=300,
                            value=60,
                            help="Total time allowed for the quiz"
                        )
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Quiz statistics
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total Questions", len(df))
                    with col2:
                        st.metric("Subjects", df['subject_name'].nunique())
                    with col3:
                        st.metric("Topics", df['topic_name'].nunique())
                    with col4:
                        max_score = len(df) * pos_marks
                        st.metric("Maximum Score", max_score)
                    
                    # Start quiz button
                    if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
                        st.session_state.quiz_data = df
                        st.session_state.quiz_settings = {
                            'pos_marks': pos_marks,
                            'neg_marks': neg_marks,
                            'time_limit': time_limit
                        }
                        st.session_state.quiz_started = True
                        st.session_state.start_time = datetime.now()
                        st.session_state.user_answers = {}
                        st.session_state.current_question = 0
                        st.rerun()
                        
            except Exception as e:
                st.error(f"Error reading CSV file: {str(e)}")
                st.info("Please check your CSV format and try again.")
    
    elif page == "ℹ️ Instructions":
        st.header("ℹ️ How to Use This System")
        
        st.markdown("""
        ### 📋 CSV File Format
        Your CSV file should contain the following columns:
        
        | Column | Description | Example |
        |--------|-------------|---------|
        | exam_name | Name of the exam | "GATE Computer Science" |
        | subject_name | Subject name | "Data Structures" |
        | topic_name | Specific topic | "Trees" |
        | question | The question text | "What is the time complexity of..." |
        | option_a | First option | "O(n)" |
        | option_b | Second option | "O(log n)" |
        | option_c | Third option | "O(n²)" |
        | option_d | Fourth option | "O(1)" |
        | correct_option | Correct answer | "B" |
        | explanation | Optional explanation | "Binary search has..." |
        
        ### 🎯 Quiz Features
        - ⏱️ **Timer**: Real-time countdown with automatic submission
        - 📝 **Navigation**: Move between questions freely
        - 💾 **Auto-save**: Your answers are saved automatically
        - 📊 **Detailed Reports**: Subject-wise and topic-wise analysis
        
        ### 📈 Scoring System
        - ✅ **Positive Marking**: Configurable marks for correct answers
        - ❌ **Negative Marking**: Configurable deduction for wrong answers
        - ⭕ **No Penalty**: No marks deducted for unattempted questions
        
        ### 📥 Report Generation
        After completing the quiz, you'll get:
        - Overall performance summary
        - Subject-wise breakdown
        - Topic-wise analysis  
        - Question-by-question review
        - Downloadable HTML report
        """)
    
    elif page == "🎯 Quiz":
        if st.session_state.quiz_data is None:
            st.error("No quiz data found. Please upload a CSV file first.")
            return
        
        df = st.session_state.quiz_data
        settings = st.session_state.quiz_settings
        
        # Calculate remaining time
        elapsed_time = datetime.now() - st.session_state.start_time
        total_seconds = settings['time_limit'] * 60
        remaining_seconds = max(0, total_seconds - elapsed_time.total_seconds())
        
        # Auto-submit if time is up
        if remaining_seconds <= 0:
            st.session_state.quiz_finished = True
            st.rerun()
        
        # Timer display
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds % 60)
        
        st.markdown(f"""
        <div class="timer-display">
            ⏰ Time Remaining: {minutes:02d}:{seconds:02d}
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar
        progress = st.session_state.current_question / len(df)
        st.progress(progress)
        st.write(f"Question {st.session_state.current_question + 1} of {len(df)}")
        
        # Current question
        current_q = st.session_state.current_question
        question_data = df.iloc[current_q]
        
        st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
        
        # Question display
        st.markdown(f"""
        <div class="question-card">
            <h3>Question {current_q + 1}</h3>
            <p><strong>Subject:</strong> {question_data['subject_name']} | <strong>Topic:</strong> {question_data['topic_name']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**{question_data['question']}**")
        
        # Options
        options = {
            'A': question_data['option_a'],
            'B': question_data['option_b'],
            'C': question_data['option_c'],
            'D': question_data['option_d']
        }
        
        # Get current answer
        current_answer = st.session_state.user_answers.get(current_q)
        
        # Radio button for options
        selected_option = st.radio(
            "Choose your answer:",
            options=['A', 'B', 'C', 'D'],
            format_func=lambda x: f"{x}. {options[x]}",
            index=['A', 'B', 'C', 'D'].index(current_answer) if current_answer else None,
            key=f"question_{current_q}"
        )
        
        # Save answer
        if selected_option:
            st.session_state.user_answers[current_q] = selected_option
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Navigation buttons
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        
        with col1:
            if st.button("⬅️ Previous", disabled=(current_q == 0)):
                st.session_state.current_question -= 1
                st.rerun()
        
        with col2:
            if st.button("➡️ Next", disabled=(current_q == len(df) - 1)):
                st.session_state.current_question += 1
                st.rerun()
        
        with col3:
            # Question navigator
            if st.button("📋 Question Navigator"):
                st.session_state.show_navigator = not st.session_state.get('show_navigator', False)
        
        with col4:
            if st.button("✅ Submit Quiz", type="primary"):
                st.session_state.quiz_finished = True
                st.rerun()
        
        # Question navigator
        if st.session_state.get('show_navigator', False):
            st.subheader("📋 Question Navigator")
            
            # Create grid of question numbers
            cols = st.columns(10)
            for i in range(len(df)):
                col_idx = i % 10
                with cols[col_idx]:
                    # Determine button style based on answer status
                    if i in st.session_state.user_answers:
                        button_type = "secondary"
                        label = f"✅ {i+1}"
                    else:
                        button_type = "primary" if i == current_q else "secondary"
                        label = f"⭕ {i+1}" if i != current_q else f"👉 {i+1}"
                    
                    if st.button(label, key=f"nav_{i}", help=f"Go to question {i+1}"):
                        st.session_state.current_question = i
                        st.rerun()
        
        # Quiz status
        answered = len(st.session_state.user_answers)
        st.info(f"📊 Progress: {answered}/{len(df)} questions answered")
        
        # Auto-refresh for timer (every 30 seconds)
        if remaining_seconds > 0:
            time.sleep(1)
            st.rerun()
    
    elif page == "📊 Results":
        if not st.session_state.quiz_finished:
            st.error("Quiz not completed yet!")
            return
        
        df = st.session_state.quiz_data
        settings = st.session_state.quiz_settings
        
        # Calculate results
        results = calculate_performance(
            df, 
            st.session_state.user_answers, 
            settings['pos_marks'], 
            settings['neg_marks']
        )
        
        # Calculate time taken
        if st.session_state.start_time:
            time_taken_delta = datetime.now() - st.session_state.start_time
            time_taken_str = str(time_taken_delta).split('.')[0]  # Remove microseconds
        else:
            time_taken_str = "Unknown"
        
        # Display results
        st.header("📊 Quiz Results")
        
        # Score summary
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Score", f"{results['total_marks']}/{results['max_marks']}")
        with col2:
            st.metric("Percentage", f"{results['percentage']}%")
        with col3:
            st.metric("Correct Answers", results['correct'])
        with col4:
            st.metric("Time Taken", time_taken_str)
        
        # Performance breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📚 Subject-wise Performance")
            subject_data = []
            for subject, perf in results['subject_performance'].items():
                accuracy = round((perf['correct'] / perf['total']) * 100, 2) if perf['total'] > 0 else 0
                subject_data.append({
                    'Subject': subject,
                    'Score': f"{perf['marks']}/{perf['total'] * settings['pos_marks']}",
                    'Accuracy': f"{accuracy}%"
                })
            st.dataframe(pd.DataFrame(subject_data), use_container_width=True)
        
        with col2:
            st.subheader("📖 Topic-wise Performance")
            topic_data = []
            for topic, perf in results['topic_performance'].items():
                accuracy = round((perf['correct'] / perf['total']) * 100, 2) if perf['total'] > 0 else 0
                topic_data.append({
                    'Topic': topic,
                    'Score': f"{perf['marks']}/{perf['total'] * settings['pos_marks']}",
                    'Accuracy': f"{accuracy}%"
                })
            st.dataframe(pd.DataFrame(topic_data), use_container_width=True)
        
        # Detailed question review
        st.subheader("📝 Question-by-Question Review")
        
        for idx in range(len(df)):
            question = df.iloc[idx]
            user_answer = st.session_state.user_answers.get(idx)
            correct_answer = question['correct_option']
            
            with st.expander(f"Question {idx + 1} - {question['subject_name']} ({question['topic_name']})"):
                st.write(f"**Question:** {question['question']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Options:**")
                    for opt in ['A', 'B', 'C', 'D']:
                        option_text = question[f'option_{opt.lower()}']
                        if opt == correct_answer:
                            st.success(f"✅ {opt}. {option_text} (Correct)")
                        elif opt == user_answer:
                            st.error(f"❌ {opt}. {option_text} (Your Answer)")
                        else:
                            st.write(f"○ {opt}. {option_text}")
                
                with col2:
                    if user_answer is None:
                        st.warning("⭕ Not Attempted")
                    elif user_answer == correct_answer:
                        st.success("✅ Correct!")
                    else:
                        st.error("❌ Incorrect")
                    
                    if 'explanation' in question and pd.notna(question['explanation']):
                        st.info(f"**Explanation:** {question['explanation']}")
        
        # Generate and offer report download
        st.subheader("📥 Download Report")
        
        if st.button("🔄 Generate Report", type="primary"):
            with st.spinner("Generating detailed report..."):
                html_report = generate_report_html(
                    df, 
                    st.session_state.user_answers, 
                    settings, 
                    results, 
                    time_taken_str
                )
                
                # Offer download
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"quiz_report_{timestamp}.html"
                
                st.download_button(
                    label="📥 Download HTML Report",
                    data=html_report,
                    file_name=filename,
                    mime="text/html",
                    use_container_width=True
                )
                
                st.success("✅ Report generated successfully! Click the button above to download.")
        
        # Reset quiz option
        if st.button("🔄 Take Another Quiz", type="secondary"):
            # Reset all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()