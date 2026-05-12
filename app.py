import streamlit as st

# Page Config
st.set_page_config(
    page_title="Hamza AI Portfolio",
    page_icon="🚀",
    layout="wide"
)

# HEADER
col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/profile.jpg", width=250)

with col2:
    st.title("🚀 Hamza AI Portfolio")
    
    st.subheader(
        "MS Data Science Student | AI & Computer Vision Enthusiast"
    )

    st.write(
        """
        Passionate about Artificial Intelligence,
        Computer Vision, and Deep Learning.
        """
    )

# METRICS
st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Projects", "5+")
col2.metric("Focus", "Computer Vision")
col3.metric("Research", "YOLOv8 + Drone Imagery")

st.divider()

# ABOUT
st.header("👨‍💻 About Me")

st.write(
    """
    I am an MS Data Science student with strong interest in:
    
    - Artificial Intelligence
    - Machine Learning
    - Deep Learning
    - Computer Vision
    - Object Detection
    
    I build practical AI applications using Python,
    OpenCV, TensorFlow, and Streamlit.
    """
)

# SKILLS
st.header("🛠 Technical Skills")

skills = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "OpenCV",
    "YOLOv8",
    "TensorFlow",
    "Streamlit",
    "Git & GitHub",
    "Data Science"
]

cols = st.columns(2)

for i, skill in enumerate(skills):
    cols[i % 2].write(f"✅ {skill}")

st.divider()

# PROJECTS
st.header("📂 Projects")

projects = {

    "AI Resume Analyzer":
    "ATS checker using Python and Streamlit.",

    "Vehicle Counter":
    "Real-time vehicle counting system using OpenCV.",

    "Face Mask Detector":
    "Real-time mask detection using TensorFlow and OpenCV.",

    "Attendance System":
    "Face detection-based attendance system using OpenCV.",

    "PDF Automation":
    "PDF merging, extraction, and watermarking tool."
}

for title, desc in projects.items():

    with st.container(border=True):

        st.subheader(title)

        st.write(desc)

st.divider()

# RESEARCH
st.header("🔬 Research")

st.write(
    """
    Current thesis/research area:
    
    - Solar Panel Detection
    - Drone Imagery Analysis
    - YOLOv8
    - Oriented Bounding Boxes
    - Deep Learning for Remote Sensing
    """
)

st.divider()

# CONTACT
st.header("📞 Contact")

st.write("GitHub:")
st.write("https://github.com/HaamzaZafar")

st.write("Email:")
st.write("hamxazafar98@gmail.com")