# Perplexity Research Prompt for Interview Question Generation

## Universal Prompt Template

```
Generate interview questions for [TOPIC_NAME] in the following order: previous year questions, books, academic papers, online websites. Ensure each question ends with its source link in brackets [SOURCE_LINK].

**Interview Preparation Details:**

- Topic: [TOPIC_NAME]
- Number of Questions: [NUM_QUESTIONS]
- Format: All questions must be multiple choice (exactly 4 options). Convert any non-MCQ questions to MCQ.
- Coding questions (if any) must include unittest cases; present them as MCQ options.

**Search Requirements:**

1. Retrieve previous year interview questions.
2. Identify key books with sample questions.
3. Extract question-style prompts from academic papers.
4. Gather practice questions from reputable online sites.

**Output Format:**

Please create a CSV file with the following columns:
- topic_name
- question (append “[SOURCE_LINK]” at end)
- option_a
- option_b
- option_c
- option_d
- correct_option
- year (if known)
- difficulty (Easy/Medium/Hard)
- explanation
```

# Perplexity Research Prompt for Revision Question Generation

## Universal Prompt Template

```
Generate revision questions for [SUBJECT_NAME] from authentic sites to help revise or master the topic. Ensure each question ends with its source link in brackets [SOURCE_LINK].

**Revision Details:**

- Subject: [SUBJECT_NAME]
- Topic: [TOPIC_NAME] (optional)
- Number of Questions: [NUM_QUESTIONS]
- Format: All questions must be multiple choice (exactly 4 options). Convert any non-MCQ questions to MCQ.

**Search Requirements:**

1. Query reputable educational websites and official documentation.
2. Extract high-quality practice questions and answers.
3. Validate authenticity and coverage of key subtopics.

**Output Format:**

Please create a CSV file with the following columns:
- subject_name
- topic_name
- question (append “[SOURCE_LINK]” at end)
- option_a
- option_b
- option_c
- option_d
- correct_option
- difficulty (Easy/Medium/Hard)
- explanation
```

# Perplexity Research Prompt for Coding Skills Practice Question Generation

## Universal Prompt Template

```
Generate coding practice questions for [SKILL_NAME] (e.g., ML, AI, Data Science, Software Engineering, Database Engineering, Python Development). Provide comprehensive MCQs covering theory and practical code implementation, using initial data for processing. Ensure each question ends with its source link in brackets [SOURCE_LINK].

**Coding Practice Details:**

- Skill: [SKILL_NAME]
- Number of Questions: [NUM_QUESTIONS]
- Data Provided: [DATA_DESCRIPTION] (e.g., sample CSV, JSON)
- Format: All questions must be multiple choice (exactly 4 options). Convert any non-MCQ questions to MCQ.
- Include unittest cases for coding problems, and present possible outputs as MCQ options.

**Search Requirements:**

1. Source questions from authoritative coding platforms and documentation.
2. Include both theoretical and implementation-based prompts.
3. Ensure data-driven questions provide sample inputs.

**Output Format:**

Please create a CSV file with the following columns:
- skill_name
- question (append “[SOURCE_LINK]” at end)
- option_a
- option_b
- option_c
- option_d
- correct_option
- difficulty (Easy/Medium/Hard)
- explanation
- unittest_code (for coding questions)
```

# Perplexity Research Prompt for Previous Year Exam Question Generation

## Universal Prompt Template

```
Generate previous year questions for [EXAM_NAME] examination. Ensure each question ends with its source link in brackets [SOURCE_LINK].

**Exam Details:**

- Exam: [EXAM_NAME]
- Subject: [SUBJECT_NAME] (if specified, otherwise "All Subjects")
- Topic: [TOPIC_NAME] (if specified, otherwise "All Topics")
- Number of Questions: [NUM_QUESTIONS]
- Time Allowed: [TIME_MINUTES] minutes

**Search Requirements:**

1. Search for official previous year question papers from the last 5–10 years.
2. Look for question banks, practice papers, and mock tests.
3. Find questions from reputable educational sources and coaching institutes.
4. Ensure questions are authentic and match the exam pattern.

**Output Format:**

Please create a CSV file with the following columns:
- exam_name
- subject_name
- topic_name
- question (append “[SOURCE_LINK]” at end)
- option_a
- option_b
- option_c
- option_d
- correct_option
- year (if known)
- difficulty (Easy/Medium/Hard)
- explanation

**Question Distribution Logic:**

- If only EXAM is specified: Generate a full-length paper covering all major subjects.
- If EXAM + SUBJECT specified: Focus on that subject’s previous year questions.
- If EXAM + SUBJECT + TOPIC specified: Focus on specific topic questions.
```