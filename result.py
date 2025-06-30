def read_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines[-1] if lines else None  # 返回最后一行，如果文件为空则返回None

# 使用示例
# 读取force,Fx
force_path = "./postProcessing/forceMonitorOnPropellerInDefault/0/force.dat"
last_line = read_last_line(force_path)
print("Fx:",last_line.split()[1])
# 读取moment,Mx
moment_path="./postProcessing/forceMonitorOnPropellerInDefault/0/moment.dat"
last_line = read_last_line(moment_path)
print("Mx:",last_line.split()[1])

