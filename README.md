# ArgStone-AGI
# AI Super Reasoning Engine


# Argstone Version 0.9.7 Readme.md file

Argstone is a **heavyweight reasoning engine** designed for exploring multiple perspectives on a single problem and simulating an exam-taker that always produces breadth of answers rather than a single thread.

It’s resource-hungry, exploratory Reasoning Engine

---

## Table of Contents

1. [Introduction](#introduction)
2. [Why Heavyweight?](#why-heavyweight)
3. [Core Features](#core-features)
4. [Architecture](#architecture)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Examples](#examples)
8. [Performance Notes](#performance-notes)
9. [Roadmap](#roadmap)
10. [FAQ](#faq)
11. [Contributing](#contributing)

---

## Introduction

Argstone is not meant to be minimal. Each run can produce dozens of responses, leveraging multiple reasoning paths, prompt variations, and heavy chains of thought. Its **goal** is to expose as many possible valid answers as possible.

---

## Why Heavyweight?

* **Breadth over speed**: prioritises coverage of perspectives.
* **Volume of answers**: default runs can generate 5–100+ distinct responses.
* **Exam-taker simulation**: model behaves like a test candidate producing multiple solutions.
* **Thick prompts**: relies on long, layered instructions.

---

## Core Features

* Multi-answer generation (configurable `num_of_stones`).
* Pure URL execution: no API key setup, no backend.
* System + variation layering for diversity.
* Exam-simulation: generate mock exam questions and answers.
* Optional logging of generated prompts for reproducibility.

---

## Architecture

1. **Input Layer**

   * Accepts questions via text.
   * Variables like `num_of_stones` control the number of answers.

2. **Processing Layer**

   * Expands input into multiple structured prompts.
   * Inserts controlled variations for diversity.

3. **Output Layer**

   * Encodes the full prompt as a URL.
   * Opens multiple browser tabs, one per variation.

---

## Installation

### Prerequisites

* Python 3.10+
* A web browser (Chrome, Firefox, Edge, Safari).

### Setup

```bash
pip install web-browser urllib
```

---

## Usage

Run directly:

```bash
python3 Your_File_Name.py
```

By default, this opens 10 ChatGPT tabs (each with slight variations).

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

## Performance Notes

* Argstone is deliberately heavyweight.
* Opening >10 tabs can slow your browser.
* Very long prompts may hit URL length limits (try trimming input if needed).

---

## Roadmap

---

## FAQ

**Q1: Why only URL mode?**
Because this version avoids the need for API keys, keeping setup minimal and cost-free.

**Q2: Can I use it offline?**
No, since it relies on ChatGPT on the cloud.

**Q3: Why is it heavyweight?**
It’s designed for depth and coverage, not speed.

**Q4: Can I reduce the load?**
Yes, lower the `num_of_stones` value or shorten prompts.

**Q5: Does it work for technical questions?**
Yes, it can handle philosophy, science, robotics, politics, or other creative domains.

**Q6: What happens if my prompt is too long?**
URLs can break if they exceed length limits (1 Million Tokens); shorten or simplify the input.

**Q7: Does it cost anything to run?**
No direct cost. It just opens ChatGPT tabs in your browser, which may require a ChatGPT account to use ChatGPT-5 but without an Account, it'll use GPT-4o.

**Q8: Can it save my results automatically?**
Not yet. Planned features include Markdown/CSV export of all answers.

**Q9: Will Argstone always generate unique answers?**
Variations help, but duplicates may still appear; the diversity improves with more nuanced prompts.

**Q10: Who is Argstone for?**
Students, researchers, and developers who want to explore a wide range of possible answers instead of a single narrow response.

---

## Contributing

Contributions welcome! Fork, branch, or open a PR.
