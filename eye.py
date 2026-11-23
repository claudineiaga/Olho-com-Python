import turtle as t, random as r, math as m
t.colormode(1.0); t.bgcolor("#0b0b14")
t.speed(0); r.seed(7)
p = t.Turtle(); p.hideturtle()   # the eyelid

def line(pts, color, w=1, tt=t):
    tt.pu(); tt.goto(pts[0]); tt.pd()
    tt.pencolor(color); tt.pensize(w)
    for q in pts[1:]: tt.goto(q)

def polar(a, d): return (d*m.cos(a), d*m.sin(a))

def eyelid(k):             # 0 = open, 1 = closed
    p.clear(); s = 1 - 1.5*k
    edge = [(x, y + (yb - y - 2)*k)
            for (x, y), (_, yb) in zip(top, bottom)]
    if k > 0:
        p.pu(); p.goto(top[0]); p.fillcolor("#c9a594")
        p.begin_fill()
        line(top + edge[::-1], "white", 3, p)
        p.end_fill()
        line(edge, "#6b5a52", 3, p)
    for (x, y), (j, n) in zip(edge[2:-2], lashes):
        a, pts = 90 - x/5 + j, [(x, y)]
        for step in range(n):           # one lash
            px, py = pts[-1]
            pts.append((px + 7*m.cos(m.radians(a)),
                        py + 7*s*m.sin(m.radians(a))))
            a += 6 if x > 0 else -6
        line(pts, "#d8d0c8", 2, p)
    t.update()

# 1. outline and eyelid crease
xs = range(-400, 401, 10)
top = [(x, 190*(1-(x/400)**2)) for x in xs]
bottom = [(x, -160*(1-(x/400)**2)) for x in xs]
t.fillcolor("#ece4dc"); t.begin_fill()
line(top + bottom[::-1], "white", 3)
t.end_fill()
line([(x, y*1.2+15) for x, y in top[4:-4]], "#6b5a52", 2)

# 2. iris: 2000 fibers
for i in range(2000):
    a, b = r.uniform(0, 2*m.pi), r.uniform(.6, 1)
    mid = r.uniform(70, 95)
    gold, blue = (.9*b, .6*b, .2*b), (.1*b, .5*b, .8*b)
    line([polar(a, 40), polar(a, mid)], gold)
    line([polar(a, mid), polar(a+.03, 150)], blue)
    line([polar(a, 140), polar(a, 152)], (0, .1, .2), 2)

# 3. pupil and reflection
t.pu(); t.goto(0, 0); t.dot(105, "black")
t.goto(-42, 40); t.dot(36, "white")

# 4. lashes, drawn by the eyelid
lashes = [(r.uniform(-8, 8), r.randint(6, 11))
          for _ in top[2:-2]]
eyelid(0)

# 5. blink
def blink(i=0):
    eyelid([0, .5, 1, 1, .6, .2, 0][i])
    wait = 40 if i < 6 else 2000       # milliseconds
    t.ontimer(lambda: blink((i + 1) % 7), wait)

t.hideturtle(); t.tracer(0); blink(); t.done()
