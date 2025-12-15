import secrets
import string


def generate_otp(length=6):
    digits = string.digits
    otp = ''.join(secrets.choice(digits) for _ in range(length))
    return otp


def main():
    print("🔐 Secure OTP Generator 🔐")

    try:
        length = int(input("Enter OTP length (default 6): ") or 6)
        otp = generate_otp(length)
        print(f"\nYour OTP is: {otp}")
    except ValueError:
        print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()
