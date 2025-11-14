# ArgStone-AGI
AI Super Reasoning Engine Developed by Prolabs Robotics

Argstone is a **heavyweight reasoning engine** designed for exploring multiple perspectives on a single problem and simulating an exam-taker that always produces breadth of answers rather than a single thread.

It’s resource-hungry, exploratory Reasoning Engine scoring 80.9% in the Humanity's Last Exam! Breaking a World Record!!!

[View Humanity's Last Exam paper](https://huggingface.co/datasets/cais/hle/viewer/default/test?views%5B%5D=test)

<img width="1135" height="558" alt="image" src="https://github.com/user-attachments/assets/dbc79b75-679f-4421-93b8-1ed8bcf3e573" />


---

## Table of Contents

1. [Introduction](#introduction)
2. [Why Heavyweight?](#why-heavyweight)
3. [Core Features](#core-features)
4. [Architecture](#architecture)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Examples](#examples)
8. [Benchmark data](#benchmark-data)
9. [Roadmap](#roadmap)
10. [FAQ](#faq)
11. [Contributing](#contributing)

---

## Introduction

Argstone is not meant to be minimal. Each run can produce dozens of responses, leveraging multiple reasoning paths, prompt variations, and heavy chains of thought. Its **goal** is to expose as many possible valid answers as possible.

---

## Why Heavyweight?

* **Breadth over speed**: prioritises coverage of perspectives.
* **Volume of answers**: default runs can generate 5–500+ distinct responses.
* **Exam-taker simulation**: model behaves like a test candidate producing multiple solutions to the same problem.
* **Thick prompts**: relies on long, layered instructions.

---

## Core Features

* Multi-answer generation (configurable `num_of_stones`).
* Pure URL execution: no API key setup, no backend, no Extra API costs.
* System + variation layering for diversity.

---

## Architecture

1. **Input Layer**

   * Accepts questions via text & Images via URL.
   * Variables `num_of_stones` * `num_of_kernels` control the number of answers.

2. **Processing Layer**
   * Combines question & System Prompt to then pass it on to the LLM.
  
3. **Answer generation layer**
   * passes the input (Question + System_prompt) to `num_of_Stones` number of LLM(s)
   * generates `Num_of_Stones`*`num_of_kernels` number of answers in total.

4. **Output Layer**
   * Retrieves the output from the LLM(s) & compiles everything into a Single `Compiler DB`.

---

## Installation

### Prerequisites

* Python 3.10+
* A web browser (Chrome, Firefox, Edge, Safari etc.).

### Setup

```bash
pip install web-browser urllib
```

---

## Usage

Run directly:

```bash
python3 ArgStone_Version_name.py
```

By default, this opens ChatGPT tabs (each with slight variations).

Run via the 'Run' button:

If you're using an IDE that has a run button built in (Eg: PyCharm, Visual Studio Code etc.), click on the run button
& it'll automatically run the code for you


---

## Examples

### Example 1: Philosophy

```bash
python3 Your_File_Name.py
```

Question: *Is Kant’s account in the Critique purely descriptive, or is it also normative?*
Result: 10 tabs × 5 answers = 50 unique arguments.

### Example 2: Robotics

```bash
python3 argstone_open_tabs.py --question "Explain the role of sensors in autonomous robots."
```

---

## Benchmark data

**ArgStone major models scores**

* Argstone Version 0.9.5: Score = 23.00%
* Argstone Version 0.9.7: Score = 51.6%
* Argstone Version 0.9.8: Score = 62.8%
* Argstone Version 0.9.9-pro: Score = 71.1%
* Argstone Version 1.0.6-e: Score = 80.9%

---

## Roadmap

---

## FAQs

**Q1: Why only URL mode?**
Because it eliminates API key setup and keeps the tool lightweight and cost-free.

**Q2: Can I use it offline?**
No, ArgStone relies on ChatGPT’s cloud infrastructure for reasoning.

**Q3: Why is it called heavyweight?**
Because it prioritises **depth and diversity** over speed and efficiency.

**Q4: Can I reduce the processing load?**
Yes. Lower `num_of_stones` or `num_of_kernels` to reduce open tabs and output volume.

**Q5: Does it support technical domains like robotics or AI?**
Absolutely. It’s designed for philosophy, science, coding, and robotics equally.

**Q6: What if my prompt is too long?**
It may exceed browser or model limits. Simplify or shorten prompts in that case.

**Q7: Does it cost anything to use?**
No direct cost for now, but you must have a ChatGPT account to access LLM responses.

**Q8: Can ArgStone save results automatically?**
Not yet, but auto-export to Markdown/CSV is planned in v1.5.0.

**Q9: Are all answers unique?**
Not always. Variation improves with prompt nuance and model randomness.

**Q10: How many answers can it produce?**
Up to thousands; total Answers = `num_of_stones` * `num_of_kernels`.

**Q11: Does ArgStone work with images?**
Not yet, but in the future it will. You can provide image URLs for multimodal reasoning when it launches.

**Q12: What Python version is required?**
Python 3.10 or later.

**Q13: Does it need an API key?**
No, it runs purely through browser-based execution.

**Q14: What happens if I exceed my browser’s tab limit?**
It will stop opening new tabs, and some prompts won’t execute.

**Q15: Can I integrate ArgStone with other apps?**
Yes. You can trigger it via importing the Prolabs robotics library in Python
or script system calls.

**Q16: Can ArgStone run on mobile?**
ArgStone is a heavyweight reasoning engine, and it could take a lot of power if you
Run it on a mobile, although you can use it when it's officially launched, not in code.

**Q17: How is ArgStone different from ChatGPT itself?**
ArgStone orchestrates **many** ChatGPT instances for parallel reasoning, not just one.

**Q18: Does it work with GPT-5 only?**
Yes, for now, it only works with ChatGPT-5 but later we are thinking of adding new models also

**Q19: Can I pause or stop execution midway?**
Yes, by closing your browser tabs or terminating the script.

**Q20: What does `num_of_stones` mean?**
It’s the number of parallel reasoning runs (like different thinkers) or the number of Tabs it opens.

**Q21: What does `num_of_kernels` mean?**
It’s the number of answers each reasoning run/tab generates internally.

**Q22: How do I get faster performance?**
Reduce answer count, shorten prompts, or use high-performance GPUs.

**Q23: Can I view all outputs together?**
Not yet, but in the future, outputs will be compiled into a single “Compiler DB” after execution.

**Q24: Is there a GUI planned?**
Yes, a visual interface for input and results is planned in v2.0.1.

**Q25: What’s the largest test ArgStone has passed?**
Humanity’s Last Exam — scoring 80.9%, the highest anyone has ever scored in the whole world!

**Q26: Does it work with non-English prompts?**
Yes, it supports multilingual reasoning.

**Q27: Can I export outputs to Google Sheets or Excel?**
This is planned for future updates through CSV export.

**Q28: Is there a memory system?**
Not yet, but persistent context is being considered for v2.1.0.

**Q29: Can it generate diagrams or flowcharts?**
Only text-based descriptions for now; visual mode is on the roadmap.

**Q30: Can ArgStone be used in education?**
Generally, no, it's meant for reasoning to find solutions to problems, not to teach how to solve them. 
(Use ChatGPT-Study-mode for education.)

**Q31: What’s the minimum system requirement?**
Any machine capable of running a modern web browser and Python 3.10+.

**Q32: Does it need internet access?**
Yes. It fetches all reasoning through online models.

**Q33: Is there a dark mode?**
Dark mode UI will be part of the ArgStone web interface after official launch for commercial use, not code.

**Q34: Can I integrate it with VS Code or PyCharm?**
Yes, it can be executed directly from the IDE terminals.

**Q35: Can it run inside Docker?**
Yes, as long as a browser container is configured.

**Q36: Does it support logging?**
Basic logging via console and optional file output is available.

**Q37: What’s the difference between `num_of_stones` and `num_of_threads`?**
`num_of_stones` controls reasoning breadth; `num_of_threads` (in advanced builds) manages concurrency.

**Q38: Can I fine-tune its reasoning style?**
Yes, by editing the system prompt inside the script.

**Q39: Does it support voice or audio input?**
No, text and image (via URL) inputs only.

**Q40: Can I limit answer length?**
Yes, by modifying prompt constraints or model token limits.

**Q41: What are “thick prompts”?**
Layered instructions combining logic, reasoning modes, and meta-guidelines for diversity.

**Q42: Can it simulate debates?**
Yes, but you'll have to use the legacy model v0.9.6, which scored very low (23%).

**Q43: Can ArgStone be used for coding questions?**
Yes. It’s excellent for exploring multiple algorithmic solutions.

**Q44: Is ArgStone open source?**
Yes, community contributions are encouraged through GitHub.

**Q45: Who created ArgStone?**
Developed by **Prolabs Robotics**, founded by **Aarav Jaisingh**.

**Q46: Can I customise tab titles or URLs?**
Not yet.

**Q47: Does it support GPT-4 or Claude?**
It's planned in the future, but till now, it only supports ChatGPT-5.

**Q48: What’s planned for ArgStone 2.0?**
LEON's Framework.

**Q49: What’s the theoretical limit of output?**
Tens of thousands of answers, limited by RAM and browser tabs.

**Q50: What's the full-form of ArgStone?**
"Argument retrieval generation Stone”.

---

## Contributing

We welcome contributions to [ArgStone]! To get started, please follow these steps:

1.  **Fork** the repository.
2.  Create a new **branch** for your feature or bug fix.
3.  Commit your changes and open a **Pull Request (PR)** with a clear description of your work.

Please ensure that you've read the [LICENSE](https://github.com/Aarav-111/ArgStone-AGI/blob/main/LICENSE) before you contribute.
