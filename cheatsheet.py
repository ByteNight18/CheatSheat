from datetime import datetime, timedelta
from tzlocal import get_localzone
import time
import json

class mc:
    @staticmethod
    def norp(num):
        if num > 0:
            return 'P'
        elif num < 0:
            return 'N'
        return None

    @staticmethod
    def arraycal(num, lst):
        return [i + num for i in lst]  # List comprehension for adding num to each element

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


class tc:
    @staticmethod
    def time():
        return datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def date():
        return datetime.now().strftime('%d/%m/%Y')

    @staticmethod
    def tz():
        local_tz = get_localzone()
        current_time = datetime.now(local_tz)
        tz_name = current_time.tzname()
        utc_offset = current_time.utcoffset()
        is_dst = current_time.dst() != timedelta(0)

        return {
            'system_time_zone': str(local_tz),
            'time_zone_name': tz_name,
            'utc_offset': utc_offset,
            'is_dst': is_dst,
            'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def timer(count):
        time.sleep(count)
        return True


class jc:
    @staticmethod
    def extract(file):
        with open(file, 'r') as data:
            return json.load(data)

    @staticmethod
    def take(file, key):
        with open(file, 'r') as data:
            extracted = json.load(data)
            return extracted.get(key, None)  # Return the result directly


class auto_test:
    @staticmethod
    def run(data, config):
        with open(config, 'r') as config_file:
            expected = json.load(config_file)["expected"]

        with open(data, 'r') as code_file:
            code = code_file.read()  # Read the code from the file

        local_scope = {}  # Create a local scope for exec
        exec(code, {}, local_scope)  # Execute the code
        
        output = local_scope.get('output', None)  # Replace 'output' with the actual variable name if different
        
        return expected == output  # Return True or False directly
