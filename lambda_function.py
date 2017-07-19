import os
import sys

# for vendor directory
sys.path.append(
    os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)), 'vendor'))


def handler(event, context):
    return True
