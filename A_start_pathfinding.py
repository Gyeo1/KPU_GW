from time import time

class Node:
    def __init__(self, coordi, state):
        self.coordi = coordi
        self.parent = None
        self.state = state
        self.g_val = 0
        self.h_val = 0
        self.f_val = 0
    def getHval(self, goal):
        if self.h_val != 0: #h값이 0== 현재 노드와 goal노드와의 거리가 0이면 함수 종료
            return
        #현재 노드, 목표 노드의 거리를 측정
        x_differ = abs(self.coordi[1] - goal[1])
        y_differ = abs(self.coordi[0] - goal[0])

        #최종 h값을 정함.
        self.h_val += min([x_differ, y_differ]) * 14
        self.h_val += abs(x_differ - y_differ) * 10
        
        
    
class searchNode: #노드를 찾는 클래스 시작점,끝점을 받아온다.
    def __init__(self, start, goal): #start:시작점 , goal:목적지
        self.map = []
        self.openList = []
        self.start = start
        self.goal = goal
        self.success = False
        
    def doMove(self):
        while not self.success:
            coordi = self.openList.pop(0) #오픈리스트에서 값을 빼옴.
            cur_node = self.map[coordi[0]][coordi[1]] #현재노드 = map에서 coordi의 좌표에 해당하는 부분.
            
            if coordi[0] != 0 and self.checkState([coordi[0] - 1, coordi[1]], cur_node.g_val):
                x = coordi[1]
                y = coordi[0] - 1
                
                self.map[y][x].state = '2'#2의값은 한번지나갔다는 의미(evaluate했다)
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            
            if coordi[0] != 0 and coordi[1] != 199 and self.checkState([coordi[0] - 1, coordi[1] + 1], cur_node.g_val):
                x = coordi[1] + 1
                y = coordi[0] - 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].g_val + self.map[y][x].h_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[1] != 199 and self.checkState([coordi[0], coordi[1] + 1], cur_node.g_val):
                x = coordi[1] + 1
                y = coordi[0]
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].g_val + self.map[y][x].h_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 199 and coordi[1] != 199 and self.checkState([coordi[0] + 1, coordi[1] + 1], cur_node.g_val):
                x = coordi[1] + 1
                y = coordi[0] + 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].g_val + self.map[y][x].h_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 199 and self.checkState([coordi[0] + 1, coordi[1]], cur_node.g_val):
                x = coordi[1]
                y = coordi[0] +1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 199 and coordi[1] != 0 and self.checkState([coordi[0] + 1, coordi[1] - 1], cur_node.g_val):
                x = coordi[1] - 1
                y = coordi[0] + 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[1] != 0 and self.checkState([coordi[0], coordi[1] - 1], cur_node.g_val):
                x = coordi[1] - 1
                y = coordi[0]
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 10
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
            if coordi[0] != 0 and coordi[1] != 0 and self.checkState([coordi[0] - 1, coordi[1] - 1], cur_node.g_val):
                x = coordi[1] - 1
                y - coordi[0] - 1
                
                self.map[y][x].state = '2'
                self.map[y][x].g_val = cur_node.g_val + 14
                self.map[y][x].getHval(self.goal)
                self.map[y][x].f_val = self.map[y][x].h_val + self.map[y][x].g_val
                self.map[y][x].parent = cur_node
                if [y, x] == self.goal:
                    self.success = True
                self.insert([y, x])
                
        self.printMap()
            
                
                
            
    def  checkState(self, coordi, value):#checkState란
        if coordi[0] in range(200) and coordi[1] in range(200):
            if self.map[coordi[0]][coordi[1]].state == '1':
                return False
        
            elif self.map[coordi[0]][coordi[1]].state == '2':
                if value + 14 > self.map[coordi[0]][coordi[1]].g_val:
                    return False
                
        if coordi in self.openList:
            self.openList.remove(coordi)
        return True 
            
    
    
    def getMap(self, filename):
        j = 0
        state = []
        row = []
        
        f = open(filename)
        lines = f.readlines()
        for line in lines:
            state.append(line.split(','))
            for i in range(len(state[j])):
                if i < 199:
                    row.append(Node([j, i], state[j][i]))
                else:
                    a = state[j][i].split('\n')#\n즉 줄바꿈 문자를 기준으로 분할
                    row.append(Node([j, i], a[0]))
            self.map.append(row)
            row = []
            j += 1
                           
                
    def insert(self, coordi):
        if len(self.openList) == 0:
            self.openList.append(coordi)
        else:
            self.openList.append(coordi)
            m = len(self.openList) - 1
            while m != 0:
                if self.map[coordi[0]][coordi[1]].f_val <= self.map[self.openList[int(m/2)][0]][self.openList[int(m/2)][1]].f_val: 
                    temp = self.openList[int(m/2)]
                    self.openList[int(m/2)] = self.openList[m]
                    self.openList[m] = temp
                    m = int(m/2)
                else:
                    break
        
        
    def makeRoot(self):
        root = self.map[0][0]
        root.getHval(self.goal)
        root.f_val = root.h_val
        self.insert(root.coordi)
        self.map[0][0].state = '2'
        
    
    def search(self):
        self.makeRoot()
        self.doMove()
        
        
    def printMap(self):
        node = self.map[self.goal[0]][self.goal[1]]        
        while node != None:
            node.state = '9'
            node = node.parent
            
        row = ""
        f = open("result.txt", 'w')
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                row += str(self.map[i][j].state)
            f.write(row)
            f.write('\n')
            row = ""
        


if __name__ == "__main__":
    start = [45,69]
    goal = [182,108]
    
    t = time()
    astar = searchNode(start, goal)
    astar.getMap("ExtendedMap.txt")
    astar.search()
    
    print (str(time() - t) + " secs")