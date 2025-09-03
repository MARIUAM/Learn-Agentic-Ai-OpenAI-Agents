# Advanced Handoffs (Aasan Alfaaz Mein)

## Handoff ka matlab kya hai?

Socho ke aap madad chahte ho aur pehle ek dost aapki baat sun raha hai.  
Lekin agar aapke sawaal zyada mushkil ho, toh pehla wala dost kehta hai:  
“Mujhe yeh solve karna mushkil hai, main tumhe apne expert dost ke paas transfer karta hoon.”

Yehi handoff hota hai – aapki baat ek specialist (kisi khaas shakhs ya agent) ko aage bejana.

---

## Basic Handoff

- Sirf ek friend se dusre friend ko call transfer karna.
- Pehla friend apni jagah chup ho jata hai, aur dusra friend ab aapki madad karta hai.

## Advanced Handoff

- Yahan pehla friend dusre friend ko complete briefing deta hai, matlab aapki problem ka summary bata deta hai, taake dusra friend ko turant samajh aaye ki kya masla hai.

---

## Handoff ko Customize Kaise Karte Hain? (Tool ka Naam Badalna aur Logging)

### Tool Name Change Karna

- Har agent ke paas ek “tool” hota hai jo usko kaam batane ke liye dikhai deta hai.
- Handoff me ham ye naam change kar sakte hain, jaise `transfer_to_refund_agent` ko `escalate_to_refunds` karna, taake clear ho jaye ki ab ye tool “Refund Specialist” ke paas ja raha hai.

### Log (Note) Karna

- Jaise dentist appointment me record ban jata hai, waise hi jab aap kisi specialist ko bhej rahe ho, ek log function chal sakta hai jo screen pe likhta hai:
  > “Handoff Initiated: User ko specialist agent ke paas transfer kiya.”
- Isse humein pata lagta rahta hai ki handoff hua bhi ya nahi.

**Example:**

```python
custom_handoff = handoff(
    agent=specialist_agent,
    tool_name_override="escalate_to_specialist",      # Tool ka naya naam
    tool_description_override="Use this for complex issues that require a specialist.",
    on_handoff=log_handoff_event,                      # Callback jo record karega
)
```
Yahan `on_handoff` matlab jab bhi ye handoff hogi, ek function chalega jo likh dega.

---

## Structured Data Pass Karna (Briefing Note)

Immagine karo ke pehle friend dusre friend ko “briefing note” bhej raha hai.  
Is note me likha hota hai aapki problem ka short summary, jese:  
“Payment problem, order_id 12345”

**Structured Data:**  
Ek special form jese list ya fields jisme exact information hoti hai.  
Jaise ek choti form jisme `reason: "Payment failed", order_id: "12345"`.

Is se fayda ye hota hai ki naya agent turant samajh jata hai kyun handoff hua aur kya karna hai.

**Example:**

```python
class EscalationData(BaseModel):
    reason: str
    order_id: str

escalation_handoff = handoff(
    agent=refund_agent,
    on_handoff=on_escalation,       # Jab handoff hogi, ye print karega note
    input_type=EscalationData,      # LLM (pehla agent) se ye data maang rha hai
)
```
Yahan agar pehla agent EscalationData nahi deta, toh handoff nahi hoga.  
Matlb agent ko keh rahe:  
“tum mujhe samajha ke batao kyun handoff kar rahe ho, order number kya hai.”

---

## Conversation History Saaf Rakhna (Filtering)

Kabhi kabhi pehla agent ne bohat saare tools (search, calculator, etc.) use kiye hote hain.  
Jab dusra agent involve hota hai, unko sirf zaroori baatein dikhani chahiye, puri purani technical history nahi.

### Filtration

- **Input Filter:** Ye ek chhota sa filter lagaya ja sakta hai taake jab naya agent aapki baat sunay, sirf asal sawaal aur zaroori jawab dikhai dein, saare tool ke dohraaye hue lines hat jaaye.

**Example:**

```python
handoff_filters.remove_all_tools
```
Bas yeh karta hai ki tool calls aur outputs hata de, taake conversation sirf normal messages ka ho jisme aap aur pehle wala agent (triage) baat kar rahe the.

**Simple Example:**  
Triage ne kai sawal pooche (tools se jaankar) aur phir final sawal nikla:  
“Fasting kitna time hai?”  
Jab FAQ agent (simple jawab dene wala) ke paas jao, toh unko sirf pichla sawaal dikhana chahta hoon, tool ki details nahi.  
Filter kar ke circuit saaf ho gaya.

---

## Poore Majmue ki Raftaar Samajhna (Prompting for Success)

Agent ko clearly batana hota hai ki uska kaam kya hai aur kab handoff karna hai.  
Agar instructions clear hon, to agent ko confusion nahi hogi.

