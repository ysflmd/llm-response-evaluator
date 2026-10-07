# LLM Response Evaluator

A small Python project for testing and analyzing large language model responses across a structured set of prompts.

## What it does

The project:
- loads prompts from a CSV file;
- sends each prompt to an LLM API;
- stores the generated response;
- lets the user assign simple evaluation scores for relevance, completeness, consistency, and instruction-following;
- saves the results to CSV;
- summarizes average scores and identifies weaker responses.

## Technologies

- Python
- Pandas
- OpenAI API
- CSV

## Project structure

```text
llm-response-evaluator/
├── README.md
├── evaluator.py
├── analysis.py
├── prompts.csv
├── sample_results.csv
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file from `.env.example` and add your API key:

```text
OPENAI_API_KEY=your_api_key_here
```

3. Run the evaluator:

```bash
python evaluator.py
```

4. Run the analysis:

```bash
python analysis.py
```

## Evaluation criteria

Each response is scored from 1 to 5 for:

- **Relevance** — how directly the response answers the prompt
- **Completeness** — whether the important parts of the request are covered
- **Consistency** — whether the answer is internally coherent
- **Instruction-following** — whether the model follows formatting or length constraints

## Notes

This is a small learning project focused on LLM evaluation rather than model training. The scoring is intentionally simple and manual so that evaluation decisions remain easy to inspect.

## Possible next steps

- compare multiple models;
- add automatic scoring;
- add hallucination/factuality checks;
- visualize evaluation results;
- create a larger benchmark dataset.
