import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(initial_sidebar_state="collapsed")

st.write("# Skills Chart")


def radarPlot(skills):
    df = pd.DataFrame(skills)
    st.dataframe(df, use_container_width=True)
    selection = st.pills(
    f"Skills",
    options=skills.keys(),
    selection_mode="multi"
    )
    st.write(f"You selected: {selection}")
    skill_selection = dict()
    for i in selection:
        skill_selection[i] = st.pills(
        i,
        options=skills[i],
        selection_mode="multi"
        )
        st.info(f"{i}: {", ".join(skill_selection[i])}")
    # Web Chart
    if selection and skill_selection:
        data = {
            "Category": selection,
            "Proficiency": [len(skill_selection[i])/len(skills[i]) * 100 for i in selection]  # Example proficiency calculation
        }
        df = pd.DataFrame(data)

        # Streamlit app
        st.title("Skills Proficiency Radar Chart")
        st.write("Visualize proficiency across skill categories.")

        # Create radar chart
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=df["Proficiency"].tolist() + [df["Proficiency"].iloc[0]],  # Close the loop
            theta=df["Category"].tolist() + [df["Category"].iloc[0]],  # Close the loop
            fill='toself',
            name='Proficiency',
            line=dict(color='#ff0000', width=2),
            fillcolor='rgba(31, 119, 180, 0.3)',
            hovertemplate='%{theta}: %{r}%'
        ))

        # Update layout for modern look
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickvals=[20, 40, 60, 80, 100],
                    ticktext=['20%', '40%', '60%', '80%', '100%'],
                    showline=True,
                    linewidth=1,
                    gridcolor='rgba(128, 128, 128, 0.2)'
                ),
                angularaxis=dict(
                    showline=True,
                    linewidth=1,
                    gridcolor='rgba(128, 128, 128, 0.2)',
                    rotation=90,
                    direction="clockwise"
                ),
                bgcolor='rgba(245, 245, 245, 0)'
            ),
            showlegend=True,
            title=dict(
                text="Skills Proficiency Overview",
                x=0.5,
                xanchor="center",
                font=dict(size=18, color="#333")
            ),
            template="plotly_white",
            height=500,
            margin=dict(l=40, r=40, t=80, b=40)
        )

        # Display chart
        st.plotly_chart(fig, use_container_width=True)

# Dictionary of fields and their corresponding resume-ready skills
tab_py, tab_oe, tab_AI, tab_cv, tab_dl, tab_llm, tab_AAI = st.tabs(["Python", "Optical Engineering", "AI", "Computer Vision", "Deep Learning", "LLM", "Agentic AI"])
with tab_py:
    skills= {
    "Core Programming": [
        "Python Software Development",
        "Object-Oriented Programming",
        "Functional Programming",
        "Multithreading and Concurrency",
        "Exception Handling",
        "Code Optimization",
        "Unit Testing with PyTest",
        "Data Structures and Algorithms",
        "Memory Management",
        "Regular Expressions",
        "File I/O Operations",
        "Python Standard Library"
    ],
    "Data Analysis and Visualization": [
        "Data Analysis with Pandas",
        "Data Visualization with Matplotlib",
        "NumPy Array Operations",
        "Seaborn Visualization",
        "Data Cleaning and Preprocessing",
        "Time Series Analysis",
        "Exploratory Data Analysis",
        "SciPy for Scientific Computing",
        "Jupyter Notebook Workflow",
        "Statistical Modeling",
        "Data Pipeline Development",
        "Plotly Interactive Visuals"
    ],
    "Web and Automation": [
        "Flask Web Development",
        "Django Application Development",
        "RESTful API Design",
        "Web Scraping with BeautifulSoup",
        "Selenium Web Automation",
        "FastAPI Implementation",
        "Script Automation",
        "API Automation with Requests",
        "Database Integration",
        "Asynchronous Programming",
        "GUI Automation with PyAutoGUI",
        "Task Scheduling with Celery"
    ],
    "Development Tools and Practices": [
        "Git Version Control",
        "Virtual Environment Management",
        "Code Linting with Flake8",
        "Continuous Integration Setup",
        "Package Development with Poetry",
        "Documentation with Sphinx",
        "Profiling and Optimization",
        "Dependency Management",
        "Docker Container Scripting",
        "IPython Debugging",
        "Code Review Practices",
        "Test-Driven Development"
    ]
}
    radarPlot(skills)

