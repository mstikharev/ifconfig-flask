from flask import Flask, jsonify
from ifparser import Ifcfg
from ifparser.ifconfig import InterfaceNotFound
import commands

app = Flask(__name__)


@app.route('/')
def ifconfig():
    ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
    interfaces = ifdata.interfaces
    total_interfaces_info = []
    for interface in interfaces:
        ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
        interface_instance = ifdata.get_interface(interface)
        interface_values = interface_instance.get_values()
        interface_dict = {
            'name': interface,
            'info': interface_values
        }
        total_interfaces_info.append(interface_dict)
    response = jsonify(total_interfaces_info)
    return response


@app.route('/interfaces/')
def interfaces():
    ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
    interfaces_array = ifdata.interfaces
    response = jsonify(interfaces=interfaces_array)
    return response


@app.route('/interfaces/<name>/')
def get_interface(name):
    ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
    try:
        interface_instance = ifdata.get_interface(name)
        interface_values = interface_instance.get_values()
        interface_dict = {
            'name': name,
            'info': interface_values
        }
    except InterfaceNotFound:
        interface_dict = {
            'response': "Can't find this interface",
            'status': 'error'
        }
    response = jsonify(interface_dict)
    return response


@app.route('/interfaces/<name>/packets/')
def get_packets(name):
    ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
    try:
        interface_instance = ifdata.get_interface(name)
        interface_values = interface_instance.get_values()
        packets = {
            'txpkts': interface_values.get('txpkts'),
            'rxpkts': interface_values.get('rxpkts')
        }
        interface_dict = {
            'name': name,
            'packets': packets,
        }
    except InterfaceNotFound:
        interface_dict = {
            'response': "Can't find this interface",
            'status': 'error'
        }
    response = jsonify(interface_dict)
    return response


@app.route('/interfaces/<name>/status/')
def get_status(name):
    ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
    try:
        interface_instance = ifdata.get_interface(name)
        interface_values = interface_instance.get_values()
        interface_dict = {
            'name': name,
            'status': interface_values.get('UP'),
        }
    except InterfaceNotFound:
        interface_dict = {
            'response': "Can't find this interface",
            'status': 'error'
        }
    response = jsonify(interface_dict)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
