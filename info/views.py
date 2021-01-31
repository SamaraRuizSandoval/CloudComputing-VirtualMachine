from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import socket
import sys


def index(request):
    # Connect to the HTML file
    template = loader.get_template('info/index.html')

    # Get Host Info
    hostname = socket.gethostname()             # Get Server Host
    IPAddr = socket.gethostbyname(hostname)     # Get IP Address
    reqMethod = request                         # Get Request method
    protocol = request.META['SERVER_PROTOCOL']  # Get server Protocol
    userAgent = (request.headers).get('User-Agent')

    # Get Remote Port
    if 'SERVER_PORT' in request.META:
        remotePort = request.META['SERVER_PORT']
    else:
        remotePort = "Error"

    # Get information from user
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"

    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string

    context = {
        'IPAddr': IPAddr,
        'remotePort': remotePort,
        'reqMethod': request,
        'serverHost': hostname,
        'protocol': protocol,
        'userAgent': userAgent,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type": os_type,
        "os_version": os_version
    }
    return HttpResponse(template.render(context, request))


def get_port(request):
    if 'SERVER_PORT' in request.META:
        return request.META['SERVER_PORT']
    else:
        return None
