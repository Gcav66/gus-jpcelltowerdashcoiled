import os
coiled_token = os.environ['COILED_TOKEN']
os.system(f"coiled login --account sales --token {coiled_token}")
