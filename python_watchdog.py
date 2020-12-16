import os,subprocess,shlex,sys
print("输入要启动的进程的名字(包括路径):")
CommandLine = input()
args = shlex.split(CommandLine)
while True:
    print("启动进程:",args);
    try:
        #获取操作系统类型
        osname = os.name
        if 'nt' == osname:
            si = subprocess.STARTUPINFO();
            si.dwFlags = subprocess.SW_HIDE;
            process = subprocess.Popen(args,startupinfo=si)
        elif 'posix' == osname:
            process = subprocess.Popen(args,close_fds=True)

        #等待进程结束
        process.wait();
        print("进程结束，重新启动进程:",args)
    except OSError as err:
        print("启动程序产生异常:{0}".format(err))
        break
    except ValueError as verr:
        print("传入了错误的参数:{0}".format(err))
        break
    except:
        print("未知错误:{0}".format(sys.exc_info()))
        break
