from typing import Dict, List
import re
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(project_description)
verbs = [token.text for token in doc if token.pos_ == "VERB"]

st.download_button("Download JSON", json.dumps(workflow), "workflow.json")

def generate_workflow(project_description: str) -> Dict:
    """Convert text into a structured workflow JSON."""
    # Example: Split sentences into tasks (customize with NLP for real use)
    sentences = re.split(r'[.,]', project_description)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    tasks = []
    for i, sentence in enumerate(sentences[:5]):  # Limit to 5 tasks for demo
        tasks.append({
            "id": str(i + 1),
            "title": f"Task {i + 1}: {sentence[:30]}...",
            "description": sentence,
            "depends_on": [] if i == 0 else [str(i)],
            "priority": "High" if i == 0 else "Medium",
            "owner": "Unassigned",
            "tags": ["Planning"] if i == 0 else ["Execution"],
            "status": "Not Started"
        })
    
    return {
        "project": project_description[:50] + ("..." if len(project_description) > 50 else ""),
        "tasks": tasks
    }
