import threading

def thread_func():
    for i in range(0, 50):
        print(i)

def main():

    t1 = threading.Thread(target=thread_func)
    t1.start()

    for i in range(0, 20):
        print(f"Hello {i}")

    t1.join()

    print("Done!")

if __name__ == "__main__":
    main()
