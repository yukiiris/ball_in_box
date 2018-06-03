import numpy as np

# the range of X-axis and Y-axis
XRANGE = (-1, 1)
YRANGE = (-1, 1)

class Nodexy:
    x=np.float64(0)
    y=np.float64(0)
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Nodexyr:
    x=np.float64(0)
    y=np.float64(0)
    r=np.float64(0)
    def __init__(self, x, y,r):
        self.x=x
        self.y=y
        self.r=r


def xyobject_to_Nodexy(nodes):
    list_Nodexy=[]
    m=len(nodes)
    for i in range(m):
        list_Nodexy.append(Nodexy(nodes[i][0], nodes[i][1]))
    print(list_Nodexy)
    return list_Nodexy

def Nodexy_to_xyobject(nodes):
    list_=[]
    m=len(nodes)
    for i in range(m):
        list_.append((nodes[i].x,nodes[i].y))
    print(list_)
    return list_
def xyrobject_to_Nodexyr(nodes):
    list_Nodexyr=[]
    m=len(nodes)
    for i in range(m):
        list_Nodexyr.append(Nodexyr(nodes[i][0], nodes[i][1],nodes[i][2]))
    return list_Nodexyr
def Nodexyr_to_xyrobject(nodes):
    list_=[]
    m=len(nodes)
    for i in range(m):
        list_.append((nodes[i].x,nodes[i].y,nodes[i].r))
    print(list_)
    return list_

def find_proper_one_in_xyrobject_by_r(_judge,nodes):
    """
    _judge 如果judges为真 则返回最大值 如果judges为假 则返回最小值
    nodes  需要处理的list,list里面存的是(x,y,r)这样的object

    return 返回数字 即是第几个
    """
    
    m = len(nodes)
    j = 0
    list_Nodexyr = xyrobject_to_Nodexyr(nodes)
    if(_judge):
        max_nodexyr = Nodexyr(0,0,0)
        for i in range(m):
            if(list_Nodexyr[i].r>max_nodexyr.r):
                j = i
                max_nodexyr=list_Nodexyr[i]
        return j
    else:
        min_nodexyr=Nodexyr(0,0,0)
        for i in range(m):
            if(list_Nodexyr[i].r<min_nodexyr.r):
                j = i
                min_nodexyr = list_Nodexyr[i]
        return j

def three_lines_suit_circle(cross1,cross2):
    r=np.float64(0)
    x=np.float64(0)
    y=np.float64(0)
    if(cross1.x == cross2.x):
        r=abs(np.float64(cross1.y-cross2.y))
        y = np.float64(cross1.y+cross2.y)/np.float64(2)
        x = cross1.x+r
        if(x<XRANGE[0] or x>XRANGE[1]):
            x = cross1.x-r
    else:
        r = abs(np.float64(cross1.x-cross2.x))
        x = np.float64(cross1.x+cross2.x)/np.float64(2)
        y = cross1.y+r
        if(y<YRANGE[0] or y>YRANGE[1]):
            y = cross1.y-r

    circle = Nodexyr(x,y,r)
    return circle

def two_lines_one_node_suit_circle(cross1,node1):
    delta_x = np.float64(0)
    delta_y = np.float64(0)
    # if(cross1.x>0):
    #     if(cross1.y>0):
            

def sort_nodes_by_littletobig_xtoy(nodes):
    """
    该方法由左上起顺时针画圈，以经过的顺序来排序
    nodes 即blockers，多个给出的点的位置(x,y)
    m     blockers的个数

    return 排序好的list
    """

    m=len(nodes)
    nodelist=xyobject_to_Nodexy(nodes)

    #for i in range(m):
        
    return nodelist

def judge_node_with_box(nodes,m):
    """
    nodes 即blockers，多个给出的点的位置(x,y)
    m     blockers的个数

    return 返回与box交点的坐标(x,y),([-1,1],[-1,1])
    """

    #lines内数据结构 (x1,y1,x2,y2,k)
    lines=[]
    #有m个点，有m-1条线段，故循环m-1次
    for i_1 in range(m):
        if(i_1==m-1):
            k=np.float64(nodes[i_1][1]-nodes[0][1])/np.float64(nodes[i_1][0]-nodes[0][1])
            lines.append((nodes[i_1][0],nodes[i_1][1],nodes[0][0],nodes[0][1]))
        else:
            k=np.float64(nodes[i_1+1][1]-nodes[i_1][1])/np.float64(nodes[i_1+1][0],nodes[i_1][0])
            lines.append(
                    (nodes[i_1][0],nodes[i_1][1],nodes[i_1+1][0],nodes[i_1+1][1],k)
                    )

    return lines

if __name__ == '__main__':
    testlist=[(0.5,0.3),(0.3,0.5),(-0.5,0.7),(0.1,0.7),(0.8,-0.8),(-0.9,0.6)]
    testlist=xyobject_to_Nodexy(testlist)
    print(testlist)
    testlist=Nodexy_to_xyobject(testlist)
    print(testlist)


