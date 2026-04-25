import pandas as pd
import os
import random


master = pd.read_csv("data/ai_job_market.csv")

# incoming file path
incoming_path = "data/jobs_incoming.csv"

# check if file exists
if os.path.exists(incoming_path) and os.path.getsize(incoming_path) > 0:
    incoming = pd.read_csv(incoming_path)
else:
    incoming = pd.DataFrame(columns=master.columns)

current_size = len(incoming)

batch_size = random.choice([10, 35, 80, 134, 55, 180])

end_index = min(current_size + batch_size, len(master))
next_batch = master.iloc[current_size:end_index]

if next_batch.empty:
    print("no more data left")
else:
    updated = pd.concat([incoming, next_batch], ignore_index=True)

    # save back to data folder
    updated.to_csv(incoming_path, index=False)

    print(f"added {len(next_batch)} new rows. now total rows are {len(updated)}")