with tab_oe:
    skills = {
    "Core Optical Engineering": [
        "Optical System Design",
        "Lens System Optimization",
        "Laser System Design",
        "Photonics Engineering",
        "Fiber Optic Systems",
        "Optoelectronic Device Development",
        "Interferometric Measurement",
        "Spectroscopic Analysis",
        "Polarization Optics Management",
        "Holographic Imaging",
        "Optical Wavefront Analysis",
        "Beam Propagation Analysis"
    ],
    "Software and Simulation Tools": [
        "MATLAB Programming",
        "Python for Optical Simulations",
        "Zemax Optical Design",
        "Code V Analysis",
        "OpticStudio Ray Tracing",
        "COMSOL Multiphysics Modeling",
        "Lumerical Photonics Simulation",
        "RSoft Optoelectronic Design",
        "LabVIEW Control Systems",
        "AutoCAD Optical Drafting",
        "ANSYS Optical Simulation",
        "SolidWorks for Optical Components"
    ],
    "Experimental and Hardware": [
        "Precision Optical Alignment",
        "Optical Performance Testing",
        "Cleanroom Fabrication Techniques",
        "Thin Film Coating",
        "Microfabrication of Optical Devices",
        "Optical Metrology",
        "Laser Beam Profiling",
        "Photodetector Calibration",
        "Fiber Optic Splicing",
        "Cryogenic Optical Systems",
        "Optical Component Assembly",
        "High-Precision Interferometry"
    ],
    "Computational and Analytical": [
        "Optical Data Analysis",
        "Signal Processing for Optics",
        "Finite Element Analysis (FEA)",
        "Ray Tracing Simulation",
        "Wave Optics Modeling",
        "Numerical Optical Modeling",
        "Statistical Data Analysis",
        "Optical Image Processing",
        "Machine Learning for Optics",
        "Optical System Optimization",
        "Monte Carlo Simulation",
        "Aberration Analysis"
    ],
    "Materials and Fabrication": [
        "Optical Material Selection",
        "Anti-Reflective Coating Design",
        "Semiconductor Device Physics",
        "Nanoscale Optical Fabrication",
        "Additive Manufacturing for Optics",
        "Lens Grinding and Polishing",
        "Photolithographic Patterning",
        "Optical Etching Techniques",
        "Material Optical Characterization",
        "Thermal Effects Analysis",
        "Diffraction Grating Fabrication",
        "Optical Crystal Processing"
    ],
    "Interdisciplinary": [
        "Electronic Circuit Design",
        "Embedded Systems Programming",
        "Optical Control Systems",
        "Robotics Integration with Optics",
        "Quantum Optics Research",
        "Biomedical Optical Devices",
        "Solar Energy Optics",
        "Astronomical Optical Systems",
        "Acousto-Optic Modulation",
        "Environmental Optical Sensing",
        "Thermal Management in Optics",
        "Optical Communication Systems"
    ],
    "Emerging and Advanced": [
        "Metamaterial Design",
        "Plasmonic Device Development",
        "Adaptive Optics Implementation",
        "Nonlinear Optical Phenomena",
        "Ultrafast Laser Systems",
        "Integrated Photonics Design",
        "AR/VR Optical Engineering",
        "LiDAR System Development",
        "AI-Driven Optical Design",
        "Blockchain for Research Data",
        "Freeform Optics Design",
        "Quantum Photonics"
    ]
}
    radarPlot(skills)

