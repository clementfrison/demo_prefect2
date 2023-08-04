from prefect import flow
from platform import platform, node
from os import getcwd


@flow(log_prints=True)
def machine_info():
    print("platform.platform() = ", platform())
    print("platform.node() = ", node())
    print("os.getcwd() = ", getcwd())


if __name__ == "__main__":
    machine_info()
