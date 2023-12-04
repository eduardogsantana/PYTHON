class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_filme):
        self._nome = novo_filme.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):#__str__ é um método especial, como __init__ , usado para retornar uma representação de string de um objeto.
        return f'Nome: {self.nome} | Ano: {self.ano} | Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):#__str__ é um método especial, como __init__ , usado para retornar uma representação de string de um objeto.
        return f'Nome: {self.nome} | Ano: {self.ano} | Duração: {self.duracao} minutos | Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self): #__str__ é um método especial, como __init__ , usado para retornar uma representação de string de um objeto.
       return f'Nome: {self.nome} | Ano: {self.ano} | Temporadas: {self.temporadas} | Likes: {self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item): # método que define 'alguem' que é iterável
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas
        
   
    def __len__(self): # método importado de list para a playlist.
        return len(self._programas)



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tdmp = Filme('todo mundo em pânico', 1999, 120)
reacher = Serie('reacher', 2022, 2)
demolidor = Serie('demolidor', 2019, 2 )
justiceiro = Serie('justiceiro', 2020, 2)
homem_aranha = Filme('homem-aranha - sem volta para casa', 2021, 180)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tdmp.dar_like()
tdmp.dar_like()
tdmp.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()


reacher.dar_like()
reacher.dar_like()
reacher.dar_like()
reacher.dar_like()
reacher.dar_like()
reacher.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
justiceiro.dar_like()
justiceiro.dar_like()
justiceiro.dar_like()


filmes_e_series = [vingadores, homem_aranha,  reacher,  demolidor, justiceiro, tdmp]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)