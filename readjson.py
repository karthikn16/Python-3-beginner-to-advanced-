import json

def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("❌ JSON file not found.")
    except json.JSONDecodeError:
        print("❌ Invalid JSON format.")
    except Exception as e:
        print("❌ Error:", e)

def main():
    print("📄 JSON File Reader App")
    print("-----------------------")

    file_path = input("Enter JSON file name (example: data.json): ")

    data = read_json_file(file_path)

    if data:
        print("\n✅ JSON File Contents:\n")
        print(data)

if __name__ == "__main__":
    main()