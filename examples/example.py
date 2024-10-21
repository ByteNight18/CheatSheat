# cheatsheet_usage.py

# Importing the necessary classes from cheatsheet.py
from cheatsheet import mc, tc, jc, auto_test  # Update with your actual module name

# Math Operations
def demonstrate_math_operations():
    print("=== Math Operations ===")
    
    num1 = 10
    num2 = 5

    # Addition
    print(f"{num1} + {num2} = {mc.add(num1, num2)}")
    
    # Subtraction
    print(f"{num1} - {num2} = {mc.sub(num1, num2)}")
    
    # Multiplication
    print(f"{num1} * {num2} = {mc.mul(num1, num2)}")
    
    # Division
    print(f"{num1} / {num2} = {mc.div(num1, num2)}")
    
    # Adding to a list
    my_list = [1, 2, 3, 4]
    increment_value = 2
    print(f"Adding {increment_value} to {my_list} gives: {mc.arraycal(increment_value, my_list)}")

# Time Operations
def demonstrate_time_operations():
    print("\n=== Time Operations ===")
    
    print(f"Current Time: {tc.time()}")
    print(f"Current Date: {tc.date()}")
    print(f"Time Zone Info: {tc.tz()}")

    print("Waiting for 3 seconds...")
    tc.timer(3)
    print("Done waiting!")

# JSON Handling
def demonstrate_json_handling():
    print("\n=== JSON Handling ===")
    
    # Assuming you have a 'data.json' file with a dictionary
    json_file = 'data.json'  # Replace with your actual JSON file path
    print("Extracting data from JSON file:")
    
    try:
        extracted_data = jc.extract(json_file)
        print("Extracted Data:", extracted_data)
        
        # Using take method
        key = 'example_key'  # Replace with an actual key from your JSON file
        value = jc.take(json_file, key)
        print(f"Value for '{key}':", value)
    except FileNotFoundError:
        print(f"File '{json_file}' not found.")

# Auto Testing
def demonstrate_auto_testing():
    print("\n=== Auto Testing ===")
    
    # Assuming you have 'data.py' for code and 'config.json' for expected results
    data_file = 'data.py'  # Replace with your actual Python file path
    config_file = 'config.json'  # Replace with your actual config file path

    print("Running auto tests...")
    test_result = auto_test.run(data_file, config_file)
    
    if test_result:
        print("Test passed! Output matches expected results.")
    else:
        print("Test failed! Output does not match expected results.")

# Main execution
if __name__ == "__main__":
    demonstrate_math_operations()
    demonstrate_time_operations()
    demonstrate_json_handling()
    demonstrate_auto_testing()
