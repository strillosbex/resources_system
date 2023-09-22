import platform
import psutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
            
def system_information():
    partitions = psutil.disk_partitions()
    svmem = psutil.virtual_memory()
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    
    array_system = {}
    array_system = {
        'system': uname.system,
        'node': uname.node,
        'release': uname.release,
        'version': uname.version,
        'machine': uname.machine,
        'processor': uname.processor,
        'memory_total': get_size(svmem.total),
        'memory_available': get_size(svmem.available),
        'memory_used': get_size(svmem.used),
        'memory_percent': f'{svmem.percent}%',
        'cores_physical': psutil.cpu_count(logical=False),
        'cores_logical': psutil.cpu_count(logical=True),
        'cpu_total_usage': f'{psutil.cpu_percent()}%',
        'frequency_max': f'{cpufreq.max:.2f}Mhz',
        'frequency_min': f'{cpufreq.min:.2f}Mhz',
        'frequency_current': f'{cpufreq.current:.2f}Mhz'
    }
    
    array_system['partition'] = []
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        #disk_io = psutil.disk_io_counters()
        array_system['partition'].append({
            'partition_device': partition.device,
            'partition_mountpoint': partition.mountpoint,
            'partition_total': get_size(partition_usage.total),
            'partition_used': get_size(partition_usage.used),
            'partition_free': get_size(partition_usage.free),
            'partition_percent': f'{partition_usage.percent}%'
            
            #,'disk_io_read': get_size(disk_io.read_bytes)
            #,'disk_io_write': get_size(disk_io.write_bytes)
        })
    
    return array_system

"""
if __name__ == '__main__':
    informations = system_information()
    print(informations)
"""