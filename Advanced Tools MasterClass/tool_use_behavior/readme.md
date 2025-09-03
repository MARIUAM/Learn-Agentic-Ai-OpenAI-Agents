

# Tool Use Behavior

Tool Use Behavior se murad hai agent ke workflow ko control karna. Agent ke configuration mein tool_use_behavior parameter hota hai jo decide karta hai ke tool call ke baad agent kya karega
openai.github.io
# Teen main modes hain:

## run_llm_again (default):
 Pehle tool chalayega, phir uska result LLM ko wapas dega taake LLM us result ki roshni mein aage analysis kare. Ye default hai
openai.github.io
.

## stop_on_first_tool: 
Pehli tool call ke turant baad agent rok jaata hai. Matlab jo raw tool output aaya, wahi final jawab hota hai aur LLM uspar aage process nahi karta
openai.github.io
.

## StopAtTools: 
Agar kuch specific tool names diye hon (jaise stop_at_tool_names=["save_data"]), to agent un tools mein se jo pehla chala uske baad ruk jayega, aur uska output final maana jayega
