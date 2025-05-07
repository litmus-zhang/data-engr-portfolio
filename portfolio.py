import streamlit as st
from PIL import Image
import json

# Page configuration
st.set_page_config(
    page_title="Your Name | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")  # Create a style.css file (see CSS below)

# Load projects data from JSON file
with open("projects.json") as f:
    projects_data = json.load(f)

# --- Hero Section ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Hi, I'm [Your Name] 👋")
    st.subheader("Robotics Engineer | AI Developer | Educator")
    st.write("""
    Passionate about building intelligent systems and teaching the next generation of engineers.
    Currently working at [Your Lab/Company] where we develop cutting-edge robotics solutions.
    """)
    
    # Resume and Contact buttons
    st.download_button(
        label="📄 Download Resume",
        data=open("resume.pdf", "rb").read(),
        file_name="YourName_Resume.pdf",
        mime="application/pdf"
    )
    st.write("[📧 Email Me](mailto:your.email@example.com)")

with col2:
    # Add your profile image (save as 'profile.jpg' in same folder)
    image = Image.open("profile.jpg")
    st.image(image, width=250)

# --- Tech Stack Section ---
st.header("🛠️ Tech Stack")
tech_columns = st.columns(4)
techs = [
    {"name": "Python", "icon": "🐍"},
    {"name": "ROS", "icon": "🤖"},
    {"name": "TensorFlow", "icon": "🧠"},
    {"name": "OpenCV", "icon": "👁️"},
    {"name": "Arduino", "icon": "⚡"},
    {"name": "Raspberry Pi", "icon": "🍓"},
    {"name": "Streamlit", "icon": "🖥️"},
    {"name": "Docker", "icon": "🐳"},
]

for i, tech in enumerate(techs):
    with tech_columns[i % 4]:
        st.markdown(f"""
        <div class="tech-card">
            <span class="tech-icon">{tech['icon']}</span>
            <span class="tech-name">{tech['name']}</span>
        </div>
        """, unsafe_allow_html=True)

# --- Projects Section ---
st.header("🚀 Projects")
st.write("Here are some of my recent projects. Click on any to learn more.")

# Display project cards in a grid
project_columns = st.columns(3)
for i, project in enumerate(projects_data):
    with project_columns[i % 3]:
        with st.expander(f"### {project['title']}"):
            st.image(project["image"], use_column_width=True)
            st.write(project["short_description"])
            st.markdown(f"[🔗 View Project]({project['link']})")

# --- Detailed Project View ---
selected_project = st.selectbox(
    "Select a project to view details",
    [project["title"] for project in projects_data]
)

if selected_project:
    project = next(p for p in projects_data if p["title"] == selected_project)
    st.header(project["title"])
    st.image(project["image"], width=500)
    st.write(project["long_description"])
    st.markdown(f"**Technologies Used:** {project['technologies']}")
    st.markdown(f"[🔗 GitHub Repository]({project['link']})")

# --- Contact Section ---
st.header("📬 Contact Me")
contact_form = """
<form action="https://formsubmit.co/your.email@example.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)