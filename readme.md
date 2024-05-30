# Multi AI agent system for financial analysis with crewAI

This financial analysis example uses OpenAI's ChatGPT 4 model and SEC-API to create a report about any publically traded company with USA Securities and Exchange Commission (SEC) filings. SEC filings are regulatory documents that companies and issuers of securities must submit on a regular basis.

Please note that this example is for demonstration purposes only. You should not construe any such information or other material as legal, tax, investment, financial, or other advice.

crewAI provides an open source framework for orchestrating role-playing autonomous AI agents. It empowers agents to work together seamlessly while tackling complex tasks.

Each AI agent plays a different role, such as a Financial Researcher, or a Financial Analyst. Each agent can be given multiple tools, such as the ability to collect and process data from the web, or through API's. crewAI can use self-made tools, or use already existing LangChain tools from the LangChain library.

Agents can work in teams (crews), where they cooperate and interact with each other in a sequential workflow (where the output of the first agent serves as the input for the second agent, as in this example), or in a hierarchical organisation (where agents get coordinated and instructed by a "manager").

The key components of crewAI are:

| Components | What they do                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Crew       | A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. A crew defines the strategy for task execution, agent collaboration, and the overall workflow.                                                                                                                                                                                                                                                                                                                                        |
| Agents     | Agents are the building blocks of a crew. Each agent has a role, goal, and backstory. This context helps guide the agent's decisions and responses.                                                                                                                                                                                                                                                                                                                                                                                           |
| Tools      | Agents can be augmented with custom tools that enhance their capabilities. These tools can be anything from information retrieval modules to data analysis scripts. The agents in this example use the SEC-API tools from the crewAI examples library. These tools download SEC filing reports and then process the reports with Meta's (Facebook's) "FAISS" (Facebook AI Similarity Search) vector store for similarity (semantic) search. They use Central Processing Unit (CPU) only and do not require any Graphic Processing Unit (GPU). |
| Tasks      | A crew needs to accomplish tasks. Each task can be assigned to one or more specific agent(s) based on their expertise.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Processes  | Complex tasks can be broken down into smaller, more manageable processes. They orchestrate the flow of information between agents. This example follows a sequential process.                                                                                                                                                                                                                                                                                                                                                                 |

This example allows you to set the company stock symbol of the company that you want to analyse in the `main.py` script. It is currently set to `MSFT`, which is the company stock symbol for Microsoft Corp.

You need an OpenAI API key for this example. [Get your OpenAI API key here](https://platform.openai.com/login). You can insert your OpenAI API key in the `main.py` script, or you can supply your OpenAI API key either via the `.env` file, or through an environment variable called `OPENAI_API_KEY`. If you don't want to use an OpenAI model, then you can also use other models, including local models.

You also need a free SEC-API key for this example to download the SEC filings. [Get your free SEC-API key here](https://sec-api.io/login). You can insert your SEC-API key in the `main.py` script, or you can supply your SEC-API key either via the `.env` file, or through an environment variable called `SEC_API_API_KEY`.

| >>>>> The final answer will look similar to this example: <<<<< |
| --------------------------------------------------------------- |

**Microsoft Corporation Financial Analysis Report**

**1. Profitability Ratios:**

- **Gross Margin:** 69.0% (146,052 / 211,915)
- **Operating Margin:** 41.8% (88,523 / 211,915)
- **Net Profit Margin:** 34.1% (72,361 / 211,915)
- **Return on Assets (ROA):** 8.3% (72,361 / 871,200) _based on total assets from previous statements_
- **Return on Equity (ROE):** 29.1% (72,361 / 248,570) _based on total equity from previous statements_

**2. Liquidity Ratios:**

- **Current Ratio:** 2.5 (184,406 / 73,206) _based on current assets and current liabilities from previous statements_
- **Quick Ratio:** 1.9 (184,406 - 5,521 / 73,206) _adjusting current assets by inventory_

**3. Solvency Ratios:**

- **Debt to Equity:** 0.46 (114,130 / 248,570) _based on total debt and total equity from previous statements_
- **Interest Coverage Ratio:** 28.4 (88,523 / 3,115) _operating income divided by interest expense from previous statements_

**4. Efficiency Ratios:**

- **Asset Turnover:** 0.24 (211,915 / 871,200) _based on total revenue and total assets from previous statements_
- **Inventory Turnover:** 38.4 (211,915 / 5,521) _based on total revenue and inventory from previous statements_

**5. Growth Metrics:**

- **Revenue Growth Year-Over-Year:** 7% (211,915 / 198,270)
- **Net Income Growth Year-Over-Year:** -0.5% (72,361 / 72,738)

**6. Valuation Metrics:**

- **Price/Earnings (P/E) Ratio:** 33.5 _based on current market price of $324 and EPS of 9.68_
- **Price/Book (P/B) Ratio:** 13.0 _based on current market price of $324 and book value per share from previous statements_

**7. Cash Flow Metrics:**

- **Operating Cash Flow:** 76,000 million _approximated from cash flow statements_
- **Free Cash Flow:** 55,500 million (76,000 - 20,500) _operating cash flow minus capital expenditures from previous statements_

**Summary:**
Microsoft's financial performance shows strong profitability with a robust net profit margin of over 34%. The company maintains a healthy liquidity position, evidenced by a current ratio of 2.5. Solvency ratios indicate a stable financial structure with moderate leverage. Efficiency ratios reveal a modest asset turnover, typical for large tech companies heavily invested in R&D and fixed assets. Growth in revenue is solid at 7%, although net income slightly declined due to increased operational costs. The valuation metrics suggest a premium market valuation, reflecting strong market confidence in Microsoft's future earnings capacity. Cash flows remain strong, providing ample room for reinvestment and shareholder returns.
