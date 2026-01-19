import streamlit as st

def render_diagram(dot_code: str, height: int = 500, use_container_width: bool = False):
    """
    Renders a Graphviz diagram natively in Streamlit.
    Default styling is applied to ensure a professional look.
    """
    # Wrap in a basic digraph if not already provided
    if not dot_code.strip().startswith(("digraph", "graph")):
        dot_code = f'''digraph {{
    graph [
        rankdir=LR, 
        center=true, 
        bgcolor="transparent",
        nodesep=0.4,
        ranksep=0.4,
        margin=0.2,
        pad=0.2,
        fontname="Inter, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    ];
    node [
        shape=rect, 
        style="filled,rounded", 
        fontname="Inter, Segoe UI, Roboto, Helvetica, Arial, sans-serif", 
        fillcolor="#FFFFFF", 
        color="#E1E4E8", 
        fontcolor="#24292E",
        fontsize=12,
        penwidth=1.5,
        width=2.5,
        height=0.6
    ];
    edge [
        color="#8B949E", 
        arrowsize=0.8, 
        penwidth=1.2,
        fontname="Inter, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
        fontsize=10
    ];
    {dot_code}
}}'''
    
    st.graphviz_chart(dot_code, use_container_width=use_container_width)
