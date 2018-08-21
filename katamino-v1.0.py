
# coding: utf-8

# # Katamino is a game with some elements that you must add them to the base until you look at a rectangle.
# In version 1.0 we add 6 object.

# In[1]:


from termcolor import colored

#basex is count of elements you want to play with them.
basex=4

#list of your elements to play with them.
elements=[1,2,3,6]

#count of all elements that created in code of game and support in game. 
baseAll=6

#base is a rectangle that we want to create elements as it.
base=[]

#backup in array to save last status of base before add an element.
backup=[]

#array of array that save state of base in end of putting process fo elements.
backupx=[]

#every position and direction that found after process that can element insert in that position.
found=[]

#element is list of your selected elements that automaticaly create by $elements & $basex
element=[1]

#elementAll is all elements that create in source code not more!!!
elementAll=[1]

color={0:'grey',1:'red',2:'blue',3:'green'}

def showBase():
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    for i in range(0,5):
        for j in range(0,basex):
            if base[j][i] in color:
                print(colored(base[j][i],color[base[j][i]]),"  ",end='')
            else:
                print(base[j][i],'  ',end='')
        #print(base[0][i],'  ',base[1][i],'  ',base[2][i],'  ',base[3][i])
        print()
    
def showBackup():
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    for i in range(0,5):
        for j in range(0,basex):
            print(backup[j][i],'  ',end='')
        #print(backup[0][i],'  ',backup[1][i],'  ',backup[2][i])
    print()

def resetBase():
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    base=[]
    backup=[]
    backupx=[]
    found=[]
    element=[1]
    
    createAllelements()
    for i in range(0,basex):
        base.append([0,0,0,0,0])
        backup.append([0,0,0,0,0])
        found.append([])
        
    for x in range(0,basex):
        backupx.append([])
        for i in range(0,basex):                
            backupx[x].append([0,0,0,0,0])
            
    for i in range(1,baseAll*8+1):
        if elementAll[i][0] in elements:
            element.append(elementAll[i])
    
    
def copyBaseToBackup():
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    for i in range(0,basex):
        for j in range(0,5):
            backup[i][j]=base[i][j]
    
def copyBackupToBase():
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    for i in range(0,basex):
        for j in range(0,5):
            base[i][j]=backup[i][j]
                        
def copyBaseToBackupx(k):
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    for i in range(0,basex):
        for j in range(0,5):
            backupx[k][i][j]=base[i][j]    
    
def copyBackupxToBase(k):
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    for i in range(0,basex):
        for j in range(0,5):
            base[i][j]=backupx[k][i][j] 


# In[2]:


def createAllelements():
    elementAll.append([1,'rd','r','r','d','d'])
    elementAll.append([1,'dr','d','d','r','r'])
    elementAll.append([1,'dl','d','d','l','l'])
    elementAll.append([1,'ld','l','l','d','d'])
    elementAll.append([1,'ru','r','r','u','u'])
    elementAll.append([1,'ur','u','u','r','r'])
    elementAll.append([1,'ul','u','u','l','l'])
    elementAll.append([1,'lu','l','l','u','u'])

    elementAll.append([2,'rd','r','r','d','l'])
    elementAll.append([2,'dr','d','d','r','u'])
    elementAll.append([2,'dl','d','d','l','u'])
    elementAll.append([2,'ld','l','l','d','r'])
    elementAll.append([2,'ru','r','r','u','l'])
    elementAll.append([2,'ur','u','u','r','d'])
    elementAll.append([2,'ul','u','u','l','d'])
    elementAll.append([2,'lu','l','l','u','r'])
    
    elementAll.append([3,'rd','r','d','d','d'])
    elementAll.append([3,'dr','d','r','r','r'])
    elementAll.append([3,'dl','d','l','l','l'])
    elementAll.append([3,'ld','l','d','d','d'])
    elementAll.append([3,'ru','r','u','u','u'])
    elementAll.append([3,'ur','u','r','r','r'])
    elementAll.append([3,'ul','u','l','l','l'])
    elementAll.append([3,'lu','l','u','u','u'])
    
    elementAll.append([4,'rd','r','r','dl','d'])
    elementAll.append([4,'dr','d','d','ur','r'])
    elementAll.append([4,'dl','d','d','ul','l'])
    elementAll.append([4,'ld','l','l','dr','d'])
    elementAll.append([4,'ru','r','r','ul','u'])
    elementAll.append([4,'ur','u','u','dr','r'])
    elementAll.append([4,'ul','u','u','dl','l'])
    elementAll.append([4,'lu','l','l','ur','u'])
    
    elementAll.append([5,'rd','r','d','d','l'])
    elementAll.append([5,'dr','d','r','r','u'])
    elementAll.append([5,'dl','d','l','l','u'])
    elementAll.append([5,'ld','l','d','d','r'])
    elementAll.append([5,'ru','r','u','u','l'])
    elementAll.append([5,'ur','u','r','r','d'])
    elementAll.append([5,'ul','u','l','l','d'])
    elementAll.append([5,'lu','l','u','u','r'])
    
    elementAll.append([6,'rd','r','d','d','r'])
    elementAll.append([6,'dr','d','r','r','d'])
    elementAll.append([6,'dl','d','l','l','d'])
    elementAll.append([6,'ld','l','d','d','l'])
    elementAll.append([6,'ru','r','u','u','r'])
    elementAll.append([6,'ur','u','r','r','u'])
    elementAll.append([6,'ul','u','l','l','u'])
    elementAll.append([6,'lu','l','u','u','l'])


