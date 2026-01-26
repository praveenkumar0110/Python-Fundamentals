'''
LangGraph basics
        - Nodes
        - Edges
        - State
'''

'''
Trip plan panna:

User: “Feb 10 ku Goa trip plan pannu”

LangGraph flow ippadi irukum:

1️⃣ Date edukkum
2️⃣ Place edukkum
3️⃣ Flights check pannum ✈️
4️⃣ Hotels check pannum 🏨 (parallel-ah nadakkum)

👉 Flights & Hotels same time la run aagum (parallel)

Condition varum

Flight illa na?

LangGraph enna pannum:

➡️ Backward poi
“Vera date try pannalama?” nu user kitta kekum
Illati next available flight thedum

Ithu normal chain la kashtam.
LangGraph la easy.

'''


'''
| LangChain                         | LangGraph                  |
| --------------------------------- | -------------------------- |
| Straight line flow (step by step) | Graph flow (any direction) |
| No memory / state                 | State maintain pannum      |
| Simple RAG, tools                 | Complex agents             |
| Parallel work kashtam             | Parallel work easy         |
| Loop / retry kashtam              | Loop / retry easy          |
| Basic chatbot / RAG               | Smart AI agent systems     |

'''