with tab_AI:
    skills = {
        "Machine Learning Foundations": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Reinforcement Learning",
            "Feature Engineering",
            "Model Evaluation Metrics",
            "Cross-Validation Techniques",
            "Hyperparameter Tuning",
            "Ensemble Methods",
            "Scikit-Learn Implementation",
            "Dimensionality Reduction",
            "Anomaly Detection",
            "Time Series Forecasting"
        ],
        "AI Model Development": [
            "Neural Network Design",
            "Gradient Descent Optimization",
            "Loss Function Engineering",
            "TensorFlow Model Building",
            "PyTorch Implementation",
            "Model Interpretability",
            "Transfer Learning",
            "Federated Learning",
            "AutoML Integration",
            "Pipeline Automation",
            "Model Deployment",
            "Explainable AI"
        ],
        "Specialized AI Applications": [
            "Natural Language Processing",
            "Computer Vision Algorithms",
            "Speech Recognition Systems",
            "Recommendation Systems",
            "Generative Adversarial Networks",
            "Knowledge Graph Construction",
            "Sentiment Analysis",
            "AI Ethics Implementation",
            "Robotic Process Automation",
            "AI for Healthcare",
            "AI-Driven Optimization",
            "Real-Time Inference"
        ],
        "AI Infrastructure and Tools": [
            "MLOps Workflow",
            "Kubernetes Model Deployment",
            "AWS SageMaker Integration",
            "Model Monitoring",
            "Data Versioning",
            "JupyterLab for AI",
            "Hugging Face Transformers",
            "ONNX Model Conversion",
            "Ray for Distributed AI",
            "MLflow Experiment Tracking",
            "Cloud AI Services",
            "Edge AI Deployment"
        ]
    }
    radarPlot(skills)

with tab_cv:
    skills = {
        "Core Vision Techniques": [
            "Image Processing",
            "Object Detection",
            "Image Segmentation",
            "Feature Extraction",
            "Edge Detection",
            "Image Classification",
            "Optical Flow Analysis",
            "3D Reconstruction",
            "Image Registration",
            "Facial Recognition",
            "Motion Tracking",
            "Template Matching"
        ],
        "Advanced Vision Algorithms": [
            "Convolutional Neural Networks",
            "YOLO Implementation",
            "R-CNN Model Development",
            "Semantic Segmentation",
            "Instance Segmentation",
            "Pose Estimation",
            "Depth Estimation",
            "Visual SLAM",
            "Image Super-Resolution",
            "Video Frame Analysis",
            "Attention Mechanisms",
            "Generative Vision Models"
        ],
        "Tools and Frameworks": [
            "OpenCV Development",
            "TensorFlow for Vision",
            "PyTorch Vision Models",
            "Keras Image Processing",
            "MATLAB Vision Toolbox",
            "Pillow Image Manipulation",
            "Dlib for Facial Analysis",
            "Albumentations Augmentation",
            "CUDA GPU Acceleration",
            "ONNX Model Optimization",
            "LabelImg Annotation",
            "VGG Image Annotator"
        ],
        "Applications and Deployment": [
            "Autonomous Vehicle Vision",
            "Medical Image Analysis",
            "Augmented Reality Systems",
            "Surveillance Systems",
            "Industrial Inspection",
            "Biometric Authentication",
            "Real-Time Video Processing",
            "Drone Navigation Vision",
            "Retail Analytics",
            "Vision-Based Robotics",
            "Edge Device Deployment",
            "Cloud Vision APIs"
        ]
    }
    radarPlot(skills)

with tab_dl:
    skills = {
        "Neural Network Fundamentals": [
            "Neural Network Architecture",
            "Backpropagation Implementation",
            "Activation Functions",
            "Loss Function Design",
            "Gradient Descent Optimization",
            "Batch Normalization",
            "Dropout Regularization",
            "Weight Initialization",
            "Stochastic Gradient Descent",
            "Learning Rate Scheduling",
            "Overfitting Mitigation",
            "Network Pruning"
        ],
        "Advanced Architectures": [
            "Convolutional Neural Networks",
            "Recurrent Neural Networks",
            "Long Short-Term Memory (LSTM)",
            "Gated Recurrent Units (GRU)",
            "Transformer Models",
            "Generative Adversarial Networks",
            "Variational Autoencoders",
            "Attention Mechanisms",
            "Residual Networks (ResNet)",
            "Graph Neural Networks",
            "Capsule Networks",
            "Self-Supervised Learning"
        ],
        "Frameworks and Optimization": [
            "TensorFlow Model Development",
            "PyTorch Deep Learning",
            "Keras Model Prototyping",
            "MXNet Implementation",
            "ONNX Model Conversion",
            "Model Quantization",
            "Distributed Training",
            "Mixed Precision Training",
            "Hyperparameter Optimization",
            "Neural Architecture Search",
            "Gradient Clipping",
            "AutoML for Deep Learning"
        ],
        "Deployment and Applications": [
            "Model Deployment to Production",
            "Edge Device Optimization",
            "Cloud Model Serving",
            "Real-Time Inference",
            "Computer Vision Applications",
            "Natural Language Processing",
            "Speech Synthesis Models",
            "Recommendation Systems",
            "Time Series Prediction",
            "Healthcare Diagnostics",
            "Robotics Control Systems",
            "Anomaly Detection Systems"
        ]
    }
    radarPlot(skills)

