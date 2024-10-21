# Cheatsheet Module

## Overview
The Cheatsheet Module is a versatile Python library designed to provide quick references for common programming tasks. It includes functions for mathematical operations, JSON data handling, time management, and automated testing. This module is aimed at making programming more efficient and user-friendly.

## Features
- **Mathematical Operations**: Functions for addition, subtraction, multiplication, and division.
- **JSON Handling**: Easy extraction and manipulation of JSON data.
- **Time Management**: Functions to get the current time, date, and timezone information.
- **Automated Testing**: Execute tests based on specified configurations to ensure code reliability.

## Installation
To install the Cheatsheet Module, you can clone the repository or install it via pip (Will Commit On PyPi later)

### Cloning the Repository
```bash
git clone https://github.com/ByteNight18/cheatsheet.git
cd cheatsheet-module
```

### Installing Required Libraries
Ensure you have the required library installed:
```bash
pip install tzlocal
```
###Usage
The Cheatsheet Module contains several classes that provide different functionalities.

```python
Classes
Math Class (mc)
norp(num): Returns 'P' for positive numbers, 'N' for negative numbers, and None for zero.
arraycal(num, lst): Adds a number to each element in a list.
add(a, b): Returns the sum of two numbers.
sub(a, b): Returns the difference between two numbers.
mul(a, b): Returns the product of two numbers.
div(a, b): Returns the quotient of two numbers.
JSON Class (jc)
extract(file): Extracts JSON data from a specified file.
take(file, key): Retrieves a value associated with a key from a JSON file.
Time Class (tc)
time(): Returns the current time.
date(): Returns the current date.
tz(): Returns timezone information, including current time, name, and UTC offset.
timer(count): Pauses execution for a specified number of seconds.
Auto Testing Class (auto_test)
run(data, config): Executes tests based on provided data and configuration files.
Example Code
Here’s a quick example of how to use the Cheatsheet Module:

python
Copy code
from cheatsheet import mc, tc, jc, auto_test

# Mathematical Operations
print(mc.add(10, 5))  # Outputs: 15
print(mc.norp(-10))    # Outputs: 'N'

# JSON Handling
data = jc.extract('data.json')
print(data)

# Time Management
print(tc.time())       # Outputs current time
print(tc.tz())         # Outputs timezone information

# Automated Testing
result = auto_test.run('data.py', 'config.json')
print('Test passed:', result)
Documentation
For detailed usage instructions and further examples, please refer to the Documentation page.
```

##Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to create a pull request or open an issue.

##Issues
If you encounter any bugs or issues, please report them on the Issues page of this repository.

##License
This project is licensed under the MIT License. See the LICENSE file for details.

###Support
If you find this module helpful, consider starring the repository or sharing it with others!
