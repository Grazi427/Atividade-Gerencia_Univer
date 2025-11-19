class Curso:
    # Representa um curso oferecido por um campus
    def __init__(self, nome, duracao_semestres):
        self.nome = nome
        self.duracao_semestres = duracao_semestres

    def __str__(self):
        return f"Curso: {self.nome} ({self.duracao_semestres} semestres)"