
from apscheduler.schedulers.blocking import BlockingScheduler
from Base_Code_Testing import whatsapp_bc_sender

def job_function():
    print("Test Message For Whatsapp BC database")
sched = BlockingScheduler()

#Schedule job function to be called every two hours
sched.add_job(whatsapp_bc_sender, 'interval', seconds=10)

sched.start()