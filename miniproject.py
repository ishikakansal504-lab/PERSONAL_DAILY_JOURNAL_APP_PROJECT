from datetime import datetime
FILENAME = "journal.txt"
def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    print("\nToday's Date:", date)
    entry = input("Write your journal entry: ")
    if entry.strip() == "":
        print("Entry cannot be empty!\n")
        return
    journal_data = [f"Date: {date}", f"Entry: {entry}", "-" * 40]
    with open(FILENAME, "a") as file:
        for line in journal_data:
            file.write(line + "\n")
    print("\nEntry added successfully!\n")
def view_entries():
    try:
        with open(FILENAME, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("\nNo entries found yet.\n")
            else:
                print("\n===== All Journal Entries =====\n")
                print(content)
    except FileNotFoundError:
        print("\nNo journal file found yet.\n")
def search_entry():
    try:
        date = input("Enter date to search (YYYY-MM-DD): ")
        found = False
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if f"Date: {date}" in lines[i]:
                    found = True
                    print("\n===== Entry Found =====")
                    print(lines[i].strip())
                    print(lines[i + 1].strip())
                    print("-" * 40)
        if not found:
            print("\nNo entry found for that date.\n")
    except FileNotFoundError:
        print("\nNo journal file found yet.\n")
def edit_entry():
    try:
        date = input("Enter date to edit (YYYY-MM-DD): ")
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        entries = []
        i = 0
        while i < len(lines):
            if f"Date: {date}" in lines[i]:
                entry_text = lines[i + 1].strip()
                entries.append((i, entry_text))
            i += 1
        if not entries:
            print("\nNo entry found for that date.\n")
            return
        print(f"\nFound {len(entries)} entries for {date}:")
        for idx, (line_no, entry_text) in enumerate(entries, start=1):
            print(f"{idx}. {entry_text}")
        choice = int(input("\nEnter the number of the entry you want to edit: "))
        if choice < 1 or choice > len(entries):
            print("\nInvalid choice.\n")
            return
        selected_index = entries[choice - 1][0]
        print("\nCurrent Entry:")
        print(lines[selected_index + 1].strip())
        new_entry = input("\nWrite the new entry: ")
        if new_entry.strip() == "":
            print("Entry cannot be empty!\n")
            return
        lines[selected_index + 1] = f"Entry: {new_entry}\n"
        with open(FILENAME, "w") as file:
            file.writelines(lines)
        print("\nEntry updated successfully!\n")
    except FileNotFoundError:
        print("\nNo journal file found yet.\n")
    except ValueError:
        print("\nPlease enter a valid number!\n")
def delete_entry():
    date_to_delete = input("Enter date to delete (YYYY-MM-DD): ")
    with open("journal.txt", "r") as f:
        lines = f.readlines()
    new_lines = []
    deleted = False
    i = 0
    while i < len(lines):
        if lines[i].startswith("Date:") and date_to_delete in lines[i]:
            print("\nDeleting this entry:")
            print(lines[i].strip())
            print(lines[i+1].strip())
            confirm = input("Do you want to delete this entry? (y/n): ").lower()
            if confirm == "y":
                deleted = True
                i += 3  
                continue
        new_lines.append(lines[i])
        i += 1
    if deleted:
        with open("journal.txt", "w") as f:
            f.writelines(new_lines)
        print("\nEntry deleted successfully!\n")
    else:
        print("\nNo entry found for that date.\n")
def main():
    while True:
        print("\n===== PERSONAL DAILY JOURNAL APP =====")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entry by Date")
        print("4. Edit Entry by Date")
        print("5. Delete Entry by Date")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                add_entry()
            elif choice == 2:
                view_entries()
            elif choice == 3:
                search_entry()
            elif choice == 4:
                edit_entry()
            elif choice == 5:
                delete_entry()
            elif choice == 6:
                print("\nThank you for using the Journal App! Goodbye!\n")
                break
            else:
                print("\nInvalid choice! Please try again.\n")
        except ValueError:
            print("\nPlease enter a valid number (1-6)!\n")
main()
