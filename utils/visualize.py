import graphviz

def visualize_workflow(workflow: Dict) -> graphviz.Digraph:
    """Generate a Graphviz diagram of the workflow."""
    dot = graphviz.Digraph(
        comment=workflow["project"],
        graph_attr={"rankdir": "LR"}  # Left-to-right layout
    )
    
    # Add nodes (tasks)
    for task in workflow["tasks"]:
        dot.node(
            task["id"],
            label=f"{task['title']}\nPriority: {task['priority']}",
            shape="box",
            style="filled",
            fillcolor="lightblue" if task["priority"] == "High" else "lightgrey"
        )
    
    # Add edges (dependencies)
    for task in workflow["tasks"]:
        for dep in task["depends_on"]:
            dot.edge(dep, task["id"])
    
    return dot
