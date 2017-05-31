# PSP_TSP
repository which was created to share codes and readme for a PSP class

robot_psp, spyral walker:

The idea was to create a dictionnary and get the key and value corresponding to the index of the middle coordinates

squared_matrix: create a squared matrix whose size is the one you provide as a parameter
index_middle_matrix: detect the index of the middle of the matrix
coordinate_middle: gives the coordinates of the robot once he reached the middle of the matrix

but, the key,value system was not created well and it resulted in going through the matrix from left to right like conventional reading instead of spyral
once I realised I try to switch for other systems: 
-dictionnary containing arrays all with this format [0,1,2,3,4,5] and then visit each array and get both the key nd value once I reach the middle of the matrix like I wanted to do in the first place
-find a relation using recurrence reasonning to find a relation and then the coordinates

but both did not work and made me lose a lot of time
I guess a better preparation of the code would have provided better results

targetted PSP
language: python
Time: 40 mins
LOC: 60
Bugs: 10


robot_psp2, obstacles detection:

The target is to create a pogramm which will tell how much robots are needed to cover a matrix where there also are obstacles
When the nearest neighbor of the current index is a 1 go cover this neihbor (if you have not covered it yet. 
If all your neigbhors (not visited) are 0 increment the robot counter and creatre a new robot on the next 1 slot
If you cannot go in a neigbor (because you hav visited everything then stop the programm and display the robot counter)

Create a matrix containing 50% 0 (obstacles) and 50% 1 (where the robot can go)
Create a "robot" on the first case containing a 1 (if (0,0) is a 0 then try (0,1)...)
Once you have visited the first line go to the next line if it contains one or several 1 check this line if there are only 0
increment the robot counter and go to the next line

while you have not reached the end of the matrix keep repeating this algorithm

targetted PSP
language: python
Time: 50 mins
LOC: 60
Bugs: 20


As I had lost lot of time with the first exercise I was not able to do the second one 
