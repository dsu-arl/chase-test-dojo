# Creating Threads

In python, creating threads is extremely simple. It's organizing and managing threads that is more difficult, but we will get to that later! In python, as always, we will need the right tools to do the job:

```python
import threading
```

We import the `threading` library, our toolbox, so that we can perform threading actions. 

Now that we have our tools available to us we can begin using them. This challenge is solely about creating a thread and letting it run. To create a thread, first of all, we need code to run in that thread. For this example, we will keep it simple. You can just copy the following function into your python file:

```python
def thread_func():
    for i in range(0,50):
        print(i)
```

All this thread function is doing is looping from 0-49 and printing the numbers out. This will help us actually see how our threading is working.

Now, to create a thread with our new `thread_func` we only need to add three lines:
- `t1 = threading.Thread(target=thread_func)` - Here we create an instance of the `Thread` class. The target is the function we want to run on a different thread. *Note: We will look at passing function arguments in other challenges.*
- `t1.start()` - This call actually starts the thread. Our function should now be running in a different thread, and our main thread should continue execution.
- `t1.join()` - This function call tells our main thread to stop and wait for our `t1` thread to finish executing and join back with the main thread.

It is rather simple at the start. Now, keep in mind, you can add whatever code you want between `t1.start()` and `t1.join()`, and it will run alongside your target function. 

For this challenge you will need to:
0. Import the threading library.
1. Copy our `thread_func()` into your python file.
2. Create a thread with this function as the target.
3. Start the thread.
4. Create a loop that prints out whatever text you want, 100 times.
5. Join the thread after your print loop.
6. Run your code and watch the threads work.

Afterwards you can run `/challenge/run <your_filename>` so that we can check your work. If your code looks good, we will give you the flag!
