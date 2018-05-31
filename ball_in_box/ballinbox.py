import math
import random
from .validate import validate

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    m规定了数量，最终圆个数一定要等于m
    blockers is the list of coordinates of tiny blocks.
    blockers是一些点，没有大小，只是我们的圆不能穿过它们
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    # circles = []
    # for circle_index in range(m):

    #     x = random.random()*2 - 1
    #     print(x)
    #     y = random.random()*2 - 1
    #     print(y)
    #     r = random.random()*0.1
    #     print(r)

    #     circles.append((x, y, r))
    #     while not validate(circles, blockers):
    #         x = random.random()*2 - 1
    #         y = random.random()*2 - 1
    #         r = random.random()*0.1
    #         circles[circle_index] = (x, y, r)

    #     circle_index += 1
    
    # n是对应的blockers里面的blocker的个数
    n=blockers.length()
    # circles是最终该算法得到的圆的集合
    # circle的格式为（x,y,r)
    circles=[]
    
    return circles
