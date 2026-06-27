import math
import string


def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 1)


def estimate_crack_time(entropy):
    if entropy < 28:
        return "Few Seconds"
    elif entropy < 40:
        return "Few Hours"
    elif entropy < 50:
        return "4 years"
    elif entropy < 70:
        return "500 years"
    else:
        return "Millions of years"


def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Add more characters")

    if any(c.islower() for c in password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 20
    else:
        suggestions.append("Add numbers")

    if any(c in string.punctuation for c in password):
        score += 20
    else:
        suggestions.append("Use unique symbols")

    if score <= 40:
        strength = "🔴 Weak"
    elif score <= 80:
        strength = "🟡 Medium"
    else:
        strength = "🟢 Strong"

    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    return score, strength, entropy, crack_time, suggestions