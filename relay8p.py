from platform import release
import requests
import re
from urllib.parse import urlparse 
import socket
import logging
from os import path


def vIP(address,port):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)
    global ipc
    
    try:
        if bool(match) is True:
            for part in address.split("."):
                if int(part) > 0 and int(part) < 255:
                    ip = address+':'+str(port)
                    ipc = ip
                    # return ip
        else:
            x = urlparse(f'http://{address}:{port}')
            y = x.hostname
            z = x.port
            ip = socket.gethostbyname(f'{y}')
            ip = ip+':'+str(z)
            ipc = ip
            # return ip
        global var
        var = req_status(ip)
        return var
    except socket.herror as herr:
        pass
    except socket.gaierror as gerr:
        pass
    except socket.timeout as terr:
        pass
    except InterruptedError as ierr:
        pass
    except OSError as oerr:
        pass
    
def config():
    global tempo
    global pw
    
    tempo = 50 #quando tipo 0 => 0, tipo 1 => 1~255 (1=100ms), tipo 2 => 1~65535 (segundos)
    pw = "br@$po&rt&ec#"

    return tempo,pw

def req_control(Tipo=0,Rele=1,Estado=1):
    try:
        r = requests.get(f'http://{ipc}/relay_cgi.cgi?type={Tipo}&relay={Rele}&on={Estado}&time={tempo}&pwd={pw}&', timeout=5)  # -> botões
        
        logging.basicConfig(filename=f'teste_log.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
        logging.info(f'Resquest success: port {Rele} was changed')

    except requests.exceptions.HTTPError as errh:
        pass
    except requests.exceptions.ConnectionError as errc:
        pass
    except requests.exceptions.Timeout as errt:
        pass
    except requests.exceptions.RequestException as err:
        pass

def req_status(ip):
    try:
        req2 = requests.get(f'http://{ip}/relay_cgi_load.cgi')   #-> update
        x2 = req2.content.decode('utf-8').lstrip("&").rstrip("&")
        l2 = list(x2.split("&"))

        var = dict()
        for i in range(len(l2)):
            var['r'+str(i)] = l2[i]

        return var
    except requests.exceptions.HTTPError as errh:
        pass
    except requests.exceptions.ConnectionError as errc:
        pass
    except requests.exceptions.Timeout as errt:
        pass
    except requests.exceptions.RequestException as err:
        pass

def caminho(arq):
    path_to_dat = path.abspath(path.join(path.dirname(__file__), f'{arq}'))
    return path_to_dat