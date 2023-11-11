import numpy as np
def distance(pointA, pointB=(0, 0), metric='taxi'):
    """
    Return distance in city blocks between points A, and B.
    If metric is 'taxi' (or omitted), use taxicab metric.
    Otherwise, use Euclidean distance
        pointA = (x1, y1)
        pointB = (x2, y2)
    If pointB is omitted, use the origin.
    """
    if metric == 'taxi':
        interval = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
    else:
        interval = np.sqrt( (pointB[0] - pointA[0])**2 \
                            + (pointB[1] - pointA[1])**2 )
    
    return interval

def taxicab(pointA, pointB):
    """
    Taxicab metric for computing distance between points A and B.
        pointA = (x1, y1)
        pointB = (x2, y2)
    Returns |x2-x1| + |y2-y1|.  Distances are measured in city blocks.
    """
    interval = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
    return interval


def dist_between_points_3d(pointA, pointB):
    """
    Computes the distance between two points in three-dimensional space.
        pointA: (x1, y1, z1)
        pointB: (x2, y2, z2)
    Returns |x2 - x1| + |y2 - y1| + |z2 - z1|
    """
    x1, y1, z1 = pointA[0], pointA[1], pointA[2]
    x2, y2, z2 = pointB[0], pointB[1], pointB[2]
    distance = abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
    return distance