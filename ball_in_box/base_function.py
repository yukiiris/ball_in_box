

class Nodexy:
    x=float(0)
    y=float(0)
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Nodexyr:
    x=float(0)
    y=float(0)
    r=float(0)
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

def find_proper_one_in_xyrobject(_judge,x_or_y,nodes):
    """
    _judge 如果judges为真 则返回最大值 反之返回最小值
    x_or_y 如果为真，则根据object中x大小排序，反之根据y大小排序
    nodes  需要处理的list,list里面存的是(x,y,r)这样的object

    return 返回数字 即是第几个
    """
    m=len(nodes)
    max_nodexyr=Nodexyr(0,0,0)




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
            k=float(nodes[i_1][1]-nodes[0][1])/float(nodes[i_1][0]-nodes[0][1])
            lines.append((nodes[i_1][0],nodes[i_1][1],nodes[0][0],nodes[0][1]))
        else:
            k=float(nodes[i_1+1][1]-nodes[i_1][1])/float(nodes[i_1+1][0],nodes[i_1][0])
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


