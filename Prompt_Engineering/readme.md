#  Prompt Engineering Guide ( GPT-4.1 )

This repo also includes a short introduction to **Prompt Engineering** for beginners.  
For more details, check out the official OpenAI Cookbook guide:  
👉 [OpenAI Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)

---
# 📘 GPT-4.1 Prompting Guide

Bilkul! Aaiye **GPT-4.1 Prompting Guide** ka ek concise aur deep yet easy-to-understand **summary** tayar karte hain—taake aap ya koi bhi naya user isay asaani se samajh jaaye:

---

## GPT-4.1 Prompting Guide – Simplified but Deep Overview

### Model mein Badlaav: Literal aur Powerful

* GPT-4.1, GPT-4o se kaafi behtar hai—ye **zaida literal** prompts ko follow karta hai, matlab ambiguity nahi chalta. Ek sentence se clear behavior reset ho jaata hai.([OpenAI Cookbook][1], [Reddit][2], [Prompthub][3])
* Ye tool-calling mein bhi kaafi improved hai—prompt mein function definitions dena aur unhe structured “tools” field ke zariye define karna ideal approach hai.([Reddit][2], [Prompthub][3], [Wikipedia][4])

---

### 1. Agentic Workflows – Workflow ko khud chalane wala

GPT-4.1 multi-step tasks ke liye banaya gaya hai, jaise:

* **System Prompt Reminders**: Remind kare ke aap ek agent ho, user prompt poori tarah complete karo.
* **Tool Calls**: Tools ko accurately use karo, hallucinate mat karo.
* **Planning (Chain-of-Thought)**: Step-by-step reasoning ko encourage karo.([Scribd][5], [OpenAI Cookbook][1])

---

### 2. Long Context Handling – Lambay context ko efficiently use karo

* GPT-4.1 ek **million token** context window support karta hai.([Prompthub][3], [Wikipedia][4])
* Best practice: Instructions ko **context ke pehle aur baad dono jagah** daalo (“sandwich method”); agar ek jagah hi daalna hai to **context ke baad** daalna zyada effective hai.([Reddit][2], [Prompthub][3], [AI Agents News][6])

---

### 3. Chain-of-Thought – Soch ko step-by-step karo

GPT-4.1 automatic reasoning default nahi karta—agar reasoning chahiye, prompt mein explicitly likho (“Think step-by-step…”, “Plan before answering…”).([Reddit][2], [Prompthub][3])

---

### 4. Instruction Following – Clear aur specific hone ka faida

* GPT-4.1 ambiguous instructions ya “assume” wala behavior nahi karta; **explicit instructions** do toh wahi follow karega.([OpenAI Cookbook][1], [Reddit][2], [Prompthub][3])
* Agar output expected nahin hai, ek clear clarifying line add karo—kaam set.([OpenAI Cookbook][1])

---

### 5. General Prompting Advice – Structure aur formatting par focus

* Use **structured format**:

  * **Role & Objective**
  * **Instructions**
  * **Optional Sub-instructions**
  * **Reasoning Steps**
  * **Output Format**
  * **Examples**
  * **Final Instructions**([Prompthub][3], [AI Agents News][6])

* Important cheezein **prompt ke start aur end** dono jagah mention karo for reinforcement.([Reddit][7], [Prompthub][3])
* Delimiters (like “---” or markup) use karo to clearly separate sections.([OpenAI Cookbook][1], [Prompthub][3])

---

### GPT-4.1 Prompting Guide — Aap ke liye ek sher (summary)

| Key Element           | Deep Samjhaana                                                                    |
| --------------------- | --------------------------------------------------------------------------------- |
| **Literal Following** | GPT-4.1 strictly literal prompts follow karta hai—ambiguity se kaam nahi chalta.  |
| **Agentic Workflows** | Model ko system reminders, tool use block, planning prompts se empower karo.      |
| **Context Handling**  | Long documents ke liye context me instructions ko start + end mein daalo.         |
| **Chain-of-Thought**  | Agar reasoning chahiye, prompt mein clearly bolna padega.                         |
| **Prompt Structure**  | Structured sections: Role, Instructions, Planning Steps, Examples, Output Format. |

---

### Summary in simple Urdu

**GPT-4.1 ek zyada precise, structured aur understandable AI model hai. Ye unclear prompts ko follow nahi karta, balki har instruction ko literal follow karta hai—jise hum prompt engineering mein “explicitness” kehte hain. Aap agar multi-step workflows banana chahte ho (jaise tools call karna, plan banana, process complete karna), to clear structure, context handling, plus reasoning model se best results milte hain.**

---

