# see the code example

https://colab.research.google.com/drive/1hL3uorPX9L9zFZnS9mrpwTMPezQ8pnYO#scrollTo=c618caf4&line=3&uniqifier=1
#  Advanced Agent Tools — Concepts & Examples

Yeh guide **OpenAI Agents SDK** ke advanced tools aur unke real-world use cases ko explain karti hai. Har section mein simple explanation + example code diya gaya hai.

---

##  Topics Covered

* 🔹 Tool Use Behavior (agent tool calls handle karna)
* 🔹 Runner ki Suraksha (`max_turns` se infinite loops rokna)
* 🔹 Context-Aware Tools (`is_enabled` flag se tools ko on/off karna)
* 🔹 Error Handling (tool failures ko gracefully handle karna)
* 🔹 Stateful Tools (internal memory wale tools)
* 🔹 Production Patterns (API Gateway, Pipeline, Assistant)

---

##  Tool Use Behavior

`tool_use_behavior` decide karta hai agent tool call ke baad kya karega.

* **`run_llm_again` (default):** Tool run hota hai → result LLM ko dobara diya jata hai → LLM aage analysis karta hai.
* **`stop_on_first_tool`:** Pehle tool call ke baad agent ruk jata hai. Raw output hi final hota hai.
* **`StopAtTools`:** Agar specific tool names diye hain, to unme se pehle tool call ke baad agent ruk jata hai.

### ✅ Example

```python
from agents import Agent, function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

agent = Agent(
    name="WeatherAgent",
    instructions="Shaher ka mausam batao",
    tools=[get_weather],
    tool_use_behavior="stop_on_first_tool"
)
```

Output:

```
The weather in Karachi is sunny
```

---

## 🛡️ Runner ki Suraksha (max\_turns)

`Runner.run` mein `max_turns` ek **hard limit** hai jo infinite loops rokta hai.

```python
from agents import Runner, MaxTurnsExceeded

try:
    result = await Runner.run(agent, "User query", max_turns=5)
    print("Agent Output:", result.final_output)
except MaxTurnsExceeded:
    print("Error: Agent max_turns limit cross kar gaya")
```

👉 Agar `max_turns=1` aur agent ko tool call karna pada, to wo pehle step ke baad hi ruk jayega.

---

## 🔑 Context-Aware Tools (is\_enabled)

Tools ko context ke hisaab se on/off kiya ja sakta hai.

```python
def is_user_admin(context, agent) -> bool:
    return context.get("user_role") == "admin"

@function_tool(is_enabled=is_user_admin)
def delete_user(user_id: str) -> str:
    return f"User {user_id} has been deleted."
```

👉 Ye tool sirf **admin users** ke liye enable hoga.

---

## ⚠️ Error Handling (Tool Failures)

Tools fail ho sakte hain, isliye errors ko **gracefully handle** karna zaroori hai.

```python
@function_tool
def divide(a: int, b: int) -> str:
    try:
        return str(a / b)
    except ZeroDivisionError:
        return "Error: Zero se divide nahi kar sakte. Alag number do."
```

Output:

* `divide(10, 2) → "5.0"`
* `divide(8, 0) → "Error: Zero se divide nahi kar sakte. Alag number do."`

---

## 🧠 Stateful Tools

Normally tools **stateless** hote hain. Lekin agar memory chahiye, `FunctionTool` se stateful tools bana sakte hain.

```python
from agents import FunctionTool

class CounterTool(FunctionTool):
    def __init__(self):
        self._count = 0
        super().__init__(
            name="incrementing_counter",
            description="Har call par ek barhta hua counter",
            params_json_schema={"type": "object", "properties": {}},
            on_invoke_tool=self.on_invoke_tool
        )

    async def on_invoke_tool(self, context, args_json_str) -> str:
        self._count += 1
        return f"Abhi count hai: {self._count}"
```

👉 Har baar call karne par counter increment hota hai.

---

## 🏗️ Production Patterns

Real-world mein alag patterns use hote hain:

* **API Gateway (Single Action):**
  `tool_use_behavior="stop_on_first_tool"` → direct response.

* **Data Pipeline (Workflow):**
  `tool_use_behavior=StopAtTools([...])` → chain of tools until final.

* **Interactive Assistant (Iterative Thinking):**
  Default `run_llm_again` → har step ke baad LLM sochta hai.

### Example: API Gateway Pattern

```python
agent = Agent(
    name="QuickLookupAgent",
    instructions="User se ek cheez find karo.",
    tools=[file_search_tool, web_search_tool],
    tool_use_behavior="stop_on_first_tool"
)
```

---

## 📜 Summary

By combining:

* `tool_use_behavior`
* `max_turns`
* `is_enabled`
* proper error handling
* (optional) stateful tools

👉 Aap apne agent ko **safe, controlled aur predictable** bana sakte ho.

---

## 📝 License

This project is licensed under the **MIT License**.

---




