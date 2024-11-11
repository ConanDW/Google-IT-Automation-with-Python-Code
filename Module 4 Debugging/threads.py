from concurrent import futures

executor = futures.ThreadPoolExecutor()

executor.submit(process_file, root, basename)
#once done, shutdown executor
executor.shutdown
#this is an example of how to run stuff in parallel in threads

executor_two = futures.ProcessPoolExecutor()
#use processes instead of threads
executor.shutdown