from fastapi import Request


async def processar_tempo_requisicao(request: Request, next):
    print("Interceptou Chegada...")
    # Pode se interceptar qualquer coisa
    # request.headers.get('Authentication')

    response = await next(request)
    print("Interceptou Volta...")
    return response
