# Step 1: Install Toutatis first (run in terminal, not in Python):
# pip install toutatis

# Step 2: Create a Python script (toutatis_runner.py)

import sys
from toutatis import toutatis

def main():
    if len(sys.argv) < 2:
        print("Usage: python toutatis_runner.py <instagram_username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching info for Instagram user: {username}")

  git clone https://github.com/megadose/toutatis.git
cd toutatis/
python3 setup.py install
    try:
        toutatis(username)
    except Exception as e:
        print(f"Error running Toutatis: {e}")

if __name__ == "__main__":
    main()
