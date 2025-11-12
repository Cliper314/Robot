from fairino import Robot

robot = Robot.RPC('192.168.58.2')

# 请替换为你的实际位姿（单位：mm, °）
pos_left_down  = [-500, -175, 250, 90, 0, 0]
pos_right_down = [-400, -175, 250, 90, 0, 0]
pos_right_up   = [-400,   0, 250, 90, 0, 0]
pos_left_up    = [-500,   0, 250, 90, 0, 0]

speed = 10  # 速度百分比

# 依次移动（直线运动）
robot.MoveL(desc_pos=pos_left_down,  tool=0, user=0, vel=speed)
robot.MoveL(desc_pos=pos_right_down, tool=0, user=0, vel=speed)
robot.MoveL(desc_pos=pos_right_up,   tool=0, user=0, vel=speed)
robot.MoveL(desc_pos=pos_left_up,    tool=0, user=0, vel=speed)
robot.MoveL(desc_pos=pos_left_down,  tool=0, user=0, vel=speed)  # 闭合