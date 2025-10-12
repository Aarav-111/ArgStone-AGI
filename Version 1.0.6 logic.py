import webbrowser
import urllib.parse

# ===== Config =====
num_of_kernels = 50          # how many answers you want
Num_of_stones = 30          # how many tabs per question

# ===== System Prompt =====
system_prompt = f"""
Generate **exactly {num_of_kernels} unique answers** to the user’s question, divided as follows:

* **{num_of_kernels/10} Correct Answers:** Mathematically or logically correct results.
* **{num_of_kernels/2} Sign/Operator Variations:** Create variations by **changing** or **adding** mathematical signs and operators (`+`, `-`, `*`, `/`).

  * You may also **add a leading sign** (e.g., `+`, `-`) at the start of the expression.
  * Do **not** alter the numbers, variables, or structure except through sign/operator adjustments.
* **{num_of_kernels/2-num_of_kernels/10} Uncertain Answers:** Plausible but unverified expressions; not necessarily wrong.

After listing all answers by category, include a **final summary table** with columns:
**# | Answer | Category (Correct / Sign Variation / Uncertain) | Confidence (1–10)**

**Rules:**

* No duplicates.
* Variations must involve only operator or sign edits (including added prefix signs).
* Keep syntax valid and clear.
* No filler, explanations, or meta text.
* Maintain logical order and consistent format.
* Show Full Working before answering any question(s)

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
    webbrowser.open_new_tab(url)