def areCollinear(p1, p2, p3):
    slope1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
    if slope1 == slope2:
        print "Points are colinear"
    else:
        print "Points are NOT colinear, what's the matter with you?"

areCollinear((5,5), (0,0), (-5,-5))
