#coding=utf-8
import psutil

#打印cpu信息
print psutil.cpu_times()
#打印cpu逻辑个数
print psutil.cpu_count()
#打印cpu物理个数
print psutil.cpu_count(logical=False)

#打印内存信息
mem = psutil.virtual_memory()
print mem
#打印内存总数
print mem.total
#打印内存剩余
print mem.free

#列出所有进程PID
print psutil.pids()
#实例化一个对象，参数为进程PID
p = psutil.Process(65135)
#进程名
print p.name()
#进程路径
print p.exe()

