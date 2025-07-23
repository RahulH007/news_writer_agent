#!/usr/bin/env python
import sys
import warnings

from crew import AiNews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from datetime import datetime
def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'The world without the internet',
    }
    
    try:
        AiNews().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()