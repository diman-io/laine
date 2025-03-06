import json
from collections import defaultdict

with open("all-stakes.json", "r", encoding="utf-8") as f:
    stakes = json.load(f)

stakes_by_val = defaultdict(int)

for stake in stakes:
    if "activeStake" in stake:
        stakes_by_val[stake["delegatedVoteAccountAddress"]] += stake["activeStake"]

for val, total_stake in stakes_by_val.items():
    print(f"{val},{total_stake}")
