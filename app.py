from password_utils import check_password

print("\n🔐 AI Password Strength Checker")

while True:
    password = input("\nPassword: ")

    score, strength, entropy, crack_time, suggestions = check_password(password)

    print(f"\n{strength}")

    bars = "█" * (score // 5)
    print(f"{bars} {score}%")

    print(f"\nEntropy Score : {entropy}")
    print(f"Estimated Crack Time : {crack_time}")

    print("\nSuggestions:")

    if suggestions:
        for s in suggestions:
            print(f"✓ {s}")
    else:
        print("✓ Excellent Password!")

    choice = input("\nCheck another password? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using AI Password Strength Checker 🔐")
        break