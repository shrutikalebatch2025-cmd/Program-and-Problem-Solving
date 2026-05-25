# Type Content here...
import sys

def solve():
    # Read total number of operations
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    phone_book = {}

    for _ in range(n):
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        
        command = parts[0]

        if command == "ADD":
            name = parts[1]
            phone = parts[2]
            phone_book[name] = phone

        elif command == "REMOVE":
            name = parts[1]
            if name in phone_book:
                del phone_book[name]

        elif command == "DISPLAY":
            if not phone_book:
                print("No contacts")
            else:
                # Sort by name (keys) alphabetically
                for name in sorted(phone_book.keys()):
                    print(f"{name}: {phone_book[name]}")

if __name__ == "__main__":
    solve()
