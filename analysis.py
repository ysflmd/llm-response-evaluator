from pathlib import Path
import pandas as pd

results_path = Path("results.csv")

if not results_path.exists():
    fallback = Path("sample_results.csv")
    if fallback.exists():
        print("results.csv not found — analyzing sample_results.csv instead.\n")
        results_path = fallback
    else:
        raise FileNotFoundError(
            "No results file found. Run evaluator.py first or add sample_results.csv."
        )

df = pd.read_csv(results_path)

score_columns = [
    "relevance_score",
    "completeness_score",
    "consistency_score",
    "instruction_following_score",
]

print("Average scores")
print("=" * 40)

averages = df[score_columns].mean()

for metric, score in averages.items():
    label = metric.replace("_score", "").replace("_", " ").title()
    print(f"{label}: {score:.2f}/5")

df["overall_score"] = df[score_columns].mean(axis=1)

print("\nLowest-scoring prompts")
print("=" * 40)

lowest = df.nsmallest(3, "overall_score")[["id", "prompt", "overall_score"]]

for _, row in lowest.iterrows():
    print(f'#{row["id"]} — {row["overall_score"]:.2f}/5')
    print(row["prompt"])
    print()
