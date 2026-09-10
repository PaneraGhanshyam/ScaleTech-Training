import pandas as pd


INPUT_FILE = "iris.csv"
OUTPUT_FILE = "species_averages.csv"


# Load dataset
df = pd.read_csv(INPUT_FILE)


# Basic inspection
print("=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DATASET INFO ===")
df.info()

print("\n=== STATISTICS ===")
print(df.describe())


# Count species
print("\n=== SPECIES COUNT ===")
print(df["species"].value_counts())


# Filter
print("\n=== PETAL LENGTH > 5 ===")
print(
    df[df["petal_length"] > 5][
        ["species", "petal_length"]
    ]
)


# Sort
print("\n=== SORTED BY PETAL LENGTH ===")
print(
    df.sort_values(
        "petal_length",
        ascending=False
    ).head(10)
)


# Group and calculate averages
average_measurements = (
    df.groupby("species")[
        [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]
    ]
    .mean()
)

print("\n=== AVERAGE MEASUREMENTS ===")
print(average_measurements)


# Save results
average_measurements.to_csv(OUTPUT_FILE)

print(f"\nResults saved to {OUTPUT_FILE}")