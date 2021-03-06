#Create a mesh of curved surface grid according to the function entered
#as 'transform'

from math import *

#example transform function
def expTransform(point):
    z = point[1]
    r = 0.2 + 10.0*exp(-z)
    x = r*sin(point[0])
    y = r*cos(point[0])
    return (x, y, z)
	
#example transform function
def triple(p):
    u = p[0]
    v = p[1]
    return (3*u, v, 0)
		
def make1DVertexArray(spacing, cols, rows, colOffset, rowOffset):
	vertices = []
	du = spacing[0]
	dv = spacing[1]
	for i in range(cols):
		for j in range(rows):
			vertices.append(((i + colOffset)*du, (j + rowOffset)*dv, 0))
	return vertices

def indexOf(i, j, cols, rows):
	return (i*rows) + j
	
def makeEdgeList(vertexArray, cols, rows, subs):
	edges = []
	for i in range(cols):
		for j in range(rows):
			p0 = indexOf(i, j, cols, rows)
			if (i%subs == 0) and (j < rows - 1):
				p1 = indexOf(i, j + 1, cols, rows)
				edges.append((p0, p1))
			if (j%subs == 0) and (i < cols - 1):
				p1 = indexOf(i + 1, j, cols, rows)
				edges.append((p0, p1))
	return edges
	
def transformedVertexList(spacing, cols, rows, colOffset, rowOffset, transform):
	vertices = make1DVertexArray(spacing, cols, rows, colOffset, rowOffset)
	for i in range(len(vertices)):
		vertices[i] = transform(vertices[i])
	return vertices
	
subs = 2 #subdivisions in a grid cell - higher number gives smoother curve
cols = 3 #number of grid cells along horizontal axis
rows = 3 #number of grid cells along vertical axis
spacing = (1, 1) #vector representing dimensions of cell
colOffset = 0 #to allow values to extend into negative or start at arbitrary value
rowOffset = 0 
transform = triple #surface function of form (u, v) -> (x, y, z)

vertices = transformedVertexList(spacing, cols, rows, \
	colOffset, rowOffset, transform)
edges = makeEdgeList(vertices, cols, rows, subs)

print(str(vertices))
print(str(edges))