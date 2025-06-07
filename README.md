# AI-Procurement-Assistant
Awesome — let’s draft you a clean, clear, and engaging `README.md` for your AI Procurement Assistant project based on your repo and what you shared. Here’s a solid version you can drop right into your repo:

---

# 🛒 AI Procurement Assistant

A smart, multi-agent AI system designed to automate procurement research, price comparison, and report generation for businesses — saving time and optimizing purchasing decisions.

---

## 📖 Overview

**AI Procurement Assistant** is a Python-based AI multi-agent application powered by [CrewAI](https://github.com/joaomdmoura/crewAI) and state-of-the-art LLMs like Google's Gemini models via API.

This system automatically:

* Suggests relevant product search queries.
* Searches the web for product offers.
* Scrapes e-commerce websites for product details.
* Generates a professional procurement report (in HTML with Bootstrap styling).
* Verifies the report for completeness, accuracy, and UI best practices.

It’s a complete end-to-end tool tailored for data-driven procurement.

---

## 🚀 How It Works

The application is composed of multiple AI agents, each assigned a specialized role:

| Agent                                   | Responsibility                                                         |
| :-------------------------------------- | :--------------------------------------------------------------------- |
| **Search Queries Recommendation Agent** | Suggests varied, product-specific search queries.                      |
| **Search Engine Agent**                 | Searches the web using Tavily API and collects relevant product links. |
| **Web Scraping Agent**                  | Scrapes product details from the given URLs using ScrapeGraph.         |
| **Procurement Report Author Agent**     | Generates a clean, structured HTML report with Bootstrap.              |
| **Report Verifier Agent**               | Verifies report quality, structure, and completeness.                  |

---

## 📝 Features

✅ AI-driven query generation
✅ Web search and scraping integration
✅ Automated procurement reporting in HTML
✅ Bootstrap-styled responsive design
✅ Report quality verification
✅ Environment-variable based API key management

---

## 🛠️ Tech Stack

* Python 3.11+
* CrewAI
* Tavily API
* ScrapeGraph
* Google Gemini (via API)
* LangChain
* Bootstrap (for HTML reports)
* Pydantic (for data modeling)
* AgentOps (agent monitoring)

---

## 📦 Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/Avatar2001/AI-Procurement-Assistant.git
cd AI-Procurement-Assistant
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Set up your `.env` file with the following keys:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
AGENTOPS_API_KEY=your_agentops_api_key
TAVILY_API_KEY=your_tavily_api_key
SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key
```

---

## ▶️ How to Run

Run the main script to start a procurement job:

```bash
python crewaicolab.py
```

You can customize the product name, websites list, country, language, and thresholds directly within the `run_procurement_crew()` function call.

---

## 📊 Example Output

* `search_queries.json` – Suggested search queries
* `search_results.json` – Collected product search results
* `extracted_details.json` – Scraped product data
* `proccurement_report.html` – Professional procurement report
* `verified_proccurement_report.html` – Verified report with inline comments

---

## 📬 Contact

For any questions, ideas, or collaboration inquiries:

**Mohamed Sherif**
📧 [mohamedsherif21k@gmail.com](mailto:mohamedsherif21k@gmail.com)


