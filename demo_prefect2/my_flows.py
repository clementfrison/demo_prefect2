from prefect import task, flow, pause_flow_run
from platform import platform, node
from os import getcwd


@flow(log_prints=True)
def machine_info():
    print("platform.platform() = ", platform())
    print("platform.node() = ", node())
    print("os.getcwd() = ", getcwd())



@task
async def step1():
    return "step1"
@task
async def step2():
    return "step2"
@flow(log_prints=True)
async def basic_flow_with_waiting():
    await step1()
    await pause_flow_run()
    await step2()



# if __name__ == "__main__":
#     machine_info()
#     basic_flow_with_waiting()
