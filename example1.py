'''
Example 1: This is an example of a synchronous Python script. 
'''
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import asyncio

def fetch_data():
    print("Fetching data...")
    time.sleep(2)  # Simulate a delay in fetching data
    print("Data fetched successfully!")
    return f"Results of data fetching at {time.ctime()}"

def main():
    print("Starting the script...")
    result1 = fetch_data()
    print("fetch completed")
    result2 = fetch_data()
    print("fetch completed")
    print("Script finished.")
    return result1, result2

t1 = time.time()

results = main()
print("Results:", results)

t2 = time.time()
print(f"Script completed in {t2 - t1:.2f} seconds.")

'''
Example 2: Example of an asynchronous code in python below
'''

async def fetch_data_async():
    print("Fetching data asynchronously...")
    await asyncio.sleep(2)  # Simulate a delay in fetching data
    print("Data fetched successfully!")
    return f"Results of async data fetching at {time.ctime()}"

async def main_async():
    task1 = fetch_data_async() # This creates a coroutine object but does not start it yet
    task2 = fetch_data_async() # This creates a coroutine object but does not start it yet
    results = await asyncio.gather(task1, task2) # This starts both tasks concurrently and waits for them to complete
    print("Task 1 completed successfully.")
    print("Task 2 completed successfully.")
    return results

t1 = time.time()

results_async = asyncio.run(main_async()) # This runs the main_async coroutine, which in turn runs the fetch_data_async coroutines concurrently 
print("Results:", results_async)

t2 = time.time()
print(f"Async script completed in {t2 - t1:.2f} seconds.")


'''
Example 3: asycnronous code with coroutine using asyncio.create_task
'''

async def fetch_data_async():
    print("Fetching data asynchronously...")
    await asyncio.sleep(2)  # Simulate a delay in fetching data
    print("Data fetched successfully!")
    return f"Results of async data fetching at {time.ctime()}"

async def main_async_create():
    task1 = asyncio.create_task(fetch_data_async()) # This creates a task that will run the fetch_data_async coroutine concurrently
    task2 = asyncio.create_task(fetch_data_async()) # This creates a task that will run the fetch_data_async coroutine concurrently
    results = await asyncio.gather(task1, task2) # This waits for both tasks to complete and gathers their results
    print("Task 1 completed successfully.")
    print("Task 2 completed successfully.")
    return results


t1 = time.time()

results_async_create = asyncio.run(main_async_create()) # This runs the main_async_create coroutine, which in turn creates and runs the fetch_data_async coroutines concurrently using create_task
print("Results:", results_async_create)

t2 = time.time()
print(f"Async script with create_task completed in {t2 - t1:.2f} seconds.")

# Aother scenario to the above example but here we await task 2 first

async def main_async_create_await_task2_first():
    task1 = asyncio.create_task(fetch_data_async()) # This creates a task that will run the fetch_data_async coroutine concurrently
    task2 = asyncio.create_task(fetch_data_async()) # This creates a task that will run the fetch_data_async coroutine concurrently
    result2 = await task2 # This waits for task2 to complete and gets its result first
    print("Task 2 completed successfully.")
    result1 = await task1 # This waits for task1 to complete and gets its result after task2 has completed
    print("Task 1 completed successfully.")
    return result1, result2

t1 = time.time()

results_async_create_await_task2_first = asyncio.run(main_async_create_await_task2_first()) # This runs the main_async_create_await_task2_first coroutine, which creates and runs the fetch_data_async coroutines concurrently using create_task and awaits task2 first
print("Results:", results_async_create_await_task2_first)

t2 = time.time()
print(f"Async script with create_task and awaiting task2 first completed in {t2 - t1:.2f} seconds.")
'''
Example 4: Asynchronous code with coroutine using asyncio.create_task and handling exceptions
'''
async def fetch_data_async_with_error():
    print("Fetching data asynchronously with error...")
    await asyncio.sleep(2)  # Simulate a delay in fetching data
    raise Exception("An error occurred while fetching data!") # Simulate an error during data fetching

async def main_async_with_error():
    task1 = asyncio.create_task(fetch_data_async_with_error()) # This creates a task that will run the fetch_data_async_with_error coroutine concurrently
    task2 = asyncio.create_task(fetch_data_async_with_error()) # This creates a task that will run the fetch_data_async_with_error coroutine concurrently
    try:
        results = await asyncio.gather(task1, task2) # This waits for both tasks to complete and gathers their results
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    print("Task 1 completed successfully.")
    print("Task 2 completed successfully.")
    return results

'''
Example 5: We'll do this using asynchronous blocking code
'''
async def fetch_data_async_blocking():
    print("Fetching data asynchronously with blocking code...")
    time.sleep(2)  # This is a blocking call that will block the entire event loop, preventing other tasks from running concurrently
    print("Data fetched successfully!")
    return f"Results of async data fetching with blocking code at {time.ctime()}"

async def main_async_blocking():
    task1 = asyncio.create_task(fetch_data_async_blocking()) # This creates a task that will run the fetch_data_async_blocking coroutine concurrently
    task2 = asyncio.create_task(fetch_data_async_blocking()) # This creates a task that will run the fetch_data_async_blocking coroutine concurrently
    results = await asyncio.gather(task1, task2) # This waits for both tasks to complete and gathers their results, but since the fetch_data_async_blocking function contains blocking code, it will block the entire event loop and prevent the tasks from running concurrently, resulting in a total execution time of approximately 4 seconds instead of 2 seconds if they were running concurrently without blocking code.
    print("Task 1 completed successfully.")
    print("Task 2 completed successfully.")
    return results

t1 = time.time()

'''
Example 6: using threads and processes
'''
async def fetch_data_async_thread():
    print("Fetching data asynchronously in a thread...", flush=True)
    time.sleep(2)  # Simulate a delay in fetching data
    print("Data fetched successfully in thread!", flush=True)
    return f"Results of async data fetching in thread at {time.ctime()}"


async def main_thread():
    # Run in Threads
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        task1 = loop.run_in_executor(executor, fetch_data_async_thread) # This runs the fetch_data_async_thread function in a separate thread using the ThreadPoolExecutor
        task2 = loop.run_in_executor(executor, fetch_data_async_thread) # This runs the fetch_data_async_thread function in a separate thread using the ThreadPoolExecutor
        results = await asyncio.gather(task1, task2) # This waits for both tasks to complete and gathers their results
        print("Task 1 completed successfully.")
        print("Task 2 completed successfully.")
        return results

        # Run in Process Pool
    with ProcessPoolExecutor() as executor:
        loop = asyncio.get_running_loop()

        task1 = loop.run_in_executor(executor, fetch_data_async_thread) # This runs the fetch_data_async_thread function in a separate process using the ProcessPoolExecutor
        task2 = loop.run_in_executor(executor, fetch_data_async_thread) # This runs the fetch_data_async_thread function in a separate process using the ProcessPoolExecutor
        results = await asyncio.gather(task1, task2) # This waits for both tasks to complete and gathers their results
        print("Task 1 completed successfully.")
        print("Task 2 completed successfully.")
        return results
