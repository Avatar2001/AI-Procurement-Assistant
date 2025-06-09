# 🛒 AI Procurement Assistant

An intelligent multi-agent AI system built with **CrewAI** to automate and streamline product procurement research from ecommerce platforms. This assistant scrapes product data, generates tailored search queries, evaluates results, and produces a polished, Bootstrap-based procurement report in HTML.

---

## 📖 Project Overview

**AI Procurement Assistant** is designed to help procurement teams or companies identify the best products and deals from multiple ecommerce websites. By combining web scraping, search automation, and report generation — powered by language models and agent collaboration — the assistant ensures a fast, reliable, and professional procurement workflow.

---

## 🚀 Features

✅ Generate smart, product-specific search queries
✅ Automatically search ecommerce platforms for product listings
✅ Scrape product details including prices, images, and specifications
✅ Evaluate and rank products based on configurable criteria
✅ Generate a comprehensive, Bootstrap-styled HTML procurement report
✅ Verify and annotate the final report for structure and quality

---

## 🛠️ Tech Stack

* **Python**
* **CrewAI** (Multi-agent orchestration)
* **Gemini 2.0 Flash** (Google LLM)
* **Tavily API** (Search engine tool)
* **ScrapeGraph API** (Smart web scraping)
* **Bootstrap** (for HTML report styling)
* **Pydantic** (for data validation)

---

## 📝 System Architecture

**Agents:**

* 📖 `Search Queries Agent`: Generates strategic, ecommerce-focused search queries.
* 🔍 `Search Engine Agent`: Fetches ecommerce product pages for those queries.
* 🛒 `Web Scraping Agent`: Scrapes product data like pricing, specifications, and images.
* 📝 `Report Author Agent`: Compiles an HTML procurement report.
* ✅ `Report Verifier Agent`: Verifies the report’s structure, Bootstrap compliance, and logical accuracy.

**Tasks:**
Each agent has a dedicated task handling input, processing, and output validations.

**Knowledge Context:**
Incorporates company-specific context (like strategy or target markets) to tailor queries and recommendations.

---

## 📂 Project Structure

```
├── agents/
│   └── (Agent definitions)
├── context/
│   └── company_context.py
├── schemas/
│   └── (Pydantic schemas)
├── tasks/
│   └── (Task definitions)
├── tools/
│   └── (Custom scraping and search tools)
├── utils/
│   └── llm_config.py
├── ai_agent_output/
│   └── (Generated reports and data)
└── main.py
```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Avatar2001/AI-Procurement-Assistant.git
   cd AI-Procurement-Assistant
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables:**

   Create a `.env` file with:

   ```
   GOOGLE_API_KEY=your_google_api_key
   TAVILY_API_KEY=your_tavily_api_key
   SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key
   ```

4. **Run the system:**

   ```bash
   python main.py
   ```

---

## 📊 Example Use Case

Procure a **coffee machine** for the office targeting ecommerce stores in **Egypt**, using **Arabic** keywords and collecting the **top 10 recommended products**.

**Input parameters:**

```python
{
  "product_name": "coffe machine for the office",
  "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
  "country_name": "Egypt",
  "no_keywords": 10,
  "language": "Arabic",
  "score_threeshold": 0.10,
  "top_recommendations_no": 10
}
```

---

## 📄 Output

* **search\_queries.json**: Suggested ecommerce search queries
* **search\_results.json**: Product links with confidence scores
* **extracted\_details.json**: Detailed product info from scraped pages
* **procurement\_report.html**: Clean, Bootstrap-based HTML report
* **verified\_procurement\_report.html**: Verified, annotated final report