### Prompt Prefix

Ek special text jesa `RECOMMENDED_PROMPT_PREFIX` diya jata hai, jise aap apne instructions ke pehle laga sakte ho.  
Isme likha hota hai:  
“Hum aapka friend hain, aapko diagnosis karna hai aur agar billing issue ho to Billing Agent ko bhejna hai.”

### Explicit Routing

Jaise doctor training me kehte hain, if X problem then do Y:

- agar billing se related sawal hai → Billing Agent ko bhejo  
- agar refund ki baat hai → Refund Agent ko

Iss se agent ko step-by-step pata rahta hai, jaise:  
“Main sab pehle analyze karunga, phir specialist ko handoff karunga.”

---

## Conversation ka Silsaal (Multi-turn)

Handoff hone ke baad user phir se message bhejta hai (jaise user:  
“Shukriya, ab kya karenge?”).

Ab decide karna hai ke agla jawab kaun dega:

### Resume with Triage Agent (Safe Tarika)

- Pura conversation dobara main agent (triage) ke paas le aao.
- Triage agent pehle hoga aur phir woh decide karega ki phir se same specialist se baat karna hai ya kuch aur karna hai.
- Ye safe hai kyunki hamari flow control wapas triage ke paas hai.

### Resume with Specialist (Efficient Tarika)

- Seedha wahi specialist agent jo last me aapki madad kar raha tha, us se continue karo.
- Matlab specialist ko turant dobara bol dete hain, poora background sab uske paas hai (history wapas dal ke).
- Isse baar baar triage repeat nahi karna padta.

---

## Example Sequence

- **Triage Agent:** “Aapko problem identify karne ka try karta hai.” (Ye agent diagnose tool use karke batata hai “payment fail hui.”)
- **Handoff (billing_agent):** “Pata chala aapka paise ki problem hai, bill pay nahi ho raha. Toh yeh summary lekar specialist ke paas bhejte hain.”
- **Specialist ke paas:** Logging message aata hai:  
  `[SYSTEM: Handoff initiated. Briefing: 'User's payment failed.']`  
  Phir Billing Agent se user ki baat agee badhta hai.
- **User bolta:** “Shukriya, ab refund kitni der me hoga?”  
  Toh aap seedha Billing Agent ke paas baat kara sakte ho, kyunki wahi ab aapki madad kar raha tha.
- **Result:** Final jawab Billing Agent deta hai.

---

## Handoffs vs Agents-as-Tools (Farq kya hai)

### Handoffs

- Jab baat complex lambi conversation ki hai aur ek aur specialist agent ko aapki madad chahiye.
- Ye aisa hai jaise doctor patient ko ek specialist ke paas bhej deta hai, aapki puri story batakar.
- Specialist phir aapka case hold karta hai.

### Agents-as-Tools

- Chhote chhote kaam ke liye.
- Jaise ek translator ya calculator jaisa tool jisme ek main agent pooche aur tool fatafat kaam karke result deta hai, phir main agent aage bajah.
- Ittafaq nahi ki ek agent dusre ko transfer karta rahe; yahan main agent sab kuch manage karta hai aur sirf madad mangta rehta hai.

---

## Wrap-Up (Aakhri Baatein)

- **Handoff kya hai:** Jab ek agent user ko doosre agent ke paas smoothly pass karta hai.
- **Customizing Handoff:** Hum tool ka naam change kar sakte aur ek callback (log) set kar sakte hain, taake kisi specialist ko transfer karte waqt hamein note mil jaye.
- **Structured Data (Briefing):** Triage agent ko majboor kar sakte hain ki woh ek chhota sa note handoff ke waqt de de (jaise “Issue: payment failed”). Isse specialist ko sab saari baat pehle hi clear mil jaati hai.
- **Cleaning Conversation:** Jab naya agent aata hai, purana technical history hata sakte hain (filters lagakar), taake sirf seedhi user ki baat samne aaye.
- **Prompt Instructions:** Har agent ko clear directions do ke uska kaam kya hai aur kab handoff karna hai, jaise “agar billing ka issue hai to billing specialist ko bhejo.” Ye instructions seedhe prompt me de do.
- **Continuing Conversation:** Handoff ke baad ya to firse triage agent se baat karke specialist tak poncho, ya seedha wohi specialist lagatar user ki queries solve karte rahe.

Yeh poora system is tarah banaya gaya hai ke agar ek agent kisi khaas masle mein phas jaye, to woh aapko turant expert ke paas raaste pe le jaye aur sab details wahan pehle se pahunchaa de.

**Maksad:** Jab bahut saare agents ek saath kaam karein, to clear roles aur saf (clean) conversation maintain honi chahiye.  
Handoffs se hum sure hote hain ke har agent ko sirf apni zaroori baat dikhai de aur user ko achchi madad mile.
