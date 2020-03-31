#REM Python console: blank lines terminate function definition

from math import *

def expTransform(point):
    z = point[1]
    r = 0.2 + 10.0*exp(-z)
    x = r*sin(point[0])
    y = r*cos(point[0])
    return (x, y, z)

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
	
subs = 2
cols = 3
rows = 3
spacing = (1, 1)
colOffset = 0
rowOffset = 0
transform = triple

vertices = transformedVertexList(spacing, cols, rows, \
	colOffset, rowOffset, transform)
edges = makeEdgeList(vertices, cols, rows, subs)

print(str(vertices))