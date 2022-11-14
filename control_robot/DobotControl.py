
import time
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#将dll读取到内存中并获取对应的CDLL实例
#Load Dll and get the CDLL object
api = dType.load()
#建立与dobot的连接
#Connect Dobot
state = dType.ConnectDobot(api, "COM3", 115200)[0]





if (state == dType.DobotConnect.DobotConnect_NoError):
    #Clean Command Queued
    dType.SetQueuedCmdClear(api)
    
    #设置运动参数
    #Async Motion Params Setting
    dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
    dType.SetPTPJointParams(api, 50, 50, 50, 50, 50, 50, 50, 50, isQueued = 1)
    dType.SetPTPCommonParams(api, 50, 50, isQueued = 1)

    # #Async Home
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)
    # #Async PTP Motion
    # #Start to Execute Command Queue
    # print("a")
    dType.SetEndEffectorSuctionCup(api, True, True, isQueued = 1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 50, 50, 0,isQueued=1)
    lastIndex = dType.SetEndEffectorSuctionCup(api, True, False, isQueued = 0)[0]
    print(lastIndex)



    dType.SetQueuedCmdStartExec(api)

    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        print(dType.GetQueuedCmdCurrentIndex(api)[0])
        time.sleep(5)
    # #Stop to Execute Command Queued

    dType.SetQueuedCmdStopExec(api)



#Disconnect Dobot
dType.DisconnectDobot(api)
