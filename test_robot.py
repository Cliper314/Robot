from fairino import Robot

# 与机器人控制器建立连接
robot = Robot.RPC('192.168.58.2')

# 获取 SDK 版本
error, version = robot.GetSDKVersion()
if error:
    print(f"Error Detected: {error}")
else:
    print(f"SDK version: {version}")

# 获取控制器 IP
error, ip = robot.GetControllerIP()
if error:
    print(f"Error Detected: {error}")
else:
    print(f"Controller IP: {ip}")