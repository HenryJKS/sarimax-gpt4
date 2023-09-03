import dash

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

layout = dbc.Container([
    dbc.Row([
        NAVBAR
    ]),

    html.H2([
        "Envio de E-mail"
    ], className='text-center mt-2'),

    html.Hr(),

    html.Div([
        html.Label("Destinatário:"),
        dcc.Input(id='receiver_address', type='email', placeholder='Digite o e-mail do destinatário'),
        html.Label("Assunto:"),
        dcc.Input(id='subject', type='text', placeholder='Digite o assunto'),

        html.Div([
            html.Label("Mensagem:"),
        ]),

        dcc.Textarea(id='message', placeholder='Digite a mensagem', style={'width': '100%', 'height': 150}),
        html.Label("Anexos:"),
        dcc.Upload(
            id='attachment-upload',
            children=html.Div([
                'Arraste e Solte ou ',
                html.A('Selecione um Arquivo')
            ]),
            multiple=True
        ),
        html.Button('Enviar E-mail', id='enviar-button'),
        html.Div(id='resultado')
    ])
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
        return '';

    try:
        mail_server = 'smtp.gmail.com'
        mail_port = 465
        sender_address = MAIL
        sender_password = MAIL_PASSWORD

        msg = MIMEMultipart("")
        msg["Subject"] = subject
        msg["From"] = sender_address
        msg["To"] = receiver_address

        msg.attach(MIMEText(message, 'plain'))

        context = ssl.create_default_context()

        if attachment_contents and attachment_filenames:
            for content, filename in zip(attachment_contents, attachment_filenames):
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(content)
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(attachment)

        with smtplib.SMTP_SSL(mail_server, mail_port, context=context) as server:
            server.login(sender_address, sender_password)
            server.sendmail(sender_address, receiver_address, msg.as_string())
        return html.Div("E-mail enviado com sucesso!", style={'color': 'green'})
    except smtplib.SMTPAuthenticationError:
        return html.Div("Erro de autenticação: Nome de usuário ou senha inválidos.", style={'color': 'red'})
    except smtplib.SMTPException as e:
        return html.Div(f"Erro ao enviar o e-mail: {e}", style={'color': 'red'})
    except Exception as e:
        return html.Div(f"Erro inesperado: {e}", style={'color': 'red'})
