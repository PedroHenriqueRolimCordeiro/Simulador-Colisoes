//Projeto Simulador de Colisões
1. Definição
Particle Dynamics
Position: p = (px, py)
Velocity: v = (vx, vy)
Acceleration: a = (ax,ay)

-------------------------------------------
//manter por enquanto a = 0
Frame f -> f + 1
Deltat = 1/FPS
Define a, v0, e p0
vf + 1 = vf + aDeltat
pf + 1 = pf + vfDeltat
--------------------------------------
Collision Detection

Para Esquerda e Direita
vf + 1 := (-vf+1[0], vf+1[1])

Para Cima e Baixo
Vf + 1 := (vf+1[0], -vf+1[1])
--------------------------------------
Example of Implementation
//Objeto
p=()   Objeto da Particula
box=() Objeto da Caixa
def update(dt): Atualizar os frames
    #dt: 1/FPS (e.g 1/60 for 60 FPS)
    #chamada pela engine para atualizar frames(Adaptar isso para o simulador)
    p.vel = p.vel + p.accel * dt
    p.pos = p.pos + p.vel * dt
    handleBoxColision()

def handleBoxColision ():
    if p.left[0] =< box.left[0] or
        p.right[0] => box.right[0]:
        p.vel[0] = -p.vel[0]
    if p.bottom[1] =< box.bottom[1] or
        p.top[1] => box.top[1]:
        p.vel[1] = -p.vel[1]
-----------------------------------------------
Resolvendo Tunneling

Easy Solution
1. Enforce speed limits on particles
2. Use higher frame rates

---------------------------------------------
Continuous Colision Detection

//Printscreen do video(muitas imagens não da para colocar aqui, vou separar elas juntas numa pagina)

----------------------------------------------
Scaling up Simulations

Idea 1: Try all pairs of particles
Torna-se rapidamente muito caro para a maquina
100 particulas ≈ 5000 testes de colisões
5000 testes a cada frame
60 FPS/1 min ≈ 18 milhoes de colisões check

idea 2: Collision Detection Framework

1. Broad Phase
    Which objects could be  colliding?
2. Narrow Phase
    Are they actually colliding?
3. Solve Collision
    How do we update dynamics?

----------------------------------------------
Idea of optimization
Sweep and Prune algorithm

Ordena particulas por um axis (x ou y)

---------------------------------------------------
Space Partitions

Uniform grid space partitioning

ver os prints

--------------------------------------------------
├── src/
│   ├── __init__.py
│   ├── physics_core/
│   │   ├── __init__.py
│   │   ├── particle.py
│   │   └── simulation_space.py
│   ├── collision/
│   │   ├── __init__.py
│   │   └── detection_response.py
│   └── visualization/
│       ├── __init__.py
│       └── animator.py
├── tests/
│   ├── __init__.py
│   ├── test_physics.py
│   └── test_collisions.py
├── docs/
├── config/
│   └── settings.yaml
├── README.md
├── requirements.txt
└── setup.py (opcional, para empacotamento)
------------------------------------------------
class Carro:
    def __init__(self, marca, modelo, ano, cor, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.km = km

    def __str__(self):
        return f"O {self.cor} carro tem {self.km} km"

Polo = Carro("VW", "Polo", 2020, "branco", 10000)
print(Polo)
Gol = Carro("VW", "Gol", 2010, "branco", 50000)
print(Gol)
for carro in (Polo, Gol):
    print(carro)
-------------------------------
Velocity Verlet
Sweep and Prune algorithm







class Trabalhador:
    tipo = "Programador"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Metodo Instancia
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

Pedro = Trabalhador("Pedro", 20)
print(Pedro)    
