import pandas as pd
import os
import time
import random
import numpy as np
from typing import List, Optional
from dataclasses import dataclass
import streamlit as st

# =========================================================
# Configuration and Constants
# =========================================================
CSV_FILE_PATH = "./data/permanent/question_bank.csv"
CSV_HEADERS = [
    "exam_name", "subject_name", "topic_name", "question", 
    "option_a", "option_b", "option_c", "option_d", 
    "correct_option", "year", "difficulty", "explanation"
]

# =========================================================
# Data Classes
# =========================================================
@dataclass
class QuestionBank:
    """
    Data class representing a question in the question bank.
    
    Attributes:
        exam_name (str): Name of the exam
        subject_name (str): Subject category
        topic_name (str): Specific topic within the subject
        question (str): The actual question text
        option_a (str): First option
        option_b (str): Second option
        option_c (str): Third option
        option_d (str): Fourth option
        correct_option (str): The correct answer (A, B, C, or D)
        year (str): Year of the question
        difficulty (str): Difficulty level (Easy, Medium, Hard)
        explanation (str): Explanation of the answer
    """
    exam_name: str
    subject_name: str
    topic_name: str
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str
    year: str
    difficulty: str
    explanation: str

# =========================================================
# Utility Functions
# =========================================================
def ensure_csv_exists() -> None:
    """
    Ensures the CSV file exists. If not, creates it with headers and dummy data.
    """
    if not os.path.exists(CSV_FILE_PATH):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(CSV_FILE_PATH), exist_ok=True)
        
        # Create CSV with dummy data
        dummy_data = generate_dummy_data()
        df = pd.DataFrame([vars(question) for question in dummy_data])
        df.to_csv(CSV_FILE_PATH, index=False)
        st.success("Created new question bank with sample data!")

def generate_dummy_data() -> List[QuestionBank]:
    """
    Generates dummy data for initial testing and demonstration.
    
    Returns:
        List[QuestionBank]: List of sample questions
    """
    return [
        QuestionBank("JEE Main", "Mathematics", "Algebra", "What is 2+2?", "3", "4", "5", "6", "B", "2020", "Easy", "Basic addition"),
        QuestionBank("JEE Main", "Mathematics", "Geometry", "What is the sum of angles in a triangle?", "180 degrees", "90 degrees", "360 degrees", "270 degrees", "A", "2020", "Easy", "Triangle angle sum property"),
        QuestionBank("NEET", "Physics", "Mechanics", "What is the speed of light?", "3×10^8 m/s", "3×10^6 m/s", "3×10^5 m/s", "3×10^7 m/s", "A", "2021", "Medium", "Fundamental constant"),
        QuestionBank("NEET", "Chemistry", "General", "What is H2O?", "Oxygen", "Hydrogen", "Water", "Carbon Dioxide", "C", "2021", "Easy", "Chemical formula for water"),
        QuestionBank("JEE Main", "Mathematics", "Algebra", "Solve for x: 2x + 3 = 7", "1", "2", "3", "4", "B", "2020", "Medium", "Basic algebraic manipulation"),
        QuestionBank("NEET", "Physics", "Mechanics", "What is Newton's Second Law?", "F=ma", "E=mc²", "V=IR", "P=IV", "A", "2021", "Hard", "Fundamental law of motion"),
        QuestionBank("JEE Main", "Mathematics", "Geometry", "What is the area of a circle?", "πr²", "2πr", "πd", "r²", "A", "2020", "Medium", "Area formula for circle"),
        QuestionBank("NEET", "Chemistry", "Acids and Bases", "What is the pH of pure water?", "7", "0", "14", "1", "A", "2021", "Easy", "Neutral pH value"),
        QuestionBank("JEE Main", "Mathematics", "Algebra", "What is the quadratic formula?", "x=(-b±√(b²-4ac))/2a", "x=(-b±√(b²+4ac))/2a", "x=(b±√(b²-4ac))/2a", "x=(-b±√(b²-4ac))/a", "A", "2020", "Hard", "Used to solve quadratic equations"),
        QuestionBank("NEET", "Physics", "Units and Measurements", "What is the unit of force?", "Newton", "Joule", "Watt", "Pascal", "A", "2021", "Easy", "SI unit of force"),
    ]

