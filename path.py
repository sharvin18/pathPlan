import matplotlib.pyplot as plt

myBox=[[5, 2.5], [7.5, 2.5], [5.5, 4], [8, 4], [6, 5.5], [8.5, 5.5], [6.5, 7], [9,7], [6, 8.5],
       [8.5, 8.5], [5.5, 10], [8, 10], [5.1, 11.5], [7.6, 11.5], [5, 13], [7.5, 13]]

#Co-ordinates with steep turns
#testing git
#myBox=[[5, 2.5], [7.5, 2.5], [6.5, 4], [9, 4], [8, 5.5], [10.5, 5.5], [5, 7.5], [7.5, 7.5], 
#        [4.5, 9], [7, 9], [7.5, 11], [10, 11], [8, 12.5], [10.5, 12.5], [8, 14], [10.5, 14]]

lBox = [[5, 1]] #first left cone
rBox = [[7.5, 1]] #first right cone
l = []
r = []
lx = []
ly = []
rx = []
ry = []

def pathPlan():
    
    j=0
    for i in range(int(len(myBox)/2)):
        #print(i)
        #print(j)
        #print(str(lBox))
        #print(str(rBox))
        #print("mybox[i][1]=", myBox)
    
        # in case of a straight path: compare x co-ordinate of left cone of previous iteration with x co-ordinate of input cones
        if myBox[j][0] > (lBox[i][0]-0.3) and myBox[j][0] < (lBox[i][0] +0.3):
            lBox.append(myBox[j])
            rBox.append(myBox[j+1])
            
        elif myBox[j+1][0] > (lBox[i][0] - 0.3) and myBox[j+1][0] < (lBox[i][0] + 0.3):
            lBox.append(myBox[j+1])
            rBox.append(myBox[j])
            
        else:
            # if the path is curved then find slope
            l1 = (myBox[j][1] - lBox[i][1])/(myBox[j][0] - lBox[i][0])
            l2 = (myBox[j+1][1] - lBox[i][1])/(myBox[j+1][0] - lBox[i][0])

            r1 = (myBox[j][1] - rBox[i][1])/(myBox[j][0] - rBox[i][0])
            r2 = (myBox[j+1][1] - rBox[i][1])/(myBox[j+1][0] - rBox[i][0])

            # in case of left curve: compare the slopes of previous left cone to new pair of cones
            if l1 < 0 and l2 > 0:
                lBox.append(myBox[j])
                rBox.append(myBox[j+1])
                
            elif l1 > 0 and l2 < 0:
                lBox.append(myBox[j+1])
                rBox.append(myBox[j])
            
            elif l1 < 0 and l2 < 0 and r1 < 0 and r2 < 0:    #incase of steep left curve
                if l2<l1:
                    lBox.append(myBox[j])
                    rBox.append(myBox[j+1])
                elif l1<l2:
                    lBox.append(myBox[j+1])
                    rBox.append(myBox[j])

            # in case of Right curve: compare the slopes of previous Right cone to input
            if r1 < 0 and r2 > 0:
                lBox.append(myBox[j])
                rBox.append(myBox[j+1])
                
            elif r1 > 0 and r2 < 0 :
                lBox.append(myBox[j+1])
                rBox.append(myBox[j])

            elif l1 > 0 and l2 > 0 and r1 > 0 and r2 > 0:
                if r2<r1:
                    lBox.append(myBox[j])
                    rBox.append(myBox[j+1])
                elif r1<r2:
                    lBox.append(myBox[j+1])
                    rBox.append(myBox[j])
                
        j += 2
 
    for i in lBox:
        lx.append(i[0])
        ly.append(i[1])
    for i in range(len(lx)):
        plt.scatter(float(lx[i]), float(ly[i]), label="stars", color="blue", marker="1", s=30)
        plt.xlim(0, 15)
        plt.ylim(0, 15)

    for i in rBox:
        rx.append(i[0])
        ry.append(i[1])
    for i in range(len(rx)):
        plt.scatter(float(rx[i]), float(ry[i]), label="stars", color="green", marker="1", s=30)
        plt.xlim(0, 15)
        plt.ylim(0, 15)


    print("Left cones: " + str(lBox))
    print("Right cones: " + str(rBox))
    left=list(zip(*lBox))
    right=list(zip(*rBox))
    plt.plot(left[0],left[1], color="blue")
    plt.plot(right[0],right[1], color="green")
    plt.show()

    l.clear()
    r.clear()
    l.append(lBox[-1])
    r.append(rBox[-1])
    #print(str(l))
    #print(str(r))
    
    lBox.clear()
    rBox.clear()
    lx.clear()
    ly.clear()
    rx.clear()
    ry.clear()

pathPlan()
