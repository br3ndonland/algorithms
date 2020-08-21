import os
import sys

version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"Hello World, from Python {version} in an external script!")
print(f"Did you know that {os.getenv('SPAM_STRING', 'there is a SPAM_STRING')}?")