def load_data() -> pd.DataFrame:
    """
    Loads data from the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing all questions
        
    Raises:
        Exception: If there's an error reading the CSV file
    """
    try:
        ensure_csv_exists()
        df = pd.read_csv(CSV_FILE_PATH)
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()

def get_unique_values(df: pd.DataFrame, column: str) -> List[str]:
    """
    Gets unique values from a specific column, sorted alphabetically.
    
    Args:
        df (pd.DataFrame): The dataframe to extract values from
        column (str): Column name to get unique values from
        
    Returns:
        List[str]: Sorted list of unique values
    """
    if df.empty:
        return []
    return sorted(df[column].dropna().unique().tolist())

def filter_and_sample_dataframe(df: pd.DataFrame, exam_filter: List[str], 
                               subject_filter: List[str], topic_filter: List[str], 
                               num_questions: int = None, random_order: bool = True) -> pd.DataFrame:
    """
    Filters and samples the dataframe based on selected criteria with random sampling.
    
    Args:
        df (pd.DataFrame): Original dataframe
        exam_filter (List[str]): Selected exam names
        subject_filter (List[str]): Selected subject names  
        topic_filter (List[str]): Selected topic names
        num_questions (int): Number of questions to sample (None for all)
        random_order (bool): Whether to randomize the order
        
    Returns:
        pd.DataFrame: Filtered and sampled dataframe
    """
    filtered_df = df.copy()
    
    # Apply filters
    if exam_filter:
        filtered_df = filtered_df[filtered_df["exam_name"].isin(exam_filter)]
    if subject_filter:
        filtered_df = filtered_df[filtered_df["subject_name"].isin(subject_filter)]
    if topic_filter:
        filtered_df = filtered_df[filtered_df["topic_name"].isin(topic_filter)]
    
    # If no questions found after filtering
    if filtered_df.empty:
        return filtered_df
    
    # Handle sampling and random ordering
    if num_questions is not None and num_questions > 0:
        available_questions = len(filtered_df)
        
        if num_questions <= available_questions:
            # Sample without replacement
            sampled_df = filtered_df.sample(n=num_questions, random_state=random.randint(1, 10000))
        else:
            # Sample with replacement (repeat questions)
            # First, get all available questions
            base_sample = filtered_df.copy()
            remaining_needed = num_questions - available_questions
            
            # Randomly sample additional questions with replacement
            additional_sample = filtered_df.sample(n=remaining_needed, replace=True, 
                                                 random_state=random.randint(1, 10000))
            
            # Combine base and additional samples
            sampled_df = pd.concat([base_sample, additional_sample], ignore_index=True)
            
        # Randomize the final order
        if random_order:
            sampled_df = sampled_df.sample(frac=1, random_state=random.randint(1, 10000)).reset_index(drop=True)
            
        return sampled_df
    
    else:
        # Return all questions, optionally randomized
        if random_order:
            filtered_df = filtered_df.sample(frac=1, random_state=random.randint(1, 10000)).reset_index(drop=True)
        return filtered_df

