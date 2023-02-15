import os

if __name__ == "__main__":
    print(os.environ.get('INPUT_API_TOKEN', 'default'))