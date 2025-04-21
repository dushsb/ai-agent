import os
from dotenv import load_dotenv

load_dotenv()


def main():
    # Main function logic should be implemented here
    """
    Main entry point for the program.
    """
    print("Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}={value}")

if __name__ == "__main__":
    main()