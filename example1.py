'''
This is an example of a synchronous Python script. 
'''
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


