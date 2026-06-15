#decorators

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Execute the original function and capture its return value
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to run.")
        
        return result  # Ensure the original function's output isn't lost
    return wrapper

@timer_decorator
def heavy_calculation(n):
    return sum(i * i for i in range(n))

# Call the decorated function
total = heavy_calculation(5_000_000)
print(f"Result: {total}")