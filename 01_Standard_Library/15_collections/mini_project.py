from collections import Counter, defaultdict, deque, namedtuple, ChainMap
Book = namedtuple("Book", ["title", "author", "category"])
books = [
    Book("Python Basics", "John", "Programming"),
    Book("AI Essentials", "Alice", "AI"),
    Book("Machine Learning", "Bob", "AI"),
    Book("Data Structures", "David", "Programming"),
    Book("Database Systems", "Emma", "Database"),
    Book("Python Advanced", "John", "Programming")
]
borrow_queue = deque()
catalog1 = {
    "Python Basics": 5,
    "AI Essentials": 3
}

catalog2 = {
    "Machine Learning": 4,
    "Database Systems": 2
}

def count_categories():
    categories = [book.category for book in books]
    counter = Counter(categories)
    print("\nBook Categories\n")
    for category, count in counter.items():
        print(f"{category}: {count}")

def show_books():
    grouped = defaultdict(list)
    for book in books:
        grouped[book.category].append(book.title)
    print("\nBooks By Category\n")
    for category, titles in grouped.items():
        print(f"{category}")
        for title in titles:
            print(f"  - {title}")

def borrow_book():
    title = input("Enter Book Title: ")
    borrow_queue.append(title)
    print("Book Added To Borrow Queue.")

def view_queue():
    if not borrow_queue:
        print("Borrow Queue Is Empty.")
        return
    print("\nBorrow Queue\n")
    for position, book in enumerate(borrow_queue, start=1):
        print(f"{position}. {book}")

def next_borrower():
    if not borrow_queue:
        print("Borrow Queue Is Empty.")
        return
    book = borrow_queue.popleft()
    print(f"{book} Borrowed Successfully.")

def merge_catalogs():
    library = ChainMap(catalog1, catalog2)
    print("\nCombined Catalog\n")
    for title, copies in library.items():
        print(f"{title} : {copies} Copies")

while True:
    print("\n" + "=" * 40)
    print("    LIBRARY INVENTORY ANALYZER")
    print("=" * 40)

    print("1. Count Books By Category")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. View Borrow Queue")
    print("5. Next Borrower")
    print("6. Merge Library Catalogs")
    print("7. Exit")
    choice = input("\nEnter Choice: ")
    if choice == "1":
        count_categories()
    elif choice == "2":
        show_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        view_queue()
    elif choice == "5":
        next_borrower()
    elif choice == "6":
        merge_catalogs()
    elif choice == "7":
        print("\nThank You For Using Library Inventory Analyzer!")
        break
    else:
        print("Invalid Choice!")