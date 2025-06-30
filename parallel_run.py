import subprocess
import sys

# 调用 shell 脚本，并实时打印输出
process = subprocess.Popen(['bash', './run.sh'], stdout=sys.stdout, stderr=sys.stderr)

# 等待脚本执行完毕
process.wait()

# 检查返回码
if process.returncode == 0:
    print("Script executed successfully!")
else:
    print(f"Script failed with return code {process.returncode}")
