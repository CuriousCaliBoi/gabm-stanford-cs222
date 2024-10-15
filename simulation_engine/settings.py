import sys
import os
from pathlib import Path

OPENAI_API_KEY ="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"
KEY_OWNER = "Rohan Saxena"
DEBUG = True
MAX_CHUNK_SIZE = 4
LLM_VERS = "gpt-4o-mini"
BASE_DIR = f"{Path(__file__).resolve().parent.parent}"
POPULATIONS_DIR = f"{BASE_DIR}/agent_bank/populations"
LLM_PROMPT_DIR = f"{BASE_DIR}/simulation_engine/prompt_template"