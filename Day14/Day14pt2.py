import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

f = open("input.txt", "r")
lines = f.read().split("\n")

robots = []
w = 101
h = 103

def inRange(x,y):
    if x < 0:
        x = w + x
    elif x >= w:
        x = x - w
    else:
        x = x
    if y < 0:
        y = h + y
    elif y >= h:
        y = y - h
    else:
        y = y
        
    return x,y

def move(v,p):
    vx,vy = v
    x,y = p
    px,py = x+vx,y+vy
    p = inRange(px,py)  
    return(p) 

def inquad(x,y):
    if x == int(w/2) or y == int(h/2):
        return "ignore"
    else:
     if x < int(w/2):
        if y < int(h/2):
            return "q1"
        else:
            return "q3"
     elif x > int(w/2):
         if y < int(h/2):
             return "q2"
         else:
             return "q4"
             
def countguards(bots):
    quad = {}
    for b in bots:
        x = b[1][0]
        y = b[1][1]
        key = inquad(x,y)
        if key not in quad:
            quad[key] = 1
        else:
            quad[key] += 1
    return quad
        
        
def result(robots):
    quads = countguards(robots)
    tot = 1
    for k,v in quads.items():
      if k != "ignore":
        tot = tot * v
    return tot

for line in lines:
    line = line.split(" ")
    line = [i.split("=") for i in line]
    line = [i[1].split(",") for i in line]
    p = [int(line[0][0]),int(line[0][1])]
    v = [int(line[1][0]),int(line[1][1])]
    robots.append([v,p])

stopped = False  
secs = 0
def onClick(event):
    global secs
    xps = []
    yps = []
    show = False
    while not show:
      xps = []
      yps = []
      for n,v in enumerate(robots):
         p = move(v[0],v[1])
         robots[n][1] = p
         xps.append(p[0])
         yps.append(p[1])
      secs += 1
      if (secs - 86) % 103 == 0 or (secs - 28)% 101 == 0:
        show = True
      
    plt.cla()
    xpoints = np.array(xps)
    ypoints = np.array(yps)
    plt.plot(xpoints, ypoints, 'o',alpha=0.25,mec="green",mew=0,mfc="green",ms=5)
    title = "secs: " + str(secs)
    plt.title(title)
    plt.draw()
  

xps = []
yps = []
for n,v in enumerate(robots):
    z,p = v
    xps.append(p[0])
    yps.append(p[1])
xpoints = np.array(xps)
ypoints = np.array(yps)

fig, ax = plt.subplots()
plt.title("title")
plot2 = ax.plot(xpoints,ypoints, 'o',alpha=0.25,mec="green",mew=0,mfc="green",ms=5)[0]
sec_text = ax.text(.5, .5, '0s', fontsize=15)
ax.set(xlim=[0, 101], ylim=[0, 103], xlabel='', ylabel='')
ax.legend()

def update(frame):
    global secs
    show = False
    while not show:
      xps = []
      yps = []
      for n,v in enumerate(robots):
         p = move(v[0],v[1])
         robots[n][1] = p
         xps.append(p[0])
         yps.append(p[1])
      secs += 1
      if (secs - 86) % 103 == 0 or (secs - 28)% 101 == 0:
        show = True
    
    title = str(secs) + "s"
    sec_text.set_text(title)
    plt.title(title)
    plot2.set_xdata(xps)
    plot2.set_ydata(yps)
    return (plot2)

ani = animation.FuncAnimation(fig=fig, func=update, frames=146, repeat=False,interval=30)
plt.show()

f.close()