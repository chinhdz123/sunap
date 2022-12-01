import DobotDllType as dType

class Control_robot():
    CON_STR = {
        dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
        dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
        dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
    def __init__(self) -> None:
        self.api =  dType.load()
        self.state = dType.ConnectDobot(self.api, "COM6", 115200)[0]
        if (self.state == dType.DobotConnect.DobotConnect_NoError):
            print("connect")
        #Clean Command Queued
        dType.SetQueuedCmdClear(self.api)
        dType.SetPTPCommonParams(self.api, 500, 500, isQueued = 0)
        dType.SetHOMEParams(self.api, 250, 0, 50, 0, isQueued = 0)
        dType.SetPTPJointParams(self.api, 50, 50, 50, 50, 50, 50, 50, 50, isQueued = 0)
        dType.SetHOMECmd(self.api, temp = 0, isQueued = 0)
        self.pose = dType.GetPose(self.api)
        self.x_pose = self.pose[0]
        self.y_pose = self.pose[1]
        self.z_pose = self.pose[2]

    def main(self,x,y):
        for x_item,y_item in zip(x,y):
            if x_item<315:
                print("x_item, y_item",x_item,y_item)
                # for y_item in y:
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
                dType.SetWAITCmd(self.api, 200, isQueued=1)
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,30,10, isQueued=1)
                # dType.SetWAITCmd(api, 200, isQueued=1)
                dType.SetEndEffectorSuctionCup(self.api, True,  True, isQueued=1)
                dType.SetWAITCmd(self.api, 500, isQueued=1)
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
                dType.SetWAITCmd(self.api, 1000, isQueued=1)
                dType.SetEndEffectorSuctionCup(self.api, True,  False, isQueued=1)
    def print(self):
        print(self.x_pose)
        print(self.z_pose)
    def up(self):
        dType.SetPTPCmd(self.api,dType.PTPMode.PTPMOVLXYZMode,self.x_pose,self.y_pose,self.z_pose+50,10,isQueued=1) 
        #print("up")
    def down(self):
        dType.SetPTPCmd(self.api,dType.PTPMode.PTPMOVLXYZMode,self.x_pose,self.y_pose,self.z_pose-10,10,isQueued=1) 
        #print("down")




""" 
def control(key,x,y):
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
    state = dType.ConnectDobot(api, "COM6", 115200)[0]
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
        pose = dType.GetPose(api)
        x_pose = pose[0]
        y_pose = pose[1]
        z_pose = pose[2]
        if key =='main':
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
        if key == 'up':
           dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose,z_pose+10,10,isQueued=1) 
        if key == 'down':
           dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose,z_pose-10,10,isQueued=1) 
        if key == 'right':
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose+10,z_pose,10,isQueued=1)
        if key == 'left':
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose-10,z_pose,10,isQueued=1)

    #dType.DisconnectDobot(api)
for i in range (10):
    control('up',[100,125],[100,125]) """
