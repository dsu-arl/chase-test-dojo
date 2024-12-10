# Passing Arguments to Thread Func

Threading is fun, but our previous program was not impressive at all. We couldn't even pass arguments to our function, which is a necessity with 99% of programs. So, how do we go about doing that?

The good news is that it is very simple, and it doesn't require too much editing of our previous code to make it work!

The first thing we're going to do is edit our `thread_func` so that it takes in parameters and utilizes them. Here is our new function:

```python
def thread_func(arg1, arg2):
    for i in range(0, 50):
        if i % 2 == 0:
            print(arg1)
        else:
            print(arg2)
```

This new function takes in two arguments (`arg1` and `arg2`). It will print `arg1` if `i` is an even number, and it will print `arg2` if `i` is an odd number. 

Ok, now that our function takes in arguments, how do we actually pass them to our thread? To do that, you will need to edit the line where you create the Thread. In your first program you added the `target` parameter and set it to `thread_func`. Now you will add another parameter called `args` and set it equal to a tuple that contains your arguments:

```python
t1 = threading.Thread(target=thread_func, args=<tuple with arguments>)
```
Make the appropriate changes to your program and run it to see the effects! Once you have done that, run `/challenge/run <filename>` to verify that your code is correct to get your flag!
