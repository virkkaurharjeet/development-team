#!/usr/bin/env python
import os
import sys
import warnings

from datetime import datetime

from dev_team.crew import DevTeam

os.makedirs('output', exist_ok=True)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    project_requirements = """ Create a UI which have option to add items to todo list. Editing of item name should also be allowed. Item should have a mandatory title, optional deadline date . The list should be displayed with a checkbox at front which can be used to an item completed. There should be a delete btn at end of each list item which will allow to delete an item."""
    module_name = "todolist.py"
    class_name = "TodoList"

    inputs = {
        'project_requirements': project_requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    try:
        result = DevTeam().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()

