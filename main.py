"""Write one funny out-of-office email reply to /output/entry.txt."""

import os

ENTRY = "I'm out of the office until Monday - my inbox is unsupervised, and frankly, so am I."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
