def origem_destino_iguais(origem,destino,lista_de_erro):
    if origem == destino:
        lista_de_erro['destino'] = 'Origem e Destino nao podem ser iguais'

def campo_tem_numero(valor_campo,nome_campo,lista_de_erro):
    if any(char.isdigit() for char in valor_campo):
        lista_de_erro[nome_campo] = 'Nao inclua numeros nesse campo'

def data_ida_maior_data_volta(ida,volta,lista_de_erro):
    if ida > volta:
        lista_de_erro['volta'] = 'Data de ida nao pode ser maior que data de volta'

def data_ida_menor_data_hoje(ida,data,lista_de_erro):
    if ida > data:
        lista_de_erro['ida'] = 'Data de ida nao pode ser menor que a data atual'
