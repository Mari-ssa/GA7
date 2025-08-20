"""
Quarterly MRR Growth analysis
Author contact: 24f3003609@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("data.csv")
    target = 15.0
    avg = round(df["MRR_Growth"].mean(), 2)
    print("Quarterly data:\n", df.to_string(index=False))
    print(f"Average MRR Growth: {avg}")
    print(f"Industry Target: {target}")
    # Plot 1
    plt.figure()
    plt.plot(df["Quarter"], df["MRR_Growth"], marker="o")
    plt.title("MRR Growth Trend (2024)")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth")
    plt.savefig("assets/mrr_trend.png", bbox_inches="tight")
    plt.close()
    # Plot 2
    plt.figure()
    plt.bar(df["Quarter"], df["MRR_Growth"])
    plt.axhline(target)
    plt.title("MRR Growth vs Industry Target (15)")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth")
    plt.savefig("assets/mrr_vs_target.png", bbox_inches="tight")
    plt.close()

    # Simple findings
    best_q = df.loc[df["MRR_Growth"].idxmax(), "Quarter"]
    print(f"Best quarter by growth: {best_q}")
    underperforming = df[df["MRR_Growth"] < target]["Quarter"].tolist()
    print("Quarters below target:", underperforming)

if __name__ == "__main__":
    main()
