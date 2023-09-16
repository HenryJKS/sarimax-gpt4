import dash
import dash_quill
import base64
from ChatBotWeb.components import navbar
from dash import html, dcc, callback, Input, Output
import smtplib, ssl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from Script.config import MAIL_PASSWORD, MAIL
import dash_bootstrap_components as dbc

NAVBAR = navbar.create_navbar()

dash.register_page(
    __name__,
    name='SendEmail',
    top_navbar=True,
    path='/sendEmail',
    external_stylesheets=[dbc.themes.LITERA]
)

quill_mods = [
    [{'header': '1'}, {'header': '2'}, {'font': []}],
    [{'size': []}],
    ['bold', 'italic', 'underline', 'strike', 'blockquote'],
    [{'list': 'ordered'}, {'list': 'bullet'},
     {'indent': '-1'}, {'indent': '+1'}],
    ['link', 'image'],
    ['clean'],
    [{'script': 'sub'}, {'script': 'super'}],
    [{'direction': 'rtl'}],
]

layout = dbc.Container([
    dbc.Row([
        NAVBAR
    ]),

    html.H2([
        "Envio de E-mail"
    ], className='text-center mt-2'),

    html.Hr(),

    html.Div([
        dbc.InputGroup(
            [
                dbc.Input(id='receiver_address', placeholder="Destino"),
                dbc.InputGroupText("@gmail.com"),
            ],
            style={'width': '25%', 'margin-right': '10px'},
        ),

        dbc.InputGroup(
            [
                dbc.InputGroupText("Assunto: "),
                dbc.Input(id='subject'),
            ],
            style={'width': '25%'}
        ),
    ], style={'display': 'flex', 'flex-direction': 'row'}),

    html.Div([
        html.Div([
            html.Label("Mensagem:"),
        ]),

        dash_quill.Quill(
            id='message',
            modules={'toolbar': quill_mods}
        ),

    ], className='mt-2'),

    html.Div([
        html.Div([

        ], id='file-list'),
    ], className='mb-2'),

    html.Div([
        dcc.Upload(
            id='attachment-upload',
            children=html.Div([
                'Arraste e Solte ou ',
                html.A('Selecione um Arquivo')
            ]),
            multiple=True,
            style={'width': '28%',
                   'height': '60px',
                   'lineHeight': '60px',
                   'borderWidth': '1px',
                   'borderStyle': 'dashed',
                   'borderRadius': '5px',
                   'textAlign': 'center',
                   'margin-top': '10px'
                   }
        )
    ]),

    html.Div([
        html.Button('Enviar E-Mail', id='enviar-button', className='btn btn-primary')
    ], className='mt-2'),

    html.Div([
        html.Div(id='resultado')
    ]),

], fluid=True, style={'background-color': '#e8f5ff', 'height': '100%'})


@callback(
    Output('resultado', 'children'),
    [Input('enviar-button', 'n_clicks')],
    [dash.dependencies.State('receiver_address', 'value'),
     dash.dependencies.State('subject', 'value'),
     dash.dependencies.State('message', 'value')],
    [dash.dependencies.Input('attachment-upload', 'contents')],
    [dash.dependencies.State('attachment-upload', 'filename')]
)
def send_mail(n_clicks, receiver_address, subject, message, attachment_contents, attachment_filenames):
    if n_clicks is None:
        return ''

    try:
        mail_server = 'smtp.gmail.com'
        mail_port = 465
        sender_address = MAIL
        sender_password = MAIL_PASSWORD

        if receiver_address is None:
            return dbc.Alert('Insira um email !', color='danger', className='text-center mt-2')

        # Concatenar o endereço
        receiver_address = receiver_address + '@gmail.com'

        if receiver_address == sender_address:
            return dbc.Alert('Não é possível enviar um e-mail para você mesmo!', color='danger',
                             className='text-center mt-2')

        if subject is None:
            return dbc.Alert("Insira o assunto do envio", color='danger', className='text-center mt-2')

        if message is None:
            return dbc.Alert("Insira a mensagem do envio", color='danger', className='text-center mt-2')

        msg = MIMEMultipart("")
        msg["Subject"] = subject
        msg["From"] = sender_address
        msg["To"] = receiver_address

        msg.attach(MIMEText(message, 'html'))

        context = ssl.create_default_context()

        if attachment_contents and attachment_filenames is not None:
            for content, filename in zip(attachment_contents, attachment_filenames):
                if filename:  # Verifique se o nome do arquivo não é None
                    # Adicione o arquivo como um anexo
                    part = MIMEBase('application', 'octet-stream')
                    file_content = content.split(',')[1]
                    part.set_payload(base64.b64decode(file_content))
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
                    msg.attach(part)

        with smtplib.SMTP_SSL(mail_server, mail_port, context=context) as server:
            server.login(sender_address, sender_password)
            server.sendmail(sender_address, receiver_address, msg.as_string())
        return dbc.Alert("E-mail Enviado com Sucesso!", color='success', className='text-center mt-2')
    except smtplib.SMTPAuthenticationError:
        return html.Div("Erro de autenticação: Nome de usuário ou senha inválidos.", className='text-danger mt-2')
    except smtplib.SMTPException as e:
        return html.Div(f"Erro ao enviar o e-mail: {e}", className='text-danger mt-2')
    except Exception as e:
        return html.Div(f"Erro inesperado: {e}", className='text-danger mt-2')


@callback(Output('file-list', 'children'),
          Input('attachment-upload', 'filename'))
def update_output(attachment_filenames):
    if attachment_filenames is None:
        return html.Div('Nenhum Arquivo Anexado', className='text-info')
    return html.Div(f'Arquivo Anexado(s): {attachment_filenames[:]}', className='text-success')
