from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/saudacao/{nome}") #decorator - @
async def root(nome: str):
    texto = f'Olá { nome }, tudo em paz?!'

    return {'mensagem': texto}

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    texto= f'O quadrado de {numero} é {resultado}'

    return {"mensagem": texto}


### Query Strings

@app.get('/dobro') #?nome=valor
def dobro(valor: int):
    resultado = 2 * valor
    return {'resultado': f'O dobro do {valor} é {resultado}'}

# http://localhost:8000/dobro?valor=4

@app.get('/area-retangulo')
def area_retangulo(largura: int, altura:int = 1):
    area = largura * altura
    return {'area': area}

# http://localhost:8000/area-retangulo?largura=5&altura=6


## Post

class Produto(BaseModel):
    nome: str
    preco: float 


@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto({produto.nome} - R$ {produto.preco}) cadastrado com sucesso!'}