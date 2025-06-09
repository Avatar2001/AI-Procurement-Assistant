from crewai import Task
import os

def get_report_verifier_task(agent, output_dir):
    return Task(
    description="\n".join([
        "The task is to verify the generated HTML page for the procurement report.",
        "Check for the following:",
        "- All 8 required sections are present and clearly labeled.",
        "- Bootstrap CSS framework is used properly for responsive layout and styling.",
        "- The content is coherent, well-structured, and reflects the analysis correctly.",
        "- Tables and charts are readable and styled professionally.",
        "- There are no broken tags or major formatting issues.",
        "- Recommendations and analysis are logically derived from findings.",
        "- The HTML follows best practices and is valid.",
        "Provide a detailed verification summary at the top and insert inline comments where improvements are needed."
    ]),
        expected_output="Annotated HTML report",
        input_file=os.path.join(output_dir, "proccurement_report.html"),
        output_file=os.path.join(output_dir, "verified_proccurement_report.html"),
        agent=agent
    )