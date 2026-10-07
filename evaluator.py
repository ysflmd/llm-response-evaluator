import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. Copy .env.example to .env and add your API key."
    )

client = OpenAI(api_key=api_key)

prompts = pd.read_csv("prompts.csv")
results = []

print(f"Loaded {len(prompts)} prompts.\n")

for _, row in prompts.iterrows():
    prompt_id = row["id"]
    prompt = row["prompt"]

    print(f"Prompt {prompt_id}: {prompt}")

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt,
    )

    answer = response.output_text
    print("\nModel response:")
    print(answer)

    print("\nScore the response from 1 to 5.")
    relevance = int(input("Relevance: "))
    completeness = int(input("Completeness: "))
    consistency = int(input("Consistency: "))
    instruction_following = int(input("Instruction-following: "))

    results.append(
        {
            "id": prompt_id,
            "prompt": prompt,
            "response": answer,
            "relevance_score": relevance,
            "completeness_score": completeness,
            "consistency_score": consistency,
            "instruction_following_score": instruction_following,
        }
    )

    print("-" * 60)

results_df = pd.DataFrame(results)
results_df.to_csv("results.csv", index=False)

print("\nEvaluation complete.")
print("Results saved to results.csv")
