# 🤖 Autonomous Hybrid Smart-Routing Multi-Agent Coding Engine

An advanced, enterprise-grade multi-agent software engineering factory built natively in Python. This framework features an autonomous, conditional Actor-Critic state machine workflow that dynamically generates, critically reviews, programmatically self-corrects, and compiles professional documentation profiles for custom software assets.

---

## 🗺️ System Architecture Blueprints

### 1. The Gateway Sniffer & Network Switch (Network Topology)

Before initiating language inference, the system executes a conditional network handshake. It samples the latency and availability of the public DNS backbone to choose the optimal computational execution path, enabling seamless orchestration across cloud or local systems:

```text
               [ USER TRIGGERS PIPELINE ]
                           │
                           ▼
            [ Ping Request to 8.8.8.8:53 ]
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
     [ Ping SUCCESS ]              [ Ping TIMEOUT / FAIL ]
      Status: ONLINE                Status: OFFLINE
            │                             │
            ▼                             ▼
  Load Environment Memory        Initialize Local Kernel
   (Secret Key Secrets Vault)   (cpu_avx2 Vector Flags)
            │                             │
            ▼                             ▼
   [ Groq Cloud Stream ]         [ Local Ollama Engine ]
 Model: Llama-3.3-70b-Versatile    Model: Llama3 (On-Prem)

```

### 2. The Multi-Agent Critic Loop (State Machine Graph)

Once the execution stream path is locked, the prompt transitions into an isolated collaborative pipeline where individual AI agents evaluate, test, and criticize each other's deliverables to eliminate syntax regressions before deployment:

```text
       ┌─────────────────────────────────────────┐
       ▼                                         │
[ Agent 1: Developer ] ──► (Initial Draft)       │
                                │                │
                                ▼                │
                       [ Agent 2: Reviewer ]     │ (Bug Report Log
                                │                │  Passed Back)
                                ▼                │
                     { Is Code Flawless? }       │
                                │                │
            ┌───────────────────┴────────────────┤
            ▼ (YES)                              ▼ (NO)
     [ Reply: 'PERFECT' ]                 [ Flag Anomalies ]
            │                                    │
            ▼                                    ▼
    Freeze Source Code                   Trigger Refactoring Pass
            │                                    │
            └───────────────────┬────────────────┘
                                │
                                ▼
                       [ Agent 3: Writer ] ──► [ Generate README ]

```

---

## 📊 Comprehensive Component Matrix

| System Component        | Execution Layer          | Dependency        | Structural Responsibility                                                                                     |
| ----------------------- | ------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------- |
| **System Gateway**      | Network Kernel           | `socket`          | Pings standard communication ports to calculate network state. Safely branches logic paths dynamically.       |
| **Security Vault**      | Local Memory             | `python-dotenv`   | Intercepts system initialization to safely inject cloud authorization keys without exposing them in codebase. |
| **Agent 1 (Developer)** | Generative Inference     | `groq` / `ollama` | Translates human-language requirements into isolated, clean, executable python code syntax blocks.            |
| **Agent 2 (Reviewer)**  | Static Analysis / Critic | `groq` / `ollama` | Scans logic arrays for bugs, exceptions, or optimization faults, issuing structural correction logs.          |
| **Agent 3 (Writer)**    | Documentation            | `groq` / `ollama` | Captures final verified code outputs and transforms them into standard technical markdown profiles.           |

---

## 🧠 Core Engineering Principles Under the Hood

### 🔬 Multi-Agent System Synergy (Actor-Critic Framework)

Single-prompt language model generation is highly prone to structural calculations failures or syntax hallucinations. This framework mitigates compilation flaws by implementing a programmatic **Actor-Critic Model**.

The **Actor (`Agent 1`)** is trained for logical construction and feature implementation, while the **Critic (`Agent 2`)** operates in an adversarial capacity, checking constraints, edge-case input handling, and potential runtime crashes. By decoupling these tasks, the engine forces automated verification loops before any code file touches production.

### 🔌 Intelligent Network Fallback Mechanics

Adhering to the distributed computing principle of **graceful degradation**, the pipeline avoids fatal connection drops. If internet availability collapses, the runtime context dynamically recalibrates: dropping cloud dependencies, enabling local hardware kernel vector processing (`cpu_avx2`), and executing local on-premise inference servers through Ollama. When online, it offloads all workloads to specialized remote GPU clusters, scaling local resource utilization down to near 0%.

---

## 🚀 Interface Options & Local Execution Guide

This platform supports dual execution entry points depending on user workflow preferences: a **Premium Full-Stack Web App Workbench UI** (`app.py`) and a **Native Offline Terminal Console Tool** (`run.py`).

### 1. Installation of Application Packages

Clone this workspace down to your local directory, open a command terminal inside the root path, and batch-install all required package matrices at once:

```bash
pip install -r requirements.txt

```

### 2. Configure Environment Cryptography

To enable high-speed cloud clusters, create a hidden file named `.env` in your root workspace folder and configure your private API token:

```text
GROQ_API_KEY=gsk_your_actual_private_cloud_key_here

```

_(Note: The repository contains strict `.gitignore` configurations that intercept Git staging to block this file from ever leaking online)._

### 3. Option A: Boot the Full-Stack Web App UI (`app.py`)

This option launches a modern browser-based studio featuring sidebar control metrics, interactive component tracking, live compilation progress sliders, layout output tabs, and physical asset download handlers.

```bash
streamlit run app.py

```

```
[ App UI Pipeline Layout Mapping ]
┌────────────────────────────────────────────────────────┐
│  Sidebar: System Specs & Token Security Vault Status   │
├────────────────────────────────────────────────────────┤
│  [📋 Requirements Input] -> [🚀 Boot Assembly Button]  │
├────────────────────────────────────────────────────────┤
│  Tabs: 💻 Source Code  │  📄 Markdown  │  📊 Logs      │
└────────────────────────────────────────────────────────┘

```

### 4. Option B: Boot the Native Terminal Tool (`run.py`)

This option handles pure, raw terminal command execution loops, automatically mapping and generating code folders cleanly segregated within your workspace directories.

```bash
python run.py

```
