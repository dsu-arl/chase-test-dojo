# Multiple Threads

Now that you know how to make a thread, and pass arguments to it, we're going to challenge you! Using your Python coding experience you're going to create a program that accepts a number 1-20 and then creates that many threads.

You can use the `argparse` library to accept the thread count as a command line argument. You can use the following outline to build your code off of:

```python
import argparse
import threading

def thread_func(arg1):
    for _ in range(10):
        print(f"This is thread {arg1}")

def main():

    num_of_threads = args.thread_count

    # Check that num_of_threads is no less than 1, and no greater than 20

    # Go through and create the exact number of threads specified
    # Hint: Use a loop. Also, did you know you can store threads in a list?

    # Put whatever you want

    # Join all the threads back to main
    # Hint: Use a loop. Also, did you make a list?

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("thread_count", type=int, help="Number of threads to create!")
    args = parser.parse_args()

    main()

```

When you have added the proper code and have tested it, run `/challenge/run <your_file>` to verify and get your flag!
