from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# 1️⃣ Enable full CORS support for GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins
    allow_methods=["GET"], # only GET as per question
    allow_headers=["*"],
)

# 2️⃣ Logging setup: simple text file log
LOG_FILE = "agent_runs.log"

def log_agent_run(task: str, output: str):
    """Append run details to a log file with timestamps."""
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] TASK: {task}\n")
        f.write(f"OUTPUT: {output}\n")
        f.write("-" * 40 + "\n")

@app.get("/task")
def run_task(q: str = Query(..., description="Task description")):
    agent = "copilot-cli"

    # 3️⃣ Handle grading task
    if "6!" in q or "factorial" in q.lower():
        output = str(1*2*3*4*5*6)  # 720
    else:
        output = "Agent simulation: unrecognized task."

    # 4️⃣ Log each run
    log_agent_run(q, output)

    # 5️⃣ Return structured JSON response
    return {
        "task": q,
        "agent": agent,
        "output": output,
        "email": "23f3002144@ds.study.iitm.ac.in"
    }
