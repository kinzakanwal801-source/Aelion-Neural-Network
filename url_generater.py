# ============================================================
# Aelion URL Generator v1.0
# ============================================================
# Installation
#
# Install the AelionCalc library before running this script:
#
#     pip install aelion_calc
#
# Make sure the trained model file (new_model (3).aelion)
# is located in the same directory as this script.
# ============================================================

from aelion_calc import Aelion
import json
import os

def main():
    model_path = "new_model.aelion"
    generator = Aelion(model_path)

    print("=" * 45)
    print(" Aelion URL Generator v1.0")
    print("=" * 45)
    print("Enter a website name to generate its URL.")
    print("Type 'exit' or 'stop' to quit.\n")

    while True:
        website = input("Enter website: ").strip()

        if website.lower() in ["exit", "stop"]:
            print("\n Thank you for using Aelion URL Generator!")
            break

        if not website:
            continue

        print("\n Generated URL: ", end="", flush=True)

        for token in generator.chat_stream(
            website,
            max_tokens=30,
            temperature=0.01,
        ):
            print(token, end="", flush=True)

        print("\n")


if __name__ == "__main__":
    main()
