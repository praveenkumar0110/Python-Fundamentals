import os
import requests
from transformers import AutoTokenizer

print("=== HuggingFace Network Fix Script Started ===")

# STEP 1 — Add environment variables to bypass SSL/proxy issues
print("\nSetting environment variables...")

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["REQUESTS_CA_BUNDLE"] = ""

print("Environment variables set.")


# STEP 2 — Test Internet Access to HuggingFace
print("\nTesting connection to huggingface.co ...")

try:
    r = requests.get("https://huggingface.co", timeout=10)
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        print("Internet OK: HuggingFace reachable ✔️")
    else:
        print("Internet Blocked ❌ — Your network is blocking HuggingFace.")
except Exception as e:
    print("Error checking HuggingFace connection:", e)


# STEP 3 — Test HuggingFace Model Download
print("\nTesting model download (bert-base-uncased)...")

try:
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    print("Model Download Successful ✔️")
except Exception as e:
    print("\n❌ Model Download FAILED")
    print("Error Details:")
    print(e)

print("\n=== Script Finished ===")
