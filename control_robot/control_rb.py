from control_robot import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#将dll读取到内存中并获取对应的CDLL实例
#Load Dll and get the CDLL object
api = dType.load()
#建立与dobot的连接
#Connect Dobot
state = dType.ConnectDobot(api, "COM4", 115200)[0]


def control(x,y):
    if (state == dType.DobotConnect.DobotConnect_NoError):
        #Clean Command Queued
        dType.SetQueuedCmdClear(api)
        
        #设置运动参数
        #Async Motion Params Setting
        dType.SetPTPCommonParams(api, 500, 500, isQueued = 0)
        dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 0)
        dType.SetPTPJointParams(api, 50, 50, 50, 50, 50, 50, 50, 50, isQueued = 0)
        # dType.SetHOMECmd(api, temp = 0, isQueued = 0)
        for x_item in x:
            for y_item in y:
                dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,80,10, isQueued=1)
                dType.SetWAITCmd(api, 200, isQueued=1)
                dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,30,10, isQueued=1)
                # dType.SetWAITCmd(api, 200, isQueued=1)
                dType.SetEndEffectorSuctionCup(api, True,  True, isQueued=1)
                dType.SetWAITCmd(api, 500, isQueued=1)
                dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,80,10, isQueued=1)
                dType.SetWAITCmd(api, 1000, isQueued=1)
                dType.SetEndEffectorSuctionCup(api, True,  False, isQueued=1)
            # dType.SetWAITCmd(api, 2000, isQueued=1)
    # dType.SetEndEffectorSuctionCup(api, True,  True, isQueued=1)
    # dType.SetWAITCmd(api, 2000, isQueued=1)
    # dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, 210,y_robot[0],80,60, isQueued=1)
    # dType.SetEndEffectorSuctionCup(api, True,  False, isQueued=1)
    # print("a")

    # dType.SetEndEffectorSuctionCup(api, True,  True, isQueued=1)
    # dType.SetWAITCmd(api, 5000, isQueued=1)
    # # dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x+10, y, z, rHead, isQueued=1)
    # dType.SetWAITCmd(api, 5000, isQueued=1)
    # lastIndex = dType.SetEndEffectorSuctionCup(api, True,  False, isQueued=1)[0]
    # print(lastIndex)




#     # #Async Home
#     dType.SetHOMECmd(api, temp = 0, isQueued = 1)
#     # #Async PTP Motion
#     # #Start to Execute Command Queue
#     # print("a")
#     dType.SetEndEffectorSuctionCup(api, True, True, isQueued = 1)
#     dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 50, 50, 0,isQueued=1)
#     lastIndex = dType.SetEndEffectorSuctionCup(api, True, False, isQueued = 0)[0]
#     print(lastIndex)



#     dType.SetQueuedCmdStartExec(api)

#     while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
#         print(dType.GetQueuedCmdCurrentIndex(api)[0])
#         time.sleep(1)
# #     # #Stop to Execute Command Queued

#     dType.SetQueuedCmdStopExec(api)


dType.DisconnectDobot(api)
# #Disconnect Dobot
# dType.DisconnectDobot(api)
