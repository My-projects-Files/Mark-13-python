import os
import subprocess
import time

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode()}")
    return stdout.decode()

def build_docker_img():
    print("Build docker image")
    command="docker build -t devops-test"
    output= run_command(command)
    print(output)

def run_docker_conatainer():
    print ("running docker container")
    command="docker run -d -p 5000:5000 -n devops_test_comtainer devops-test"
    output= run_command(command)
    print(output)

def wait_for_container():
    print("waiting for the container")
    time.sleep(5)

def check_container_health():
    print("checking for container health")