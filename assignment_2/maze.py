#Assignment 2
import sys
import copy
from typing import Any

class MazeError(Exception):
    def __init__(self,error_massage):
        self.error_massage = error_massage
    def __str__(self):
        return self.error_massage

class Maze():
    def __init__(self,file_name):
        with open(file_name) as self.file:
            content=self.file.read()
        self.temp_list_content = []
        list_line = content.splitlines()
        for i in list_line:
            i = i.rstrip().replace(' ','')
            if i != '':
                self.temp_list_content.append(list(i))
        self.list_content = copy.deepcopy(self.temp_list_content)
        for y in range(len(self.temp_list_content)):
            for x in range(len(self.temp_list_content[0])):
                if self.list_content[y][x].isdigit():
                    self.list_content[y][x] = int(self.temp_list_content[y][x])
        #print(self.temp_list_content)
        #print(self.list_content)
        num_row=len(self.list_content)
        num_column=len(self.list_content[0])
        if num_row > 41 or num_row < 2:
            raise MazeError('Incorrect input.')
        if num_column > 31 or num_column < 2:
            raise MazeError('Incorrect input.')
        for i in range(num_row):
            if len(self.list_content[i])!=num_column:
                raise MazeError('Incorrect input.')
            for j in range(num_column):
                if self.list_content[i][j]==0:
                    continue
                if self.list_content[i][j]==1:
                    continue
                if self.list_content[i][j] == 2:
                    continue
                if self.list_content[i][j] == 3:
                    continue
                else:
                    raise MazeError('Incorrect input.')
        for i in range(num_row):
            for j in range(num_column):
                if self.list_content[-1][j] in (2,3):
                    raise MazeError('Input does not represent a maze.')
                if self.list_content[i][-1] in (1,3):
                    raise MazeError('Input does not represent a maze.')
        for i in range(num_row):
            if len(self.list_content[i])!=num_column:
                raise MazeError('Incorrect input')

        self.maze_map=[]
        self.colour=0
        self.original_graph=[]
        self.gate=0
        self.gate_position=[]
        self.whole_wall=[]#所有走过的路径===不需要
        self.inner_point={}
        self.number_inner_point=0
        self.area=[]
        self.access_area=[]
        self.number_access_area=0
        self.path=[]
        self.colour_area={}
        self.inaccessible_colour=0
        self.number_cul_de_sace=0
        #self.cul_de_sace_position={}
        self.pillar = []
        self.number_cross_area = []#画×的
        self.path_position={}
        self.number_path = 0
        self.number_colour_gate={}

    #def print_maze(self):
        #for _ in self.list_content:
            #print(_)

    def map_of_maze(self):
        list_content=self.list_content
        num_row=len(list_content)
        num_colunm=len(list_content[0])
        maze_map=[[0 for i in range(num_colunm*2-1)]for j in range(num_row*2-1)]
        #print(self.maze_map)
        for i in range(num_row):
            for j in range(num_colunm):
                if list_content[i][j]==0:
                    continue
                elif list_content[i][j]==1:
                    maze_map[i*2][j*2]=1
                    maze_map[i*2][j*2+1] = 1
                    maze_map[i*2][j*2+2] = 1
                elif list_content[i][j]==2:
                    maze_map[i*2][j*2]=1
                    maze_map[i*2+1][j*2]=1
                    maze_map[i*2+2][j*2] = 1
                elif list_content[i][j]==3:
                    maze_map[i*2][j*2] = 1
                    maze_map[i*2+1][j*2] = 1
                    maze_map[i*2+2][j*2] = 1
                    maze_map[i*2][j*2+1] = 1
                    maze_map[i*2][j*2+2] = 1
        self.original_graph=copy.deepcopy(maze_map)
        self.maze_map=maze_map
        #print(self.maze_map)
        #print(self.original_graph)

    def colour_shapes(self):
        num_row=len(self.maze_map)
        num_column=len(self.maze_map[0])
        colour=1
        for i in range(num_row):
            for j in range(num_column):
                if self.maze_map[i][j]==1:
                    colour += 1
                    self.find_continuous_one(i,j,colour)
                    self.whole_wall.append([i,j])
        self.colour=colour
        #print(self.colour)


    def find_continuous_one(self,i, j, colour):
        self.maze_map[i][j] = colour
        num_row = len(self.maze_map)
        num_column = len(self.maze_map[0])
        if i - 1 >= 0 and self.maze_map[i - 1][j] == 1:
            self.find_continuous_one(i - 1, j, colour)
        if i + 1 < num_row and self.maze_map[i + 1][j] == 1:
            self.find_continuous_one(i + 1, j, colour)
        if j - 1 >= 0 and self.maze_map[i][j - 1] == 1:
            self.find_continuous_one(i, j - 1, colour)
        if j + 1 < num_column and self.maze_map[i][j + 1] == 1:
            self.find_continuous_one(i, j + 1, colour)

    def find_gate(self):
        num_row = len(self.maze_map)
        num_column = len(self.maze_map[0])
        for i in range(num_row):
            if i ==0 or i==num_row-1:
                for j in range(num_column):
                    if j%2==1 and self.maze_map[i][j]==0:
                        self.gate += 1
                        self.gate_position.append([i,j])
            for j in (0,num_column-1):
                if i%2==1 and self.maze_map[i][j]==0:
                    self.gate += 1
                    self.gate_position.append([i,j])
        #print(self.gate,self.gate_position)

    def find_set_of_walls(self):
         self.colour-=1
         #print(self.colour)

    def find_inaccessible_inner_points(self):
        #print(self.maze_map)
        #print(self.original_graph)
        num_row=len(self.original_graph)
        num_column=len(self.original_graph[0])
        inaccessible_colour=2
        for i in range(num_row):
            for j in range(num_column):
                if self.original_graph[i][j]==0:
                    self.inner_point[inaccessible_colour]=0
                    self.find_continuous_zero(i,j,inaccessible_colour)
                    self.colour_area[inaccessible_colour]=self.area
                    inaccessible_colour += 1
                    self.inaccessible_colour=inaccessible_colour
                    self.area=[]
        #print(self.inner_point)
        for i in range(num_row):
            for j in range(num_column):
                if i==0 and self.original_graph[i][j]!=1:
                    if [i,j] in self.gate_position:
                        if self.original_graph[i][j] in self.inner_point:
                            del self.inner_point[self.original_graph[i][j]]
                        #print(self.inner_point)
                if i==num_row-1 and self.original_graph[i][j]!=1:
                    if [i,j] in self.gate_position:
                        if self.original_graph[i][j] in self.inner_point:
                            del self.inner_point[self.original_graph[i][j]]
                if j==0 and self.original_graph[i][j]!=1:
                    if [i,j] in self.gate_position:
                        if self.original_graph[i][j] in self.inner_point:
                            del self.inner_point[self.original_graph[i][j]]
                if j==num_column-1 and self.original_graph[i][j]!=1:
                    if [i,j] in self.gate_position:
                        if self.original_graph[i][j] in self.inner_point:
                            del self.inner_point[self.original_graph[i][j]]
        list_tem=self.inner_point.values()
        #print(self.inner_point)
        for i in list_tem:# self.inner_point={2:3,3:1,4:3}
            if i>1:
                i=i//2 +1
                self.number_inner_point = self.number_inner_point + i
            else:
                self.number_inner_point = self.number_inner_point + i
        for key in self.inner_point:
            del self.colour_area[key]#除封
        #print(self.original_graph)
        #print(self.inner_point,self.number_inner_point)
        #print(self.colour_area)


    def find_continuous_zero(self,i, j, colour):
        self.inner_point[colour]=self.inner_point[colour]+1
        self.area.append([i,j])
        self.original_graph[i][j] = colour
        num_row = len(self.original_graph)
        num_column = len(self.original_graph[0])
        if i - 1 >= 0 and self.original_graph[i - 1][j] == 0:
            self.find_continuous_zero(i - 1, j,colour)
        if i + 1 < num_row and self.original_graph[i + 1][j] == 0:
            self.find_continuous_zero(i + 1, j,colour)
        if j - 1 >= 0 and self.original_graph[i][j - 1] == 0:
            self.find_continuous_zero(i, j - 1,colour)
        if j + 1 < num_column and self.original_graph[i][j + 1] == 0:
            self.find_continuous_zero(i, j + 1,colour)



    def find_accessible_areas(self):
        list_key=self.colour_area.keys()
        self.number_access_area=len(list_key)
        #print(self.number_access_area)


    def find_cul_de_sacs(self):
        #print(self.original_graph)
        num_row = len(self.original_graph)
        num_column = len(self.original_graph[0])
        dict_colour = {}
        dict_prevent_repeat={}
        #print(self.inaccessible_colour)
        for i in range(2, self.inaccessible_colour ):
            dict_colour[i] = 0
            dict_prevent_repeat[i]=0
        #print(self.colour_area.keys())
        #print(dict_colour)
        #print(dict_prevent_repeat)
        for n in range(num_row):
            for m in range(num_column):
                if self.original_graph[n][m] != 1:
                    if self.find_neighbor(n, m):
                        dict_colour[self.original_graph[n][m]]=[n,m]
                        dict_prevent_repeat[self.original_graph[n][m]]+=1
        #print(dict_colour)
        #print(dict_prevent_repeat)
        for key in dict_prevent_repeat:
            if dict_prevent_repeat[key]!=0:
                self.number_cul_de_sace += 1
        #print(self.number_cul_de_sace)
        number_gate = 0
        dict_num_gate = {}
        for key in self.colour_area:
            list_temp = self.colour_area[key]
            number_gate = 0
            for i in list_temp:
                if i in self.gate_position:
                    number_gate += 1
            dict_num_gate[key] = number_gate
        #print(dict_num_gate)
        for key in dict_num_gate:
            if dict_num_gate[key] == 1:  # 只有一个门的时候
                list_tem=self.colour_area[key]
                for i in self.colour_area[key]:
                    self.number_cross_area.append(i)
        #print(self.number_cross_area)
            elif dict_prevent_repeat[key]!=0 and dict_num_gate[key]!=1:
                spike=dict_colour[key]
                self.number_cross_area.append(spike)
                while True:
                    if self.find_spike_neighbor(key,spike):
                        spike=self.find_spike_neighbor(key,spike)
                    if self.find_neighbor_cross(spike[0],spike[-1]):
                       self.number_cross_area.append(spike)
                    break#至此，所有要画×的坐标找齐了
        self.number_colour_gate=dict_num_gate
        #print(self.number_cross_area)

    def find_spike_neighbor(self,colour_key,spike):#spike是[2,3]
        num_row=len(self.original_graph)
        num_column=len(self.original_graph[0])
        if spike[0] - 1 >= 0 and self.original_graph[spike[0] - 1][spike[-1]] == colour_key:
            return [spike[0] - 1,spike[-1]]
        if spike[0] + 1 < num_row and self.original_graph[spike[0] + 1][spike[-1]] == colour_key:
            return [spike[0] + 1, spike[-1]]
        if spike[-1] - 1 >= 0 and self.original_graph[spike[0]][spike[-1] - 1] == colour_key:
            return [spike[0],spike[-1] - 1]
        if spike[-1] + 1 < num_column and self.original_graph[spike[0]][spike[-1] + 1] ==colour_key:
            return [spike[0],spike[-1] + 1]

    def find_neighbor(self,i, j):#找spike的
        num_row = len(self.original_graph)
        num_column = len(self.original_graph[0])
        num_around = 0
        if i - 1 >= 0 and self.original_graph[i - 1][j] == 1:  # ahead
            num_around += 1
        if i + 1 < num_row and self.original_graph[i + 1][j] == 1:  # under
            num_around += 1
        if j - 1 >= 0 and self.original_graph[i][j - 1] == 1:  # left
            num_around += 1
        if j + 1 < num_column and self.original_graph[i][j + 1] == 1:  # right
            num_around += 1
        if num_around == 3:
            return num_around
        else:
            return False

    def find_neighbor_cross(self,i, j):#找 × 的:从spike开始周围保证2个1，一旦有3个1立马停止
        num_row = len(self.original_graph)
        num_column = len(self.original_graph[0])
        num_around = 0
        if i - 1 >= 0 and self.original_graph[i - 1][j] == 1:  # ahead
            num_around += 1
        if i + 1 < num_row and self.original_graph[i + 1][j] == 1:  # under
            num_around += 1
        if j - 1 >= 0 and self.original_graph[i][j - 1] == 1:  # left
            num_around += 1
        if j + 1 < num_column and self.original_graph[i][j + 1] == 1:  # right
            num_around += 1
        if num_around >=2:
            return [i,j]
        else:
            return False

    def find_pillar(self):
        num_row=len(self.list_content)
        num_colunm=len(self.list_content[0])
        for i in range(num_row):
            for j in range(num_colunm):
                if self.list_content[i][j]==0:
                    if i-1>=0 and self.list_content[i-1][j]!=2 and self.list_content[i-1][j]!=3:
                        if j-1>=0 and self.list_content[i-1][j]!=1 and self.list_content[i-1][j]!=3:
                            self.pillar.append([i*2,j*2])
        #print(self.pillar)

    def find_unique_path(self):
        for key in self.colour_area:
            for i in self.colour_area[key]:
                if i not in self.number_cross_area:
                    if i not in self.pillar:
                        self.path.append(i)#[[1,2],[3,4]]
        num_row=len(self.original_graph)
        num_column=len(self.original_graph[0])
        for i in range(num_row):
            for j in range(num_column):
                if [i,j] in self.pillar:
                    self.original_graph[i][j]=1
                if [i,j] in self.number_cross_area:
                    self.original_graph[i][j]=1
        #print(self.path)
        #print(self.colour_area)
        for key in self.colour_area:
            if self.number_colour_gate.get(key):
                if self.number_colour_gate[key]==2:
                    self.number_path+=1
                    self.path_position[key]=self.colour_area[key]
        #print(self.path_position)

    def analyse(self):
        self.map_of_maze()
        self.colour_shapes()
        self.find_gate()
        self.find_set_of_walls()
        self.find_inaccessible_inner_points()
        self.find_accessible_areas()
        self.find_cul_de_sacs()
        self.find_pillar()
        self.find_unique_path()
        if self.gate==0:
            print('The maze has no gate.')
        elif self.gate==1:
            print ('The maze has a single gate.')
        else:
            print(f'The maze has {self.gate} gates.')
        if self.colour==0:
            print('The maze has no wall.')
        elif self.colour==1:
            print ('The maze has walls that are all connected.')
        else:
            print(f'The maze has {self.colour} sets of walls that are all connected.')
        if self.number_inner_point==0:
            print('The maze has no inaccessible inner point.')
        elif self.number_inner_point == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {self.number_inner_point} inaccessible inner points.')
        if self.number_access_area==0:
            print('The maze has no accessible area.')
        elif self.number_access_area==1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {self.number_access_area} accessible areas.')
        if self.number_cul_de_sace==0:
            print('The maze has no accessible cul-de-sac.')
        elif self.number_cul_de_sace==1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {self.number_cul_de_sace} sets of accessible cul-de-sacs that are all connected.')
        if self.number_path==0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif self.number_path==1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {self.number_path} entry-exit paths with no intersections not to cul-de-sacs.')



#maze = Maze('maze_13.txt')
#maze.analyse()

