def generate_csv_download(df: pd.DataFrame, filename_prefix: str = "questions") -> None:
    """
    Generates a CSV download button for the questions.
    
    Args:
        df (pd.DataFrame): DataFrame containing questions
        filename_prefix (str): Prefix for the filename
    """
    if df.empty:
        return
    
    # Create CSV string
    csv_string = df.to_csv(index=False)
    
    # Generate filename with timestamp
    timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.csv"
    
    # Create download button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            label="📥 Download Questions as CSV",
            data=csv_string,
            file_name=filename,
            mime="text/csv",
            type="secondary",
            use_container_width=True,
            help="Download the generated questions as a CSV file"
        )
    """
    Saves a new question to the CSV file.
    
    Args:
        question_data (QuestionBank): Question object to save
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        # Validate required fields
        if not all([question_data.exam_name, question_data.subject_name, 
                   question_data.topic_name, question_data.question]):
            st.error("Please fill in all required fields (Exam, Subject, Topic, Question)")
            return False
            
        # Validate correct option
        if question_data.correct_option.upper() not in ['A', 'B', 'C', 'D']:
            st.error("Correct option must be A, B, C, or D")
            return False
        
        # Convert to dataframe and append to CSV
        df = pd.DataFrame([vars(question_data)])
        df.to_csv(CSV_FILE_PATH, mode='a', header=False, index=False)
        return True
        
    except Exception as e:
        st.error(f"Error saving question: {str(e)}")
        return False

def display_questions_table(df: pd.DataFrame, num_requested: int = None) -> None:
    """
    Displays questions in a formatted table with better readability and full width.
    
    Args:
        df (pd.DataFrame): DataFrame containing questions to display
        num_requested (int): Number of questions that were requested
    """
    if df.empty:
        st.info("📭 No questions found matching the selected criteria.")
        return
    
    # Create a more readable display format
    display_df = df.copy()
    
    # Add question numbers for better identification
    display_df.insert(0, 'Q.No', range(1, len(display_df) + 1))
    
    # Rename columns for better display
    column_mapping = {
        'Q.No': '#',
        'exam_name': '🎓 Exam',
        'subject_name': '📚 Subject', 
        'topic_name': '🎯 Topic',
        'question': '❓ Question',
        'option_a': '🅰️ Option A',
        'option_b': '🅱️ Option B', 
        'option_c': '🅾️ Option C',
        'option_d': '🆔 Option D',
        'correct_option': '✅ Answer',
        'year': '📅 Year',
        'difficulty': '⚡ Difficulty',
        'explanation': '💡 Explanation'
    }
    
    display_df = display_df.rename(columns=column_mapping)
    
    # Display summary info with enhanced metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("📊 Generated", len(display_df))
    with col2:
        if num_requested and num_requested > len(df):
            unique_questions = len(df)
            repeated_questions = len(display_df) - unique_questions
            st.metric("🔄 Repeated", repeated_questions)
        else:
            difficulty_dist = display_df['⚡ Difficulty'].value_counts()
            most_common_difficulty = difficulty_dist.index[0] if len(difficulty_dist) > 0 else "N/A"
            st.metric("🎯 Most Common", most_common_difficulty)
    with col3:
        unique_subjects = display_df['📚 Subject'].nunique()
        st.metric("📚 Subjects", unique_subjects)
    with col4:
        unique_topics = display_df['🎯 Topic'].nunique()
        st.metric("🎯 Topics", unique_topics)
    with col5:
        if num_requested:
            st.metric("🎯 Requested", num_requested)
        else:
            unique_exams = display_df['🎓 Exam'].nunique()
            st.metric("🎓 Exams", unique_exams)
    
    # Show sampling info if applicable
    if num_requested and len(display_df) > 0:
        original_count = len(df.drop_duplicates()) if not df.empty else 0
        if len(display_df) > original_count:
            st.info(f"ℹ️ **Sampling Info**: Generated {len(display_df)} questions from {original_count} unique questions. Some questions were repeated to meet your requirement.")
        elif len(display_df) < num_requested:
            st.warning(f"⚠️ **Note**: Only {len(display_df)} questions available matching your criteria (requested {num_requested}).")
    
    st.markdown("---")
    
    # Display the table with full width and enhanced styling
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        height=600,  # Fixed height with scrolling
        column_config={
            "#": st.column_config.NumberColumn(
                "#",
                width="small",
                help="Question number"
            ),
            "❓ Question": st.column_config.TextColumn(
                "❓ Question",
                width="large",
                help="The question text"
            ),
            "🅰️ Option A": st.column_config.TextColumn(
                "🅰️ Option A",
                width="medium"
            ),
            "🅱️ Option B": st.column_config.TextColumn(
                "🅱️ Option B", 
                width="medium"
            ),
            "🅾️ Option C": st.column_config.TextColumn(
                "🅾️ Option C",
                width="medium"
            ),
            "🆔 Option D": st.column_config.TextColumn(
                "🆔 Option D",
                width="medium"
            ),
            "✅ Answer": st.column_config.TextColumn(
                "✅ Answer",
                width="small"
            ),
            "⚡ Difficulty": st.column_config.SelectboxColumn(
                "⚡ Difficulty",
                options=["Easy", "Medium", "Hard"],
                width="small"
            ),
            "💡 Explanation": st.column_config.TextColumn(
                "💡 Explanation",
                width="large",
                help="Detailed explanation of the answer"
            )
        }
    )

# =========================================================
# Streamlit UI Components
# =========================================================
def create_multiselect_with_all_option(label: str, options: List[str], key: str) -> List[str]:
    """
    Creates a multiselect widget with an "All" option.
    
    Args:
        label (str): Label for the multiselect
        options (List[str]): List of available options
        key (str): Unique key for the widget
        
    Returns:
        List[str]: Selected options
    """
    if not options:
        st.warning(f"No {label.lower()} options available")
        return []
    
    # Add "All" option at the beginning
    options_with_all = ["All"] + options
    
    selected = st.multiselect(
        label,
        options=options_with_all,
        key=key,
        help=f"Select specific {label.lower()} or choose 'All' to include everything"
    )
    
    # If "All" is selected, return all actual options (excluding "All")
    if "All" in selected:
        return options
    
    return selected

# =========================================================
# Main Application
# =========================================================
def main():
    """
    Main function that runs the Streamlit application.
    """
    # Configure page
    st.set_page_config(
        page_title="Question Bank Generator",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for both light and dark theme compatibility
    st.markdown("""
    <style>
    /* Root variables for theme adaptation */
    :root {
        --bg-primary: #0e1117;
        --bg-secondary: #1e2130;
        --bg-tertiary: #262730;
        --text-primary: #ffffff;
        --text-secondary: #c4c4c4;
        --border-color: #3d3d3d;
        --accent-blue: linear-gradient(45deg, #4dabf7 0%, #339af0 100%);
        --accent-teal: linear-gradient(45deg, #38d9a9 0%, #20c997 100%);
        --accent-pink: linear-gradient(45deg, #ff8cc8 0%, #ff6b9d 100%);
        --accent-purple: linear-gradient(45deg, #9775fa 0%, #845ef7 100%);
    }
    
    /* Light theme overrides */
    @media (prefers-color-scheme: light) {
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --bg-tertiary: #f1f3f4;
            --text-primary: #262626;
            --text-secondary: #525252;
            --border-color: #e6e9ef;
        }
    }
    
    .main > div {
        padding: 2rem 1rem;
    }
    
    /* Enhanced tabs for dark theme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0 20px;
        background: var(--bg-secondary);
        border-radius: 15px 15px 0 0;
        border: 2px solid var(--border-color);
        font-weight: bold;
        color: var(--text-secondary);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--bg-tertiary);
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--accent-purple);
        border-bottom: 2px solid transparent;
        color: white !important;
        box-shadow: 0 4px 15px rgba(151, 117, 250, 0.3);
    }
    
    /* Enhanced metrics for dark theme */
    .stMetric {
        background: var(--bg-secondary);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease;
    }
    
    .stMetric:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stMetric [data-testid="metric-container"] {
        background: transparent;
    }
    
    /* Enhanced buttons for dark theme */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        background: var(--accent-purple);
        color: white !important;
        font-weight: bold;
        height: 3.5em;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(151, 117, 250, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(151, 117, 250, 0.4);
        background: linear-gradient(45deg, #a78bfa 0%, #9333ea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Form elements styling for dark theme */
    .stMultiSelect > label,
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label {
        font-weight: bold;
        color: var(--text-primary) !important;
        font-size: 1rem;
    }
    
    .stMultiSelect > div > div,
    .stTextInput > div > div,
    .stTextArea > div > div,
    .stSelectbox > div > div {
        background-color: var(--bg-secondary) !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 10px !important;
    }
    
    /* Enhanced header styling for dark theme */
    .main-header {
        text-align: center;
        padding: 3rem 2rem;
        background: var(--accent-purple);
        color: white;
        margin: -2rem -1rem 2rem -1rem;
        border-radius: 0 0 25px 25px;
        box-shadow: 0 8px 32px rgba(151, 117, 250, 0.3);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 3.2rem;
        font-weight: 800;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    
    .main-header p {
        margin: 1rem 0 0 0;
        font-size: 1.3rem;
        opacity: 0.95;
        font-weight: 300;
    }
    
    /* Section headers for dark theme */
    .section-header {
        text-align: center;
        padding: 2.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .section-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .section-header p {
        margin: 0.8rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 300;
    }
    
    .generate-header { background: var(--accent-blue); }
    .save-header { background: var(--accent-teal); }
    .stats-header { background: var(--accent-pink); }
    
    /* Form sections for dark theme */
    .form-section {
        background: var(--bg-secondary);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Dataframe styling for dark theme */
    .stDataFrame {
        background: var(--bg-secondary);
        border-radius: 15px;
        border: 1px solid var(--border-color);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    /* Info boxes for dark theme */
    .stInfo {
        background: var(--bg-secondary);
        border: 1px solid var(--accent-blue);
        border-radius: 10px;
    }
    
    .stSuccess {
        background: var(--bg-secondary);
        border: 1px solid var(--accent-teal);
        border-radius: 10px;
    }
    
    .stWarning {
        background: var(--bg-secondary);
        border: 1px solid #ffa502;
        border-radius: 10px;
    }
    
    .stError {
        background: var(--bg-secondary);
        border: 1px solid #ff3838;
        border-radius: 10px;
    }
    
    /* Enhanced expander for dark theme */
    .streamlit-expander {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 10px;
    }
    
    /* Custom scrollbar for dark theme */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--border-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #606060;
    }
    
    /* Sidebar styling for dark theme */
    .css-1d391kg {
        background: var(--bg-secondary);
    }
    
    /* Chart styling adjustments */
    .stChart {
        background: var(--bg-secondary);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid var(--border-color);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Enhanced header with dark theme compatibility
    st.markdown("""
    <div class="main-header">
        <h1>🌙 Question Bank Generator</h1>
        <p>Create, Manage & Generate Questions with Dark Theme Elegance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    
    if df.empty:
        st.error("No data available. Please check your CSV file.")
        return
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["🔍 Generate Questions", "💾 Save Questions", "📊 Database Stats"])
    
    # ========== TAB 1: Generate Questions ==========
    with tab1:
        # Enhanced header with dark theme compatibility
        st.markdown("""
        <div class="section-header generate-header">
            <h1>🔍 Generate Questions</h1>
            <p>Filter and find the perfect questions for your needs</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Filter section with enhanced styling
        st.markdown("### 🎯 Filter Questions by Category")
        
        # Create filter columns with enhanced spacing
        col1, col2, col3 = st.columns([1, 1, 1], gap="large")
        
        with col1:
            st.markdown("##### 🎓 Exam Selection")
            exam_options = get_unique_values(df, "exam_name")
            selected_exams = create_multiselect_with_all_option(
                "Select Exam(s)", exam_options, "exam_select"
            )
        
        with col2:
            st.markdown("##### 📚 Subject Selection")
            subject_options = get_unique_values(df, "subject_name")
            selected_subjects = create_multiselect_with_all_option(
                "Select Subject(s)", subject_options, "subject_select"
            )
        
        with col3:
            st.markdown("##### 🎯 Topic Selection")
            topic_options = get_unique_values(df, "topic_name")
            selected_topics = create_multiselect_with_all_option(
                "Select Topic(s)", topic_options, "topic_select"
            )
        
        # Enhanced sampling options
        st.markdown("### 🎲 Sampling Options")
        col1, col2, col3 = st.columns([1, 1, 1], gap="large")
        
        with col1:
            st.markdown("##### 🔢 Number of Questions")
            # First check how many questions are available with current filters
            preview_df = filter_and_sample_dataframe(df, selected_exams, selected_subjects, selected_topics, num_questions=None, random_order=False)
            available_count = len(preview_df)
            
            use_limit = st.checkbox("📝 Limit number of questions", help="Check to specify exact number of questions")
            if use_limit:
                num_questions = st.number_input(
                    "Number of questions",
                    min_value=1,
                    max_value=10000,
                    value=min(10, max(1, available_count)),
                    help=f"Available questions with current filters: {available_count}. If you request more, questions will be repeated."
                )
                if num_questions > available_count and available_count > 0:
                    st.info(f"ℹ️ Will repeat {num_questions - available_count} questions from {available_count} available")
            else:
                num_questions = None
        
        with col2:
            st.markdown("##### 🎲 Random Ordering")
            random_order = st.checkbox("🔀 Randomize question order", value=True, 
                                     help="Shuffle questions in random order each time")
        
        with col3:
            st.markdown("##### 📋 Available Questions")
            st.metric("Available", available_count, help="Questions matching current filters")
        
        # Enhanced generate button section
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Generate Questions", type="primary", use_container_width=True):
                with st.spinner("🔄 Generating questions..."):
                    # Generate questions with new sampling functionality
                    sampled_df = filter_and_sample_dataframe(
                        df, selected_exams, selected_subjects, selected_topics,
                        num_questions=num_questions, random_order=random_order
                    )
                    
                    st.markdown("---")
                    display_questions_table(sampled_df, num_questions)
                    
                    # Add download button if questions were generated
                    if not sampled_df.empty:
                        st.markdown("### 📥 Export Questions")
                        generate_csv_download(sampled_df, "generated_questions")
    
    # ========== TAB 2: Save Questions ==========
    with tab2:
        # Enhanced header for save questions tab with dark theme
        st.markdown("""
        <div class="section-header save-header">
            <h1>💾 Save Questions</h1>
            <p>Add new questions to your database</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create form with enhanced styling
        with st.form("question_form", clear_on_submit=True):
            # Basic Information with enhanced styling
            st.markdown("### 📋 Basic Information")
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3, gap="large")
            
            with col1:
                exam_name = st.text_input("🎓 Exam Name *", placeholder="e.g., JEE Main, NEET")
            with col2:
                subject_name = st.text_input("📚 Subject Name *", placeholder="e.g., Mathematics, Physics")
            with col3:
                topic_name = st.text_input("🎯 Topic Name *", placeholder="e.g., Algebra, Mechanics")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Question Details with enhanced styling
            st.markdown("### ❓ Question Details")
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            
            question = st.text_area("📝 Question *", placeholder="Enter your question here...", height=120)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Options with enhanced styling
            st.markdown("### 📝 Answer Options")
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2, gap="large")
            
            with col1:
                option_a = st.text_input("🅰️ Option A", placeholder="First option")
                option_c = st.text_input("🅾️ Option C", placeholder="Third option")
            
            with col2:
                option_b = st.text_input("🅱️ Option B", placeholder="Second option")
                option_d = st.text_input("🆔 Option D", placeholder="Fourth option")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Additional Information with enhanced styling
            st.markdown("### ℹ️ Additional Information")
            st.markdown("<div class='form-section'>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3, gap="large")
            
            with col1:
                correct_option = st.selectbox("✅ Correct Option *", ["", "A", "B", "C", "D"])
            with col2:
                year = st.text_input("📅 Year", placeholder="e.g., 2023")
            with col3:
                difficulty = st.selectbox("⚡ Difficulty Level", ["", "Easy", "Medium", "Hard"])
            
            explanation = st.text_area("💡 Explanation", placeholder="Explain why this answer is correct...", height=100)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Enhanced submit button with spacing
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                submitted = st.form_submit_button("💾 Save Question", type="primary", use_container_width=True)
            
            if submitted:
                # Create question object
                new_question = QuestionBank(
                    exam_name=exam_name.strip(),
                    subject_name=subject_name.strip(),
                    topic_name=topic_name.strip(),
                    question=question.strip(),
                    option_a=option_a.strip(),
                    option_b=option_b.strip(),
                    option_c=option_c.strip(),
                    option_d=option_d.strip(),
                    correct_option=correct_option,
                    year=year.strip(),
                    difficulty=difficulty,
                    explanation=explanation.strip()
                )
                
                # Save question
                if save_question(new_question):
                    st.success("✅ Question saved successfully!")
                    st.balloons()
                    time.sleep(2)
                    st.experimental_rerun()
    
    # ========== TAB 3: Database Stats ==========
    with tab3:
        # Enhanced header for stats tab
        st.markdown("""
        <div style="background: linear-gradient(45deg, #fd79a8, #e84393); color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem; text-align: center;">
            <h1 style="margin: 0; font-size: 2.5rem;">📊 Database Statistics</h1>
            <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">Analyze your question bank data</p>
        </div>
        """, unsafe_allow_html=True)
        
        if not df.empty:
            # Enhanced overview metrics with better styling
            st.markdown("### 📈 Overview Metrics")
            col1, col2, col3, col4 = st.columns(4, gap="large")
            
            with col1:
                st.metric(
                    label="📝 Total Questions", 
                    value=len(df),
                    help="Total number of questions in the database"
                )
            with col2:
                st.metric(
                    label="🎓 Total Exams", 
                    value=df["exam_name"].nunique(),
                    help="Number of different exams"
                )
            with col3:
                st.metric(
                    label="📚 Total Subjects", 
                    value=df["subject_name"].nunique(),
                    help="Number of different subjects"
                )
            with col4:
                st.metric(
                    label="🎯 Total Topics", 
                    value=df["topic_name"].nunique(),
                    help="Number of different topics"
                )
            
            st.markdown("---")
            
            # Enhanced distribution charts with better styling
            st.markdown("### 📊 Data Distribution")
            
            col1, col2 = st.columns(2, gap="large")
            
            with col1:
                st.markdown("#### 🎓 Questions by Exam")
                exam_counts = df["exam_name"].value_counts()
                st.bar_chart(exam_counts, height=400, use_container_width=True)
                
                # Show detailed breakdown
                with st.expander("📋 Detailed Breakdown"):
                    for exam, count in exam_counts.items():
                        percentage = (count / len(df)) * 100
                        st.write(f"**{exam}**: {count} questions ({percentage:.1f}%)")
            
            with col2:
                st.markdown("#### ⚡ Questions by Difficulty")
                difficulty_counts = df["difficulty"].value_counts()
                st.bar_chart(difficulty_counts, height=400, use_container_width=True)
                
                # Show detailed breakdown
                with st.expander("📋 Detailed Breakdown"):
                    for difficulty, count in difficulty_counts.items():
                        percentage = (count / len(df)) * 100
                        st.write(f"**{difficulty}**: {count} questions ({percentage:.1f}%)")
            
            st.markdown("---")
            
            # Subject distribution with full width
            st.markdown("### 📚 Questions by Subject")
            subject_counts = df["subject_name"].value_counts()
            st.bar_chart(subject_counts, height=300, use_container_width=True)
            
            # Recent additions (if year column has data)
            st.markdown("### 📅 Questions by Year")
            if df["year"].notna().any() and df["year"].str.strip().ne('').any():
                year_counts = df[df["year"].str.strip() != ""]["year"].value_counts().sort_index()
                st.line_chart(year_counts, height=300, use_container_width=True)
                
                # Show year breakdown
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### 📈 Recent Activity")
                    latest_years = year_counts.tail(3)
                    for year, count in latest_years.items():
                        st.write(f"**{year}**: {count} questions")
                        
                with col2:
                    st.markdown("#### 📊 Total by Period")
                    total_with_year = df["year"].notna().sum()
                    total_without_year = len(df) - total_with_year
                    st.write(f"**With Year Info**: {total_with_year}")
                    st.write(f"**Without Year Info**: {total_without_year}")
            else:
                st.info("📋 No year data available for questions.")
                
        else:
            st.warning("📭 No data available to display statistics.")

# =========================================================
# Application Entry Point
# =========================================================
if __name__ == "__main__":
    main()