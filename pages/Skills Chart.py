import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def radarPlot(selection, skill_selection):
        # Sample dataset
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
tab_cs, tab_oe = st.tabs(
    ["Computer Science", "Optical Engineering"]
)
with tab_cs:
    skills = {
    "Computer Vision": [
        "Image Processing",
        "Object Detection",
        "Image Segmentation",
        "Facial Recognition",
        "Optical Character Recognition (OCR)",
        "Feature Extraction",
        "3D Reconstruction",
        "OpenCV",
        "YOLO",
        "Convolutional Neural Networks (CNNs)"
    ],
    "Deep Learning": [
        "Neural Network Architecture Design",
        "Convolutional Neural Networks (CNNs)",
        "Recurrent Neural Networks (RNNs)",
        "Long Short-Term Memory (LSTM) Networks",
        "Generative Adversarial Networks (GANs)",
        "Transfer Learning",
        "Hyperparameter Tuning",
        "TensorFlow",
        "PyTorch",
        "Model Optimization"
    ],
    "Large Language Models (LLMs)": [
        "Natural Language Processing (NLP)",
        "Text Generation",
        "Sentiment Analysis",
        "Named Entity Recognition (NER)",
        "Text Summarization",
        "Question Answering Systems",
        "Prompt Engineering",
        "Fine-Tuning LLMs",
        "Transformers",
        "Hugging Face"
    ],
    "Generative AI": [
        "Content Generation",
        "Image Synthesis",
        "Text-to-Image Generation",
        "Style Transfer",
        "Variational Autoencoders (VAEs)",
        "Generative Adversarial Networks (GANs)",
        "Music Generation",
        "Synthetic Data Creation",
        "Stable Diffusion",
        "DALL-E"
    ],
    "Agentic AI": [
        "Autonomous Decision Making",
        "Reinforcement Learning",
        "Multi-Agent Systems",
        "Task Automation",
        "Environment Interaction",
        "Policy Optimization",
        "Goal-Oriented AI Design",
        "OpenAI Gym",
        "Agent Simulation",
        "Behavioral Modeling"
    ],
    "Python": [
        "Python Programming",
        "Data Analysis with Pandas",
        "Data Visualization with Matplotlib",
        "Web Scraping",
        "API Development",
        "Script Automation",
        "NumPy",
        "SciPy",
        "Flask",
        "Django"
    ],
    "Web Development": [
        "Full-Stack Web Development",
        "Responsive Web Design",
        "RESTful API Development",
        "Web Application Security",
        "Performance Optimization",
        "Version Control with Git",
        "HTML5",
        "CSS3",
        "JavaScript",
        "Node.js"
    ],
    "Front End": [
        "User Interface (UI) Design",
        "React.js",
        "Vue.js",
        "Angular",
        "TypeScript",
        "CSS Frameworks (Bootstrap, Tailwind)",
        "Single Page Applications (SPAs)",
        "Web Accessibility (WCAG)",
        "Client-Side Rendering",
        "State Management"
    ],
    "Back End": [
        "Server-Side Development",
        "Database Integration",
        "API Design and Development",
        "Authentication and Authorization",
        "Microservices Architecture",
        "Express.js",
        "Django",
        "Spring Boot",
        "GraphQL",
        "Serverless Computing"
    ],
    "Databases": [
        "Database Design",
        "SQL Query Optimization",
        "NoSQL Databases",
        "Data Modeling",
        "Database Administration",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Redis",
        "Elasticsearch"
    ],
    "DevOps": [
        "Continuous Integration/Continuous Deployment (CI/CD)",
        "Infrastructure as Code (IaC)",
        "Cloud Deployment",
        "Monitoring and Logging",
        "Configuration Management",
        "Jenkins",
        "Ansible",
        "Terraform",
        "AWS",
        "Azure"
    ],
    "Docker": [
        "Containerization",
        "Docker Compose",
        "Container Orchestration",
        "Image Optimization",
        "Dockerfile Creation",
        "Microservices Deployment",
        "Container Security",
        "Docker Swarm",
        "Kubernetes Integration",
        "Container Networking"
    ],
    "Linux": [
        "Linux System Administration",
        "Bash Scripting",
        "Server Configuration",
        "File System Management",
        "Network Troubleshooting",
        "Cron Jobs",
        "SSH Management",
        "Ubuntu",
        "CentOS",
        "System Monitoring"
    ]
}
    df = pd.DataFrame(skills)
    st.dataframe(df, use_container_width=True)
    selection = st.pills(
    "Skills",
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
        st.write(f"Skills in {i}: {skill_selection[i]}")
    # Web Chart
    if selection and skill_selection:
        radarPlot(selection, skill_selection)
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
    df = pd.DataFrame(skills)
    st.dataframe(df, use_container_width=True)
    selection = st.pills(
    "Skills",
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
        st.write(f"Skills in {i}: {skill_selection[i]}")
    # Web Chart
    if selection and skill_selection:
        radarPlot(selection, skill_selection)