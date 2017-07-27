from networktables import NetworkTables

def initialize(robot_ip):
    NetworkTables.initialize(robot_ip)
    global smart_dashboard
    smart_dashboard = NetworkTables.getTable("SmartDashboard")

def send_number(location, data):
    smart_dashboard.putNumber(location, data)