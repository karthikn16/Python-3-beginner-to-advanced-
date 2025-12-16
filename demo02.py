import secrets
import string

def generate_otp(length=6, otp_type="1"):
    if otp_type == "1":
        characters = string.digits
    elif otp_type == "2":
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid OTP type")

    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    print("🔐 Secure OTP Generator 🔐")
    print("1. Numeric OTP")
    print("2. Alphanumeric OTP")

    otp_type = input("Choose OTP type (1 or 2): ").strip()

    try:
        length = int(input("Enter OTP length (default 6): ") or 6)
        otp = generate_otp(length, otp_type)
        print("\n✅ Your Secure OTP is:", otp)
    except ValueError as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
