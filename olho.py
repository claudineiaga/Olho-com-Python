import turtle as t, random as r, math as m
t.colormode(1.0); t.bgcolor("#0b0b14")
t.speed(0); r.seed(7)
p = t.Turtle(); p.hideturtle()   # a pálpebra

def linha(pts, cor, w=1, tt=t):
    tt.pu(); tt.goto(pts[0]); tt.pd()
    tt.pencolor(cor); tt.pensize(w)
    for q in pts[1:]: tt.goto(q)

def polar(a, d): return (d*m.cos(a), d*m.sin(a))

def palpebra(k):           # 0 = aberto, 1 = fechado
    p.clear(); s = 1 - 1.5*k
    borda = [(x, y + (yb - y - 2)*k)
             for (x, y), (_, yb) in zip(cima, baixo)]
    if k > 0:
        p.pu(); p.goto(cima[0]); p.fillcolor("#c9a594")
        p.begin_fill()
        linha(cima + borda[::-1], "white", 3, p)
        p.end_fill()
        linha(borda, "#6b5a52", 3, p)
    for (x, y), (j, n) in zip(borda[2:-2], cil):
        a, pts = 90 - x/5 + j, [(x, y)]
        for passo in range(n):          # um cílio
            px, py = pts[-1]
            pts.append((px + 7*m.cos(m.radians(a)),
                        py + 7*s*m.sin(m.radians(a))))
            a += 6 if x > 0 else -6
        linha(pts, "#d8d0c8", 2, p)
    t.update()

# 1. contorno e pálpebra
xs = range(-400, 401, 10)
cima = [(x, 190*(1-(x/400)**2)) for x in xs]
baixo = [(x, -160*(1-(x/400)**2)) for x in xs]
t.fillcolor("#ece4dc"); t.begin_fill()
linha(cima + baixo[::-1], "white", 3)
t.end_fill()
linha([(x, y*1.2+15) for x, y in cima[4:-4]], "#6b5a52", 2)

# 2. íris: 2000 fibras
for i in range(2000):
    a, b = r.uniform(0, 2*m.pi), r.uniform(.6, 1)
    meio = r.uniform(70, 95)
    ouro, azul = (.9*b, .6*b, .2*b), (.1*b, .5*b, .8*b)
    linha([polar(a, 40), polar(a, meio)], ouro)
    linha([polar(a, meio), polar(a+.03, 150)], azul)
    linha([polar(a, 140), polar(a, 152)], (0, .1, .2), 2)

# 3. pupila e reflexo
t.pu(); t.goto(0, 0); t.dot(105, "black")
t.goto(-42, 40); t.dot(36, "white")

# 4. cílios, desenhados pela pálpebra
cil = [(r.uniform(-8, 8), r.randint(6, 11))
       for _ in cima[2:-2]]
palpebra(0)

# 5. piscar
def piscar(i=0):
    palpebra([0, .5, 1, 1, .6, .2, 0][i])
    espera = 40 if i < 6 else 2000       # milissegundos
    t.ontimer(lambda: piscar((i + 1) % 7), espera)

t.hideturtle(); t.tracer(0); piscar(); t.done()
