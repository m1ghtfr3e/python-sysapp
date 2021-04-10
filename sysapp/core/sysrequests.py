#!/usr/bin/python python

'''
A script to get information of the current state
of processes.
'''

from typing import NamedTuple, NewType, Dict, List

try:
    import psutil
except ImportError:
    print('\n>> python3 -m pip install psutil\n')


# Specific Types
#
# Dictionaries returned from psutil modules
# normally don't go along with python / pylint
# conventions.
PSdict = NewType('PSdict', Dict[str, NamedTuple])
PSlist = NewType('PSlist', List[NamedTuple])

# System specific functions

def count_cpus() -> int:
    ''' Number of logical CPUs
    '''
    return psutil.cpu_count()

def count_cpus_nonlogical() -> int:
    ''' Number of "hard" CPUs
    '''
    return psutil.cpu_count(logical=False)

def cpu_stats() -> NamedTuple:
    ''' CPU Stats

    Returns a named tuple.
    ctx_switches:  number of context switches
                  since boot.
    interrupts: number of interrupts since
                boot.
    soft_interrupts: number of software
                     interrupts since boot.
    syscalls: number of syscalls since boot.
              ! always set to 0 on Linux !
    '''
    return psutil.cpu_stats()

def cpu_frequency_all() -> NamedTuple:
    ''' Summary of CPU Frequency

    Returns a named tuple.
    '''
    return psutil.cpu_freq(percpu=False)

def cpu_frequency_each() -> NamedTuple:
    ''' Frequency per CPU

    Returns a named tuple.
    '''
    return psutil.cpu_freq(percpu=True)

def cpu_percent() -> float:
    ''' CPU Utilization in percent

    Returns the system wide utilization of CPU
    as percentage.
    '''
    return psutil.cpu_percent()

def average_sysload() -> tuple:
    ''' Average System Load

    Returns a tuple, consisting the values of
    the average system load over the last 1, 5 and
    15 minutes.
    '''
    return psutil.getloadavg()

# Memory specific functions.

def virtual_memory() -> NamedTuple:
    ''' Statistics about Virtual Memory

    Returns a named tuple consisting of fields
    expressed in bytes.
    '''
    return psutil.virtual_memory()

def virtual_memory_dict() -> PSdict:
    ''' Statistics about Virtual Memory
        represented as a dictionary

    Like Virtual Memory but as dict.
    '''
    return psutil.virtual_memory()._asdict()

def used_ram_percent() -> float:
    ''' Used RAM as Percentage
    '''
    return psutil.virtual_memory().percent

def available_ram_percent() -> float:
    ''' Available RAM as Percentage
    '''
    available = psutil.virtual_memory().available
    total = psutil.virtual_memory().total
    percentage = (available * 100) / total
    return percentage

def swap_memory() -> NamedTuple:
    ''' Statistics about Swap Memory

    Returns a named tuple consisting of fields
    expressed in bytes.
    '''
    return psutil.swap_memory()

# Disk specific functions

def disk_partitions() -> PSlist:
    ''' Mounted Disk Partitions

    Returns a list of named Tuples with informations
    about all mounted disk Partitions.
    '''
    return psutil.disk_partitions()

def disk_usage(path: str = '/') -> NamedTuple:
    ''' Disk Usage of the Partition holding
        the given Path

    Returns a named Tuple.
    '''
    return psutil.disk_usage(path)

def io_statistics() -> PSdict:
    ''' Statistics about system wide Disk I/O

    Returns a dictionary holding named tuples with
    I/O statistics for each mounted disk.

    Notes
    -----
    "nowrap" is activated to True by default.
    '''
    return psutil.disk_io_counters(perdisk=True)

# Network specific functions.

...

# Sensors specific functions.

def sensors_temp() -> PSdict:
    ''' Hardware temperatures in Celsius

    Returns a dictionary with a named Tuple for each
    hardware temperature sensors entry.
    '''
    return psutil.sensors_temperatures(fahrenheit=False)

def sensors_fans() -> PSdict:
    ''' Hardware Fans Speed
    '''
    ...