# element 1 
# 
# 1 1 1 
#     1 
#     1 
# 
# 
# element 2 
# 
# 2
# 2 2
# 2 2
# 
# 
# element 3
# 
# 3 3
#   3
#   3
#   3
#   
#   
# element 4
# 
# 4 4 4
#   4
#   4
# 
# 
# element 5
# 
# 5 5
#   5
# 5 5
# 
# 
# element 6
# 
# 6 6
#   6
#   6 6
#   
# 

# In[3]:


def availableToAdd(x,y,element):
    global basex,base,backup,backupx,found,elementAll,elements,baseAll
    
    if x>=0 and y>=0:
        if x<basex and y<5:
            if base[x][y]==0:
                base[x][y]=element
                return True
    
    copyBackupToBase()
    return False


# In[4]:


def addToBase(element,x,y):
    
    global basex,base,backup,backupx,found,elementAll,elements,baseAll
    
    copyBaseToBackup()
    x=x-1
    y=y-1
    
    if not availableToAdd(x,y,element[0]): return(False)
    
    for i in range(2,6):
        if element[i]=='r':
            x+=1
            if not availableToAdd(x,y,element[0]): return(False)
        if element[i]=='d':
            y+=1
            if not availableToAdd(x,y,element[0]): return(False)           
        if element[i]=='l':
            x-=1
            if not availableToAdd(x,y,element[0]): return(False)  
        if element[i]=='u':
            y-=1
            if not availableToAdd(x,y,element[0]): return(False)  
            
        if element[i]=='ur':
            x+=1
            y-=1
            if not availableToAdd(x,y,element[0]): return(False)
        if element[i]=='ul':
            x-=1
            y-=1
            if not availableToAdd(x,y,element[0]): return(False)           
        if element[i]=='dr':
            x+=1
            y+=1
            if not availableToAdd(x,y,element[0]): return(False)  
        if element[i]=='dl':
            x-=1
            y+=1
            if not availableToAdd(x,y,element[0]): return(False)     
           
    return(True)


# In[5]:


def checkSolve():
    global basex,base,backup,backupx,found,element,elementAll,elements,baseAll
    t=0
    for i in range(0,basex):
        for j in range(0,5):
            if base[i][j]>0:
                t+=1
                if t==basex*5:
                    return(True)
    return(False)


# In[6]:


resetBase()
k=0
while k>-1 and k<basex:
    t=1
    copyBaseToBackupx(k)
    for el in range(1,9):
        for x in range(1,basex+1):
            for y in range(1,6):
                if [element[(k*8)+el],x,y] in found[k]:
                    continue
                if addToBase(element[(k*8)+el],x,y):
                    found[k].append([element[(k*8)+el],x,y])
                    print("=========found=========")
                    showBase()
                    k+=1
                    t=0
                    break
            if t==0: 
                break
        if t==0: 
            break
    
    if not t==0:
        found[k]=[]
        copyBackupxToBase(k-1)
        k-=1
                
                
            
            
            
if checkSolve():
    print ("")
    print ("")
    print ("YES WE CAN!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("")
    print("")
    print("These elements dosn't match!!!")
                                    

