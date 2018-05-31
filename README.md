# ball_in_box


conda  env create --file environment.yml

conda install --file requirements.txt -y

pip install -e .

**编程要求**
* 我们只需要修改*ballinbox.py*里面的ball_in_box函数
* 实现的算法如下
```
在一个二维平面2x2
里面有小方块的blocker
我们需要在剩余的空间内放置圆圈
使得最终r^2*PI最大
即尽量填满能放置的空间
```




**以下是老师给的要求**
**coded in utf-8**
```
要求：
1. 同学们的项目地址是github.com/XXX/ball_in_box
2. 至少有两个文件github.com/XXX/ball_in_box/ball_in_box/__init__.py 
github.com/XXX/ball_in_box/ball_in_box/ballinbox.py 
3. ballinbox.py中有ball_in_box函数
4. ball_in_box函数有对应的输入和输出。


In a box bounded by [-1, 1], given m balloons(they cannot overlap) with variable radio r and position mu. And some tiny blocks are in the box at given position {d}; balloons cannot overlap with these blocks. find the optimal value of r and mu which maximizes 
sum r^2*PI
```

