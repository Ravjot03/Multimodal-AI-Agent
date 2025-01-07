# Multimodal AI Agent for Web Search and Stock Analysis

This project demonstrates a multimodal AI agent setup that integrates different AI models and tools for web searching and stock analysis. The AI agents use the Groq model (powered by Llama-3.3-70b) to gather and analyze information from web search engines (DuckDuckGo) and financial data sources (Yahoo Finance) in a highly collaborative manner.

---

## Abstract

This report presents the development of a multimodal AI agent leveraging large language models (LLMs) and external domain-specific tools to provide real-time web search and financial analysis. The agent integrates LLaMA-3.3-70b, DuckDuckGo for web search, and YFinanceTools for financial data retrieval, enabling automated stock tracking, company news summarization, and analyst recommendations. The designed system is capable of delivering structured and source-backed outputs using markdown. This work explores the potential of multimodal AI agents in applications requiring data synthesis from heterogeneous sources, highlighting their relevance in decision support systems.

---
## Introduction

With the rapid evolution of large language models (LLMs), there has been a growing interest in developing AI systems that can interact with multiple data sources and tools. These multimodal AI agents aim to bridge the gap between natural language understanding and real-world data retrieval by enabling contextual information synthesis from diverse domains.

This project focuses on building a multimodal AI agent capable of:

- Performing real-time web searches to retrieve relevant information.

- Providing financial insights, including stock prices, company fundamentals, and analyst recommendations.

- Delivering structured outputs using markdown for enhanced readability.

By combining the power of LLaMA-3.3-70b with domain-specific tools, the agent showcases the potential of multimodal AI in real-world applications such as financial analysis and automated research.

---
## Methodology

### System Architecture

The system is composed of three primary components:

- Web Search Agent: Utilizes DuckDuckGo to retrieve information from the web.

- Financial Analysis Agent: Uses YFinanceTools to gather financial data, including stock prices, company news, and recommendations.

- Multimodal Agent: A central agent coordinating the web search and financial analysis agents, ensuring a unified and structured output.

### Tools and Technologies

- LLM: LLaMA-3.3-70b, a large language model known for its versatility in natural language understanding.

- DuckDuckGo API: Used for real-time web searches.

- YFinanceTools: Provides financial data, including stock prices, fundamentals, and news.

- Groq Model API: Facilitates interaction with the LLaMA model.

### Implementation

The system was implemented using the Python-based PHI framework. Each agent was instantiated with specific tools and instructions tailored to its task.

Full code is available here - [Code](https://github.com/Ravjot03/Multimodal-AI-Agent/blob/main/financial_agent-github.py)

---
## Results

The multimodal AI agent was tested by querying for real-time financial information and relevant web search data. Below are sample outputs for a query regarding Tesla stock:

![image](https://github.com/user-attachments/assets/6b8d6211-1d0c-4f3e-9846-25c83d3210c1)


The output demonstrates the agent’s capability to retrieve and present structured information, including tables for financial data and bullet points for news summaries, ensuring clarity and ease of interpretation.

---
## Discussion

This project highlights the feasibility and utility of integrating large language models with external tools to create multimodal agents. Key takeaways include:

- Versatility: The agent can handle diverse tasks, from web search to financial analysis, without requiring retraining.

- Scalability: Additional tools can be integrated to extend the agent’s capabilities to other domains, such as healthcare or legal research.

- Limitations: The accuracy of outputs depends on the reliability of the external tools and the underlying LLM. Furthermore, real-time performance may vary based on network latency and API response times.

---
## Applications

The developed multimodal AI agent has several potential applications, including:

- Financial Technology (FinTech): Automated analysis of market data for investors and financial analysts.

- Research Assistance: Rapid information retrieval from the web for academic and industrial research.

- Business Intelligence: Providing real-time insights for decision-making in various industries.

---
## Future Work

Future improvements to the multimodal AI agent could include:

- Enhanced Tool Integration: Incorporating more specialized tools for different domains.

- Improved Natural Language Understanding: Upgrading to newer and more advanced LLMs as they become available.

- Personalization: Allowing users to customize the agent’s behavior based on specific needs or preferences.

---
## Conclusion

This report details the design and implementation of a multimodal AI agent capable of real-time web search and financial analysis. By leveraging LLaMA-3.3-70b and domain-specific tools, the agent demonstrates how multimodal AI can enhance decision-making processes across various fields. With further development, such agents could become invaluable tools for professionals in data-driven industries.

---
## References

1. OpenAI. (2024). "LLaMA: A Large Language Model for Versatile Applications."

2. DuckDuckGo API Documentation. (2024).

3. YFinance Tools Documentation. (2024).

4. PHI Framework User Guide. (2024).
