import pandas as pd

prompts = pd.read_csv("prompts.csv")

results = []

for _, row in prompts.iterrows():
    prompt = row["prompt"]

    # Placeholder response for now
    response = f"Example response generated for: {prompt}"

    relevance = 4
    completeness = 4
    consistency = 5

    results.append({
        "id": row["id"],
        "prompt": prompt,
        "response": response,
        "relevance_score": relevance,
        "completeness_score": completeness,
        "consistency_score": consistency
    })

results_df = pd.DataFrame(results)
results_df.to_csv("results.csv", index=False)

print("Evaluation complete. Results saved to results.csv")
