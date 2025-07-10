from datetime import datetime, timedelta, time, timezone
import pywhatkit as kit
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

escopo=['https://www.googleapis.com/auth/calendar.readonly']
def registrar_logs(texto):
    with open('log_envios.txt','a',encoding='UTF-8') as log:
        agora=datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        log.write(f'[{agora}] {texto}\n')
def autenticargoogle():
    credencial=None
    if os.path.exists('token.json'):
        credencial= Credentials.from_authorized_user_file('token.json', escopo)
    if not credencial or not credencial.valid:
        if credencial and credencial.expired and credencial.refresh_token:
            credencial.refresh(Request())
        else:
            flow= InstalledAppFlow.from_client_secrets_file('credentials.json',escopo)
            credencial=flow.run_local_server(port=0)
        with open('token.json','w') as token:
            token.write(credencial.to_json())
    return credencial


def confirma_eventos():
    lista_eventos = []
    credencial = autenticargoogle()
    service = build('calendar', 'v3', credentials=credencial)
    hoje = datetime.now(timezone.utc).date()
    amanha = hoje + timedelta(days=1)
    tempo_min = datetime.combine(amanha, time.min).isoformat() + 'Z'
    tempo_max = datetime.combine(amanha, time.max).isoformat() + 'Z'

    agenda = service.events().list(
        calendarId='primary',
        timeMin=tempo_min,
        timeMax=tempo_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])

    for evento in agenda:
        inicio = evento['start'].get('dateTime', evento['start'].get('date'))
        titulo = evento.get('summary', '(Sem titulo)')
        descricao = evento.get('description', '(Sem descrição)')
        lista_eventos.append({
            'inicio': inicio,
            'titulo': titulo,
            'descrição': descricao
        })

    if not lista_eventos:
        print('Nenhum evento encontrado')

    return lista_eventos
def extrai_dados(texto):
    linhas=texto.split('\n')
    dados={}
    ctt=[]
    for linha in linhas:
        linha =linha.strip().lower()
        if linha.startswith('tutor:'):
            dados['tutor']=linha.split(':',1)[1].strip()
        elif linha.startswith('ctt:'):
            numero=linha.split(':',1)[1].strip()
            ctt.append(numero)
        elif linha.startswith('doutor:'):
            dados['doutor']=linha.split(':',1)[1].strip()
    dados['ctt']=ctt
    return dados
def proximo_horario(minuto_extra=1):
    agora=datetime.now()
    hora=agora.hour
    minuto=agora.minute + minuto_extra
    if minuto >= 60:
        minuto-=60
        hora=(hora+1)%24
    return hora,minuto
def envia_mensagem(agenda):
    hora, minuto=proximo_horario(2)
    contatos_enviados=[]
    for evento in agenda:
        descricao = evento.get('descrição',"")
        dados = extrai_dados(descricao)
        titulo=evento.get('titulo','Consulta')
        horario=evento.get('inicio',"Horario não informado")
        try:
            if len(dados['ctt'])>=1:
                numero_tutor='+55'+dados['ctt'][0]
                if numero_tutor not in contatos_enviados:
                    mensagem_tutor=f"Olá {dados.get('tutor',' ')}, seu pet tem {titulo} com Dr. {dados.get('doutor','')} confirmada para amanhã ás {horario}, tudo certo?"
                    kit.sendwhatmsg(numero_tutor,mensagem_tutor,hora,minuto)
                    contatos_enviados.append(numero_tutor)
                    registrar_logs(f'Mensagem enviada para tutor: {numero_tutor}')
            if len(dados['ctt'])>=2:
                numero_doutor = '+55'+dados['ctt'][1]
                if numero_doutor not in contatos_enviados:
                    mensagem_doutor = f"Olá Dr. {dados.get('doutor')}, amanhã você tem {titulo} com o pet do tutor {dados.get('tutor','')}. Tudo certo?"
                    kit.sendwhatmsg(numero_doutor,mensagem_doutor,hora,minuto+1)
                    contatos_enviados.append(numero_doutor)
                    registrar_logs(f'Mensagem enviada para doutor: {numero_doutor}')
        except Exception as e:
            registrar_logs(f'❌ Erro ao enviar mensagens: {str(e)}')
if __name__=='__main__':
    eventos=confirma_eventos()
    if eventos:
        envia_mensagem(eventos)
    else:
        registrar_logs('Nenhum evento para amanhã.')
