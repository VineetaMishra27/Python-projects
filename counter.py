def counter_app():
    print("Counter App Starting...")
    count = 0

    while True:
        print(f"\nCurrent Count: {count}")
        print("Choose an option:")
        print("1. Increment")
        print("2. Decrement")
        print("3. Reset")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            count += 1
        elif choice == '2':
            count -= 1
        elif choice == '3':
            count = 0
        elif choice == '4':
            print("Exiting Counter App.")
            break
        else:
            print("Invalid choice. Try again.")

counter_app()
          

