
def pathPlan():
    #top view coordinates of previous pair of cones
    xLeft1 = 10
    yLeft1 = 10
    xRight1 = 20
    yRight1 = 10
    # (xLeft1,yLeft1) = (10,10) and (xRight1, yRight1) = (20,10) are left and right cones of the previous iteration respectively

    #inputs for straight path
    xLeft2 = 10
    yLeft2 = 30
    xRight2 = 20
    yRight2 = 30

    #inputs for right curved path
    #xLeft2 = 15
    #yLeft2 = 20
    #xRight2 = 25
    #yRight2 = 20

    #inputs for left curved path
    #xLeft2 = 5
    #yLeft2 = 20
    #xRight2 = 15
    #yRight2 = 20

    # in case of a straight path: compare x co-ordinate of left cone of previous iteration with x co-ordinate of input cones
    if xLeft2 > (xLeft1-2) and xLeft2 < (xLeft1 +2):
            print(str(xLeft2) + "," + str(yLeft2) + " = Left cone")
            print(str(xRight2) + "," + str(yRight2) + " = Right cone")
    elif xRight2 > (xLeft1 - 2) and xRight2 < (xLeft1 + 2):
            print(str(xRight2) + "," + str(yRight2) + " = Left cone")
            print(str(xLeft2) + "," + str(yLeft2) + " = Right cone")
    else:
        # if the path is curved then find slope
        l1 = (yLeft2 - yLeft1)/(xLeft2 - xLeft1)
        l2 = (yRight2 - yLeft1)/(xRight2 - xLeft1)

        r2 = (yRight2 - yRight1)/(xRight2 - xRight1)
        r1 = (yLeft2 - yRight1)/(xLeft2 - xRight1)

        # in case of left curve: compare the slopes of previous left cone to new pair of cones
        if l1 < 0 and l2 > 0:
            print(str(xLeft2) + "," + str(yLeft2) + " = Left cone")
            print(str(xRight2) + "," + str(yRight2) + " = Right cone")
        elif l1 > 0 and l2 < 0:
            print(str(xRight2) + "," + str(yRight2) + " = Left cone")
            print(str(xLeft1) + "," + str(yLeft1) + " = Right cone")

        # in case of Right curve: compare the slopes of previous Right cone to input
        if r1 < 0 and r2 > 0:
            print(str(xLeft2) + "," + str(yLeft2) + " = Left cone")
            print(str(xRight2) + "," + str(yRight2) + " = Right cone")
        elif r1 > 0 and r2 < 0 :
            print(str(xLeft2) + "," + str(yLeft2) + " = Right cone")
            print(str(xRight2) + "," + str(yRight2) + " = Left cone")
