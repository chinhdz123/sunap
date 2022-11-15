# import DobotDllType as dType

# CON_STR = {
#     dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
#     dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
#     dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

# #将dll读取到内存中并获取对应的CDLL实例
# #Load Dll and get the CDLL object
# api = dType.load()
# #建立与dobot的连接
# #Connect Dobot
# state = dType.ConnectDobot(api, "COM4", 115200)[0]

# x = [ 519, 644, 775, 908, 511, 644, 779, 922, 507, 644, 785, 932, 499, 643, 793, 947, 486, 639, 799, 964, 476, 635, 804, 980]
# y = [ 993, 988, 980, 965, 1107, 1101, 1095, 1081, 1231, 1230, 1221, 1209, 1367, 1364, 1357, 1349, 1513, 1510, 1505, 1502, 1671, 1673, 1674, 1676]
def control(x,y):
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
    state = dType.ConnectDobot(api, "COM4", 115200)[0]
    if (state == dType.DobotConnect.DobotConnect_NoError):
        print("connect")
        #Clean Command Queued
        dType.SetQueuedCmdClear(api)
        
        #设置运动参数
        #Async Motion Params Setting
        dType.SetPTPCommonParams(api, 500, 500, isQueued = 0)
        dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 0)
        dType.SetPTPJointParams(api, 50, 50, 50, 50, 50, 50, 50, 50, isQueued = 0)
        dType.SetHOMECmd(api, temp = 0, isQueued = 0)
        for x_item,y_item in zip(x,y):
            if x_item<315:
                print("x_item, y_item",x_item,y_item)
                # for y_item in y:
                dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
                dType.SetWAITCmd(api, 200, isQueued=1)
                dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,30,10, isQueued=1)
                # dType.SetWAITCmd(api, 200, isQueued=1)
                dType.SetEndEffectorSuctionCup(api, True,  True, isQueued=1)
                dType.SetWAITCmd(api, 500, isQueued=1)
                dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
                dType.SetWAITCmd(api, 1000, isQueued=1)
                dType.SetEndEffectorSuctionCup(api, True,  False, isQueued=1)
    dType.DisconnectDobot(api)
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


# dType.DisconnectDobot(api)
# #Disconnect Dobot
# dType.DisconnectDobot(api)
