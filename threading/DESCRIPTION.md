# Threading

As you learn how to write python programs, you learn how to write single threaded programs. Instructions are executed one by one, and in order. As you grow in your skills, you may run into situations where you want two things to be running at the same time. That is where threads come in. 

## What are threads?

A normal python program that you write is executed as a single thread. Threading allows us to add in as many threads as we want (or however many our computer can handle). This means you can have several different execution threads that run pseudo-simultaneously. I say 'pseudo-simultaneously' because, in general, our computer processors can only execute one instruction at a time. Yet, modern CPU's implement technology to allow concurrent commands to be executed. They do this by breaking up the CPU into different 'cores' that each operate as if they are different CPUs. This allows us to create programs that run simultaneously. 

Basic Program:
            Main Thread
        - - - - - - - - - -

Threaded Program:

                Main Thread
         - - - - - - - - - - - - - -
                - - - - - - 
                 2nd Thread

## What is this used for?

When you want two things running at the same time. For instance, imagine you have a chat application. You want your clients to be able to send, but also receive data at any time. This involves having one thread for listening for incoming data, and one thread waiting for the user to send data. 
