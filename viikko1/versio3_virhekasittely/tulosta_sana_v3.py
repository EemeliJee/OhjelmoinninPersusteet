def main():
  file = "sana.txt"

    try:
      with open(file, "r", encoding="utf-8) as f:
                sana = f.read().strip()

     if not sana:
         print("Error: file is empty.")
         return

      print(sana)

except FileNotFoundError:
    print(f"Error: file '{file}' not found.")
except PermissionError:
    print(f"Error: unsufficient permission to read file '{file}'.")
except Exception as e:
    print(f"Unknown error: {e}")


if __name__ == "__main__":
  main()