with tab_llm:
    skills = {
        "Core NLP Techniques": [
            "Natural Language Processing",
            "Text Preprocessing",
            "Tokenization Techniques",
            "Sentiment Analysis",
            "Named Entity Recognition",
            "Text Classification",
            "Word Embeddings",
            "Part-of-Speech Tagging",
            "Dependency Parsing",
            "Text Summarization",
            "Question Answering",
            "Topic Modeling"
        ],
        "LLM Architecture and Training": [
            "Transformer Architecture",
            "BERT Model Fine-Tuning",
            "GPT Model Development",
            "Attention Mechanism Design",
            "Pretraining Strategies",
            "Transfer Learning for NLP",
            "Prompt Engineering",
            "Parameter-Efficient Fine-Tuning",
            "Instruction Tuning",
            "Reinforcement Learning from Human Feedback",
            "Model Scaling",
            "Context Window Optimization"
        ],
        "Tools and Frameworks": [
            "Hugging Face Transformers",
            "PyTorch for NLP",
            "TensorFlow Text Processing",
            "SpaCy Pipeline Development",
            "NLTK Text Analysis",
            "Fairseq Model Training",
            "DeepSpeed Optimization",
            "Megatron-LM Scaling",
            "LangChain Integration",
            "AllenNLP Framework",
            "Sentence Transformers",
            "ONNX for NLP Models"
        ],
        "Applications and Deployment": [
            "Chatbot Development",
            "Text Generation Systems",
            "Machine Translation",
            "Conversational AI",
            "Content Moderation",
            "Knowledge Base Querying",
            "Automated Writing Assistance",
            "Legal Document Analysis",
            "Customer Support Automation",
            "Multimodal LLMs",
            "Cloud LLM Deployment",
            "Ethical AI Implementation"
        ]
    }
    radarPlot(skills)

with tab_AAI:
    skills = {
        "Agent Design and Behavior": [
            "Autonomous Agent Development",
            "Goal-Oriented Behavior Design",
            "Multi-Agent System Architecture",
            "Decision-Making Algorithms",
            "Environment Interaction Modeling",
            "Agent Communication Protocols",
            "Behavioral Adaptation",
            "Task Decomposition",
            "Planning and Execution",
            "Agent Simulation",
            "Cognitive Modeling",
            "State Space Representation"
        ],
        "Reinforcement Learning": [
            "Reinforcement Learning Design",
            "Q-Learning Implementation",
            "Deep Q-Networks (DQN)",
            "Policy Gradient Methods",
            "Actor-Critic Models",
            "Reward Function Engineering",
            "Exploration-Exploitation Strategies",
            "Multi-Agent Reinforcement Learning",
            "Inverse Reinforcement Learning",
            "Hierarchical RL",
            "Model-Based RL",
            "OpenAI Gym Integration"
        ],
        "Tools and Frameworks": [
            "PyTorch for Agent Training",
            "TensorFlow Agent Models",
            "RLlib for Scalable RL",
            "Stable-Baselines3 Implementation",
            "Gymnasium Environment Design",
            "Unity ML-Agents",
            "PettingZoo Multi-Agent Environments",
            "Ray for Distributed Agents",
            "MESA Agent-Based Modeling",
            "LangChain for Agentic Workflows",
            "JAX for Optimization",
            "MATLAB for Simulations"
        ],
        "Applications and Deployment": [
            "Robotic Task Automation",
            "Game AI Development",
            "Supply Chain Optimization",
            "Smart Grid Management",
            "Autonomous Vehicle Navigation",
            "Conversational Agent Systems",
            "Financial Trading Agents",
            "Healthcare Workflow Automation",
            "Industrial Process Control",
            "Edge Device Agent Deployment",
            "Ethical Agent Design",
            "Real-Time Decision Systems"
        ]
    }
    radarPlot(skills)