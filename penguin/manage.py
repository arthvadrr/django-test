#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
from datetime import datetime

# Logger configuration
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'penguin.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        error_message = "Django is not installed or not available on PYTHONPATH."
        logging.error(error_message)
        raise ImportError(error_message)
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        logging.error(error_message)
        raise

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    start_time = datetime.now()
    try:
        main()
    except ImportError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        end_time = datetime.now()
        print(f"Execution time: {end_time - start_time}")