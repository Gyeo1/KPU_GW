class Node:
    def __init__(self,parent=None,position=None):
        self.parent=parent
        self.position=position

        self.g=0
        self.h=0
        self.f=0
    def __eq__(self,other):
        return self.position==other.position

def heuristic(node, goal, D=1, D2=2 ** 0.5):  # Diagonal Distance로 휴리스틱 값을 구하는 함수!
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])
   # return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    return D * (dx + dy)
def aStar(maze,start,end):
    startNode=Node(None,start)
    endNode=Node(None,end)

    openList=[]
    closedList=[]

    openList.append(startNode)

    while openList:
        currentNode=openList[0]
        currentIdx=0

        for index, item in enumerate(openList):
            if item.f<currentNode.f:
                currentNode=item
                currentIdx=index
        openList.pop(currentIdx)
        closedList.append(currentNode)

        if currentNode==endNode:
            path=[]
            current=currentNode
            while current is not None:
                path.append(current.position)
                current=current.parent
            return path[::-1]
        children=[]
        for newPosition in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            nodePosition=(
                currentNode.position[0]+newPosition[0], #X축
                currentNode.position[1]+newPosition[1] #Y축

            )
            within_range_criteria=[
                nodePosition[0]>(len(maze)-1),
                nodePosition[0]<0,
                nodePosition[1]>(len(maze[len(maze)-1])-1),
                nodePosition[1]<0,
            ]

            if any(within_range_criteria):
                continue

            if maze[nodePosition[0]][nodePosition[1]]!=0:
                continue
            new_node=Node(currentNode,nodePosition)
            children.append(new_node)

        for child in children:
            if child in closedList:
                continue
            child.g=currentNode.g+1
            #child.h=((child.position[0]-endNode.position[0])**2)+((child.position[1]-endNode.position[1])**2)
            child.h=heuristic(child,endNode)
            child.f=child.g+child.h

            if len([openNode for openNode in openList
                    if child == openNode and child.g > openNode.g]) > 0:
                continue

            openList.append(child)


def main():
    # 1은 장애물
    maze1=[]
    f=open("Map.txt")

    lines=f.readlines()#readlines는 파일의 모든 줄을 읽어온다.
    #print(lines)
    for line in lines:
        a=line.split(',') #각 줄을 ,를 기주으로 나눈게 a임
        b=list(map(int,a))
     #   print(b) #list(map(int,a))는 리스트의 문자열을 int형으로 바꾸는것.
        maze1.append(b)


    #print(lines)
    #print(maze1)
    f = open("result.txt", 'w')
    row=""
    for i in range(10):
        for j in range(11):
            row+=str(maze1[i][j])
        f.write(row)
        f.write("\n")
        row=""


    start = (0, 0)#(x축,y축)
    end = (0,3)

    path = aStar(maze1, start, end)
    print(path)
    an=[]
    #print(len(path))
    for i in range(len(path)):
        for j in range(2):
            an.append(path[i][j])
    print(an)
    for i in range(0,len(an),2):
        print(i)
        #maze1[an[i]][an[i+1]]


if __name__ == '__main__':
    main()
