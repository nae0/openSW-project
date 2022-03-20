import turtle as t

i, k, tx, ty = [0]*4
swidth, sheight = 800, 450

if __name__ == "__main__" :
    t.shape('turtle')
    t.setup(width = swidth + 50, height = sheight + 50)
    t.screensize(swidth, sheight)
    t.penup()
    tx, ty = -500, 250
    t.goto(tx, ty)

    for i in range(1, 10) :
        for k in range(2, 10) :
            t.goto(tx + 80 * k, ty - 40 * i)
            gugu = str(k) + ' x ' + str(i) + ' = ' + str(k*i)
            t.write(gugu, font = ('Arial', 12, 'bold'))

    t.done()
