class Artigo:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f"Titulo: {self.titulo} | Autor {self.autor}"

class Edicao:
    
    def __init__(self, numero, volume, data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = []
        
    def adicionar_novo_artigo(self, artigo):
        self.artigos.append(artigo)
        
    def get_edicao(self):
        return f"Edição Número: {str(self.numero)} | Volume: {str(self.volume)} | Data: {str(self.data)} "
    
    def __deletar_item__(self, titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo)
    
    def show_artigo(self):
        for artigo in self.artigos:
            print(artigo.__str__())
    
    def __len__(self):
        return len(self.artigos)
    
class Revista:
    
    def __init__(self, titulo, issn, periodicidade):
        self.titulo = titulo
        self.issn = issn 
        self.periodicidade = periodicidade
        self.edicoes = []
        
    def adicionar_nova_edicao(self, edicao):
        self.edicoes.append(edicao)
        
    def lancar_edicao(self, edicao):
        num_artigos = edicao.__len__()
        if (num_artigos >= 10 and num_artigos <= 15):
            return " Sua edição foi lançada com sucesso! "

        else:
            return "Houve um problema na hora do lançamento. Verifique se sua ediçaõ tem entre 10 artigos e 15 artigos para lançar a edição."
    
    def show_edicoes(self):
        for edicao in self.edicoes:
            print(edicao.get_edicao())
        
        
