#!/usr/bin/python
# coding=utf-8
import datetime
from apscheduler.jobstores.redis import RedisJobStore
import tornado.ioloop
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.tornado import TornadoScheduler


job_store = {
    'redis': RedisJobStore(db=15,
                           jobs_key='apscheduler.jobs',
                           run_times_key='apscheduler.run_times',
                           host='redis.fqwang.net',
                           port='6379',
                           password='nantian888',
                           )
    # 'redis': RedisJobStore(db=15,
    #                        jobs_key='apscheduler.jobs',
    #                        run_times_key='apscheduler.run_times',
    #                        host='redis.fqwang.net',
    #                        port='6379',
    #                        password='nantian888',
    #                        )
    # 'redis': RedisJobStore(db=15,
    #                        jobs_key='apscheduler.jobs',
    #                        run_times_key='apscheduler.run_times',
    #                        host='redis.fqwang.net',
    #                        port='6379',
    #                        password='nantian888',
    #                        )
    # TODO:这里可以导入多个不同类型的存储对象。然后在下面实例化的时候加入对应参数就可以了。目前是redis的demo。
}

scheduler = TornadoScheduler(jobstores=job_store)  # 实例化调度器，这里使用的是redis的作为存储器的调度器。


def redis_job(key: str):
    print('test', key)
    pass


jobtime = datetime.datetime.now() + datetime.timedelta(seconds=1)
scheduler.add_job(func=redis_job,
                  trigger='interval',  # 触发器（date,cron,interval有3种）
                  args=['hahahah'],  # func的参数
                  id='firstjob',  # 定时任务的id，设置replace_existing = True 那么重复id就替换，反之亦然。
                  replace_existing=True,  # 看上一行。
                  jobstore='redis',  # 存储器
                  next_run_time=jobtime)

scheduler.start()  # 阻塞调度器，可以通过一条线程去调用。
tornado.ioloop.IOLoop.instance().start()
print('777')
