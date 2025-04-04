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
    command="docker build -t devops-test ."
    output= run_command(command)
    print(output)

def run_docker_container():
    print ("running docker container")
    command="docker run -d -p 5000:5000 --name devops_test_container devops-test"
    output= run_command(command)
    print(output)

def wait_for_container():
    print("waiting for the container")
    time.sleep(5)

def check_container_health():
    print("checking for container health")
    command= "curl -s http://localhost:5000"
    output=run_command(command)
    exp="Hello, people of this world"
    if exp in output.strip():
        print("application is running successfully")
    else:
        print("Error: application did not respond correctly.")

def cleanup():
    print("cleaning docker container ...")
    run_command("docker stop devops_test_container")
    run_command("docker rm devops_test_container")
    print("cleanup Completed!")

def main():
    build_docker_img()
    run_docker_container()
    wait_for_container()
    check_container_health()
    wait_for_container()
    cleanup()

if __name__ == "__main__":
    main()