import time
start=input("Enter the start time")
end=input("Enter the end time")
start_stopwatch=time.time()

end_stopwatch=time.time()

elapsed_time =  end_stopwatch-start_stopwatch

print(f"Elapsed Time is :{elapsed_time} second")