[1]: https://cookbook.openai.com/examples/gpt4-1_prompting_guide?utm_source=chatgpt.com "GPT-4.1 Prompting Guide"
[2]: https://www.reddit.com/r/PromptEngineering/comments/1k6yid7/openai_dropped_a_prompting_guide_for_gpt41_heres/?utm_source=chatgpt.com "OpenAI dropped a prompting guide for GPT-4.1, here's ..."
[3]: https://www.prompthub.us/blog/the-complete-guide-to-gpt-4-1-models-performance-pricing-and-prompting-tips?utm_source=chatgpt.com "The Complete Guide to GPT-4.1: Models, Performance ..."
[4]: https://en.wikipedia.org/wiki/GPT-4.1?utm_source=chatgpt.com "GPT-4.1"
[5]: https://www.scribd.com/document/859440350/GPT-4-1-Prompting-Guide-OpenAI-Cookbook?utm_source=chatgpt.com "GPT-4.1 Prompting Guide _ OpenAI Cookbook | PDF"
[6]: https://aiagent.marktechpost.com/post/the-ultimate-gpt-4-1-prompting-guide-by-openai?utm_source=chatgpt.com "The Ultimate GPT-4.1 Prompting Guide by OpenAI"
[7]: https://www.reddit.com/r/ChatGPTPro/comments/1jzyf6k/openai_just_dropped_a_detailed_prompting_guide/?utm_source=chatgpt.com "OpenAI just dropped a detailed prompting guide and it's ..."



# code Example

# 🧑‍💻 Example: Weather Helper Agent with GPT-4.1

Yeh ek simple demo hai jisme humne **Prompt Engineering structure** (Role, Instructions, Tool-use, Reasoning, Output format, etc.) apply kiya hai aur GPT-4.1 ko ek **Weather Agent** banaya hai.

---

## 🚀 Code Example

```python
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ─────────────────────────────────────────────────────────────
# SYSTEM PROMPT TEMPLATE  ➜ maps to your headings one by one
# ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """
# Role and Objective
You are a Weather Helper agent. Your objective is to answer user weather queries by correctly using the get_weather tool and returning a short, friendly summary.

# Instructions
- Be brief, accurate, and helpful. If something is missing, ask a focused question.
- If tool output conflicts with your prior knowledge, trust the tool output.
- Never invent data; if the tool fails, say what failed and suggest next step.

## Sub-categories for more detailed instructions
### Tool-use
- If a city is provided, call get_weather with that city.
- If city is missing or unclear, ask the user for the city (do NOT guess).
### Persistence
- Continue the task until the user’s query is resolved; don’t stop right after planning or just a tool call.
### Planning
- Before each tool call, briefly plan internally. After tool results, reflect internally.
- Only share a concise, high-level rationale with the user (no internal chain-of-thought).

# Reasoning Steps
(Think step by step internally. Decide: Do I have city? If yes ➜ call tool. If not ➜ ask for city. After tool, summarize result clearly.)

# Output Format
- Start with one-line answer.
- Then 1–3 bullets: temp, condition, any note.
- If information is missing, ask exactly what’s needed in one short question.

# Examples
## Example 1
User: "Weather in Lahore?"
Assistant: (plan internally) ➜ call get_weather(city="Lahore") ➜ summarize result.

# Context
- Data source is the get_weather tool provided by the app.
- If the tool errors or returns null, say: "I couldn’t get the weather right now." and suggest trying again.

# Final instructions and prompt to think step by step
- Think step by step silently; show only the final answer + 1–3 bullets.
- If you need more info, ask a single, direct question and wait.
"""

# ─────────────────────────────────────────────────────────────
# TOOL DEFINITION (function calling schema)
# ─────────────────────────────────────────────────────────────
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city (returns temperature and condition).",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g., 'Lahore'."}
                },
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    }
]

# ─────────────────────────────────────────────────────────────
# (Demo) our backend function to fulfill the tool call
# In real app, yahan OpenWeatherMap ya kisi real API ko hit karna hota hai.
# ─────────────────────────────────────────────────────────────
def get_weather_backend(city: str) -> dict:
    demo = {
        "Lahore": {"temperature": "32°C", "condition": "Sunny"},
        "Karachi": {"temperature": "30°C", "condition": "Humid"},
    }
    return demo.get(city, {"temperature": "N/A", "condition": "Unknown"})

# ─────────────────────────────────────────────────────────────
# STEP 1: user message
# ─────────────────────────────────────────────────────────────
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Tell me the weather in Lahore."}
]

# ─────────────────────────────────────────────────────────────
# STEP 2: first model call — it should propose a tool call
# ─────────────────────────────────────────────────────────────
first = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=tools
)

msg = first.choices[0].message
tool_calls = msg.tool_calls or []

if tool_calls:
    call = tool_calls[0]
    tool_name = call.function.name
    args = json.loads(call.function.arguments or "{}")

    if tool_name == "get_weather":
        tool_result = get_weather_backend(args.get("city", ""))

        messages += [
            msg,
            {
                "role": "tool",
                "tool_call_id": call.id,
                "name": tool_name,
                "content": json.dumps(tool_result)
            }
        ]

        final = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages
        )
        print(final.choices[0].message.content)
else:
    print(msg.content or "No content from model.")

