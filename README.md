# Hybrid Smart-Routing Multi-Agent Coding Engine

An advanced, autonomous multi-agent software engineering pipeline built using Python. This system features a conditional Actor-Critic workflow that dynamically writes, reviews, self-corrects, and documents code execution streams.

## 🌟 Key Architecture Features
* **Smart-Routing Hybrid Execution:** Automatically detects network status. Routes to high-performance **Groq Cloud API** (`Llama 3.3 70B`) when online, and gracefully falls back to a localized on-premise **Ollama Server** (`Llama 3`) when offline.
* **Multi-Agent Actor-Critic Workflow:** * `Agent 1 (Developer)` compiles the initial functional matrices.
  * `Agent 2 (Reviewer)` runs structural parsing to detect logical syntax bugs.
  * `Agent 1` programmatically refactors code baseline parameters based on logs.
  * `Agent 3 (Technical Writer)` generates clean markdown documentation profiles.
* **Isolated Environment State Savings:** Dynamically generates independent structural project directories for every user prompt to prevent file clashing.

---

## 🚀 How to Run the Project (For Users & Recruiters)

This entire application runs directly inside your **Command Line Interface (CLI)**. Follow these steps to execute the pipeline on your machine:

### 1. Prerequisites & Dependencies
Clone this repository to your desktop, open your terminal inside the project directory, and run the following command to automatically install all required library dependencies at once:

```bash
pip install -r requirements.txt