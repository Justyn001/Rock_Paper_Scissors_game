import functions as rps

flag = True
while flag:
    j = rps.fileread()
    x = rps.start()
    y = rps.computerchoice()
    z = rps.game(x,y,j)
    flag = rps.savetofile(z)