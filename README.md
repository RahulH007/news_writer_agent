# News Writer Agent

![crewAI Logo](https://raw.githubusercontent.com/RahulH007/news_writer_agent/main/assets/crewai-brand-color.svg)

The **News Writer Agent** is an AI-powered system designed to automate the process of researching, summarizing, and generating professional news articles. Built on the [crewAI](https://crewai.com) framework, it streamlines workflows and delivers polished markdown articles effortlessly.

---

## Features

- **Automated Research**: Gather the latest and most relevant information.
- **Web Scraping**: Extract insights from multiple websites.
- **Content Summarization**: Generate concise summaries.
- **Markdown Output**: Produce professional articles ready for publication.

---

## Installation

1. Ensure **Python >=3.10 <3.14** is installed.
2. Install [UV](https://docs.astral.sh/uv/):
   ```bash
   pip install uv
   ```
3. Install dependencies:
   ```bash
   crewai install
   ```

---

## Usage

Run the following command to start the agent:

```bash
crewai run
```

This generates a `news_article.md` file with the output.

---

## Customization

- Configure agents in `src/ai_news/config/agents.yaml`.
- Define tasks in `src/ai_news/config/tasks.yaml`.
- Add custom logic in `src/ai_news/crew.py`.
- Set your `OPENAI_API_KEY` in the `.env` file.

---

## Feedback

Feel free to contribute or share feedback:

- **GitHub Issues**: Report bugs or request features.

---

Let’s redefine news creation with AI!
