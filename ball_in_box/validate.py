import math


def validate(circles, blockers):
    """
    该函数用来判断所计算出来的结果是否能放到容器中，不要改，看懂就行
    circles 计算所得的圆圈的元组
    blockers 圆中的小障碍

    return true or false 返回布尔值
    """
    for circle in circles:
        #圆左边界x坐标
        xmr = circle[0] - circle[2]
        #圆右边界坐标
        xpr = circle[0] + circle[2]
        #圆左边界y坐标
        ymr = circle[1] - circle[2]
        #y圆右边界坐标
        ypr = circle[1] + circle[2]

        #检测圆是否在【-1，1】之间
        if (not (xmr <= 1 and xmr >=-1 )) \
           or (not (xpr <= 1 and xpr >=-1 )) \
           or (not (ymr <= 1 and ymr >=-1 )) \
           or (not (ypr <= 1 and ypr >=-1 )):
            return False

    # Is circle good for blockers?
    if blockers is not None and len(blockers) > 0:
        for circle in circles:
            for block in blockers:
                x = circle[0]
                y = circle[1]
                r = circle[2]
                bx = block[0]
                by = block[1]
                # 只要block即该点在所有的圆外，就说明ok
                if math.sqrt((x - bx)**2 + (y - by)**2) < r:
                    return False

    # 确保圆之间没有相交
    # Is circle good for each other?
    for circle1 in circles:
        for circle2 in circles:
            x1 = circle1[0]
            y1 = circle1[0]
            r1 = circle1[0]
            x2 = circle2[0]
            y2 = circle2[0]
            r2 = circle2[0]
            # 如果两个圆心距离小于半径和，即相交，可以相切不能相交
            if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) < (r1 + r2):
                return False

    # all good
    return True
