from flask import Flask, request, render_template
import plotly.express as px
from io import BytesIO
from dash import html, dcc, callback, Input, Output, State
import dash
import base64
# werkzeug é um servidor web para desenvolvimento
from werkzeug.serving import run_simple

# server = Flask(__name__)
#
# app = dash.Dash(__name__, server=server)
#
#
# @server.route('/home')
# def index():
#     return 'Hello Flask App'
#
#
# app.layout = html.Div([
#     html.H1('Hello Dash app')
# ])
#
#
# if __name__ == '__main__':
#     run_simple('localhost', 5000, server)
