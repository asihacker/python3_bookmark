import click


# default：给命令行选项添加默认值
# help：给命令行选项添加帮助信息
# type：指定参数的数据类型，例如int、str、float
# required：是否为必填选项，True为必填，False为非必填
# prompt：在命令行提示用户输入对应选项的信息
# nargs：指定命令行选项接收参数的个数，如果超过则会报错，不超过不报错。(默认参数 default 用list tuple 都可以哦～～)
# multiple:批量参数 设置默认的话就是list了，看下面例子  python hello.py -n asihacker -i game -i study -c 10
# required:参数是否是必须的
# hide_input:密码输入
# confirmation_prompt:确定输入 就是输入密码2次对比是不是一样的～～～

@click.command()
@click.option('--name', '-n', prompt='你的名字是什么？', help='输入你的名字', type=str, required=True)
@click.option('--birthday', '-b', default=[1995, 2, 11], nargs=3, help='输入你的具体年月日 -b 1995 2 11',
              type=(int, int, int))  # 这里可以定义每一个参数的类型
@click.option('--interest', '-i', default=['game', 'mp3', 'mp4'], multiple=True, type=str,  # type=list 你会看到不一样的结果～
              help='输入你的兴趣爱好 -i game -i study')
@click.option('--password', '-p', prompt='请输入你的密码', hide_input=True, confirmation_prompt=True, required=True,
              help='密码回帮你隐藏哦！')
@click.option('--count', '-c', default=1, help='你要打印多少次？')
@click.confirmation_option(prompt='你确定你输入的对吗?')  # ==Are you sure? [y/N]:
def hello(name, birthday, interest, password, count):
    for x in range(count):
        click.echo(f'你好，{name}!你的生日是{birthday},你的爱好是{interest},你的密码是{password}')


if __name__ == '__main__':
    hello()
# python hello.py
