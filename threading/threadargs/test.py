import threading

def thread_func(arg1, arg2):
    for i in range(0, 50):
        if i % 2 == 0:
            print(arg1)
        else:
            print(arg2)

def main():
    t1 = threading.Thread(target=thread_func, args=("Yummy", "Foop"))
    t1.start()

    for i in range(0, 27):
        print(i)

    t1.join()
    print("Done!")

if __name__ == "__main__":
    main()
