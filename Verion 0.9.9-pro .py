import webbrowser
import urllib.parse

# Define a "system prompt" that instructs the AI how to behave.
# Here, the AI is roleplaying as an exam taker who should generate
# 15 distinct answers to a multiple-choice question, with reasoning.

# define how any answers you want to get
num_of_answers = 5

system_prompt = f"""
Give {num_of_answers} distinct answers. For each, show the full calculation or step-by-step working that leads to that answer, as if solving it on paper. Do not rank the answers.
"""

question = """
Which was the first statute in the modern State of Israel to explicitly introduce the concept of "good faith"? (Do not append "the" or the statute's year to the answer.)
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
