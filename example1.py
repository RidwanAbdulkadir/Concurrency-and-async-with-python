'''
Example 1: This is an example of a synchronous Python script. 
'''
import asyncio
import time

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
    task1 = fetch_data_async()
    task2 = fetch_data_async()
    results = await asyncio.gather(task1, task2)
    print("Task 1 completed successfully.")
    print("Task 2 completed successfully.")
    return results

t1 = time.time()

results_async = asyncio.run(main_async())
print("Results:", results_async)

t2 = time.time()
print(f"Async script completed in {t2 - t1:.2f} seconds.")

