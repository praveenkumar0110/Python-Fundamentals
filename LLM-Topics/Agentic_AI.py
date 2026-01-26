'''
| Normal LLM         | Agentic AI                |
| ------------------ | ------------------------- |
| Question ku answer | Goal ku work pannum       |
| Single response    | Multiple steps yosikkum   |
| Tools illa         | Tools use pannum          |
| Planning illa      | Plan panni execute pannum |

'''

#Agentic AI Architecture

'''
User Goal
   ↓
LLM (Brain)
   ↓
Planner (steps decide pannum)
   ↓
Tool Selector
   ↓
Tools (DB, API, Files, etc.)
   ↓
Memory (store context)
   ↓
LLM
   ↓
Final Result
'''

# Parts explanation

# 1️⃣ LLM (Brain)

# Reason pannum, next step decide pannum.

# 2️⃣ Planner

# Task ah small steps ah break pannum.

# 3️⃣ Tool Selector

# Yentha tool use panna nu decide pannum.

# 4️⃣ Tools

# MySQL, Email, Files, APIs.

# 5️⃣ Memory

# Previous steps / data remember pannum.