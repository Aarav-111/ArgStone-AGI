import webbrowser
import urllib.parse

# Define a "system prompt" that instructs the AI how to behave.
# Here, the AI is roleplaying as an exam taker who should generate
# 15 distinct answers to a multiple-choice question, with reasoning.

# define how any answers you want to get
num_of_answers = 5

system_prompt = f"""
You are an exam taker.
For the following multiple-choice question, give {num_of_answers} DIFFERENT possible answers (no duplicate).
Each answer should be labeled Answer 1 through Answer {num_of_answers}.
Do not just repeat reasoning; commit to {num_of_answers} distinct choices from the options.

SHOW FULL, Detailed working before answering
"""

question = """
Which flying unit from 1 tier building in BAR can shoot and stun enemy targets?
"""

# Merge system message + question into a single full prompt
full_prompt = f"{system_prompt}:\n\n{question}"

# Encode the full prompt text into a URL-safe format
encoded_prompt = urllib.parse.quote(full_prompt)

# Construct the final URL to directly open ChatGPT with the encoded query
URL = f"https://chat.openai.com/?q={encoded_prompt}&temporary-chat=true"

# Choose how many browser tabs to open with the query.
# The playful variable name "Num_of_stones" hints at "Infinity Stones."

Num_of_stones = 10  # The more tabs opened, the more parallel queries, the better

# Open the generated URL in new browser tabs, one per loop cycle
for _ in range(Num_of_stones):
    webbrowser.open_new_tab(URL)
