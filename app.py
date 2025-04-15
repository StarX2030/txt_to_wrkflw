import streamlit as st
import json
from utils.workflow import generate_workflow
from utils.visualize import visualize_workflow

# --- Streamlit UI ---
st.set_page_config(page_title="Workflow Generator", layout="wide")
st.title("📋 Structured Workflow Generator")

# User Input
project_desc = st.text_area(
    "Describe your project:", 
    placeholder="e.g., 'Build a fraud detection model with governance...'"
)

if st.button("Generate Workflow"):
    if project_desc.strip():
        # Generate JSON Workflow
        workflow = generate_workflow(project_desc)
        
        # Display JSON
        st.subheader("Generated Workflow (JSON)")
        st.code(json.dumps(workflow, indent=2), language="json")
        
        # Visualize
        st.subheader("Workflow Diagram")
        graph = visualize_workflow(workflow)
        st.graphviz_chart(graph)
    else:
        st.warning("Please enter a project description!")
