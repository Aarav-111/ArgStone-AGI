import webbrowser
import urllib.parse

# ===== Config =====
num_of_kernels = 50          # how many answers you want
Num_of_stones = 30          # how many tabs per question

# ===== System Prompt =====
system_prompt = f"""Give {num_of_kernels} distinct answers (No Duplicates). For each, show the full calculation or step-by-step working that leads to that answer, as if solving it on paper. Do not rank the answers.

"""

# ===== Place your question here =====
question = r"""
Which was the first statute in the modern State of Israel to explicitly introduce the concept of "good faith"? (Do not append "the" or the statute's year to the answer.)
"""

# ===== Launcher =====
base_url = "https://chat.openai.com/?q={}&temporary-chat=true"

full_prompt = f"{system_prompt}\n\n{question}"
encoded_prompt = urllib.parse.quote(full_prompt)
url = base_url.format(encoded_prompt)

for _ in range(Num_of_stones):
    webbrowser.open(url)