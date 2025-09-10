# Perplexity Research Prompt for Exam Question Generation

## Universal Prompt Template

```
Generate previous year questions for [EXAM_NAME] examination. 

**Exam Details:**
- Exam: [EXAM_NAME]
- Subject: [SUBJECT_NAME] (if specified, otherwise "All Subjects")
- Topic: [TOPIC_NAME] (if specified, otherwise "All Topics")
- Number of Questions: [NUM_QUESTIONS]
- Time Allowed: [TIME_MINUTES] minutes

**Search Requirements:**
1. Search for official previous year question papers from the last 5-10 years
2. Look for question banks, practice papers, and mock tests
3. Find questions from reputable educational sources and coaching institutes
4. Ensure questions are authentic and match the exam pattern

**Output Format:**
Please create a CSV file with the following columns:
- exam_name: Name of the examination
- subject_name: Subject name
- topic_name: Specific topic/chapter name
- question: The complete question text
- option_a: First option
- option_b: Second option
- option_c: Third option
- option_d: Fourth option
- correct_option: The correct answer (A, B, C, or D)
- year: Year when this question appeared (if known)
- difficulty: Easy/Medium/Hard
- explanation: Brief explanation of the correct answer

**Question Distribution Logic:**
- If only EXAM is specified: Generate full-length paper covering all major subjects
- If EXAM + SUBJECT specified: Focus on that subject's previous year questions
- If EXAM + SUBJECT + TOPIC specified: Focus on specific topic questions

Ensure all questions are multiple choice with exactly 4 options each.
```

## Example Usage Scenarios:

### Scenario 1: Full Length Paper
```
Generate previous year questions for GATE examination. 

**Exam Details:**
- Exam: GATE Computer Science
- Subject: All Subjects
- Topic: All Topics
- Number of Questions: 65
- Time Allowed: 180 minutes
```

### Scenario 2: Subject-Specific PYQs
```
Generate previous year questions for JEE Main examination. 

**Exam Details:**
- Exam: JEE Main
- Subject: Mathematics
- Topic: All Topics
- Number of Questions: 30
- Time Allowed: 90 minutes
```

### Scenario 3: Topic-Specific PYQs
```
Generate previous year questions for UPSC Civil Services examination. 

**Exam Details:**
- Exam: UPSC CSE Prelims
- Subject: History
- Topic: Ancient Indian History
- Number of Questions: 20
- Time Allowed: 30 minutes
```

## Variables to Replace:
- `[EXAM_NAME]`: Name of the examination (e.g., "GATE", "JEE Main", "NEET", "UPSC CSE")
- `[SUBJECT_NAME]`: Subject name (e.g., "Mathematics", "Physics", "Computer Science")
- `[TOPIC_NAME]`: Specific topic (e.g., "Calculus", "Thermodynamics", "Data Structures")
- `[NUM_QUESTIONS]`: Number of questions needed (e.g., 50, 100, 200)
- `[TIME_MINUTES]`: Time limit in minutes (e.g., 60, 120, 180)