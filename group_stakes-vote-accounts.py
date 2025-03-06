import json
from collections import defaultdict

with open("vote-accounts.json", "r", encoding="utf-8") as f:
    result = json.load(f)["result"]

stakes_by_val = defaultdict(int)

for nodes in [result["current"], result["delinquent"]]:
    for node in nodes:
        if "activatedStake" in node:
            stakes_by_val[node["votePubkey"]] += node["activatedStake"]

for val, total_stake in stakes_by_val.items():
    print(f"{val},{total_stake}")
