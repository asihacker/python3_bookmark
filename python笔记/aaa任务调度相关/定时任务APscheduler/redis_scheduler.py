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
                           host='127.0.0.1',
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
job_defaults = {
    'coalesce': True,
    # 当由于某种原因导致某个job积攒了好几次没有实际运行（比如说系统挂了5分钟后恢复，有一个任务是每分钟跑一次的，
    # 按道理说这5分钟内本来是“计划”运行5次的，但实际没有执行），如果coalesce为True，
    # 下次这个job被submit给executor时，只会执行1次，也就是最后这次，如果为False，
    # 那么会执行5次（不一定，因为还有其他条件，看后面misfire_grace_time的解释）
    'max_instances': 1000,
    # 就是说同一个job同一时间最多有几个实例再跑，比如一个耗时10分钟的job，被指定每分钟运行1次，
    # 如果我们max_instance值为5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了。
    # 默认情况下同一个job，只允许一个job实例运行。这在某个job在下次运行时间到达之后仍未执行完毕时，能达到控制的目的。
    # 你也可以该变这一行为，在你调用add_job时可以传递max_instances=5来运行同时运行同一个job的5个job实例。
    'misfire_grace_time': 30
    # 设想和上述coalesce类似的场景，如果一个job本来14:00有一次执行，但是由于某种原因没有被调度上，
    # 现在14:01了，这个14:00的运行实例被提交时，会检查它预订运行的时间和当下时间的差值（这里是1分钟），
    # 大于我们设置的30秒限制，那么这个运行实例不会被执行。
}

scheduler = TornadoScheduler(job_defaults=job_defaults, jobstores=job_store)  # 实例化调度器，这里使用的是redis的作为存储器的调度器。


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
