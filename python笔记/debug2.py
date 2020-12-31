#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 15:23
# @Author  : AsiHacker
# @File    : debug2.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# !/usr/bin/python
# -*- coding: UTF-8 -*-


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 12:45
# @Author  : AsiHacker
# @File    : test7.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import base64
import json
import time
import uuid

import websocket
from paho.mqtt import client as mqtt
from paho.mqtt.client import mqtt_cs_disconnecting


class MqttClient(mqtt.Client):
    """facebook异步链接"""

    # headers = {
    #     'Cookie': self.cookie,
    #     'User-Agent': self.user_agent,
    #     'Origin': 'https://www.facebook.com',
    #     'Host': 'edge-chat.facebook.com'
    # }
    # username={'u': '100060616839779', 's': 2089424816643318, 'cp': 3, 'ecp': 10, 'chat_on': True, 'fg': True, 'd': 'e3570878-49d1-11eb-9dde-acde48001122', 'ct': 'websocket', 'mqtt_sid': '', 'aid': 219994525426954, 'st': [], 'pm': [], 'dc': '', 'no_auto_fg': True, 'gas': None, 'pack': []}
    # path = /chat?region=prn&sid=xxxxxxx&cid=xxxxxxxxx

    def __init__(self, path: str, username: dict, headers: dict, sequence_id: int, proxy: dict):

        super().__init__(client_id='mqttwsclient', protocol=mqtt.MQTTv31, clean_session=True, transport='websockets')
        websocket.enableTrace(False)
        self._ws = websocket.WebSocketApp("ws://161.117.252.224:9898",
                                          on_open=self.ws_on_open,
                                          on_message=self.ws_on_message,
                                          on_error=self.ws_on_error,
                                          on_close=self.ws_on_close)
        self._ping_counter = 0
        self.status = 'Connecting'
        self.tls_set()  # 开启ssl认证
        # 设置代理 http {'proxy_type': 3, 'proxy_addr': '127.0.0.1', 'proxy_port': 1087, 'proxy_username': 'user', 'proxy_password': 'pwd'}
        # 设置代理 socks5 {'proxy_type': 2, 'proxy_addr': '127.0.0.1', 'proxy_port': 1086, 'proxy_username': 'user', 'proxy_password': 'pwd'}
        self.entity_fbid = username['u']
        self.ws_set_options(path=path, headers=headers)  # 设置头部 和 cookie
        self.username_pw_set(json.dumps(username, separators=(",", ":")))  # 认证用户
        self.proxy_set(**proxy)
        self.sequence_id = sequence_id
        self.default_topics = [
            "/legacy_web",
            "/webrtc",
            "/rtc_multi",
            "/onevc",
            "/t_ms",
            "/thread_typing",
            "/orca_typing_notifications",
            "/notify_disconnect",
            "/orca_presence",
            "/br_sr",
            "/sr_res",
            "/ls_req",
        ]  # 默认订阅的Topic

    def on_connect(self, client, userdata, flags, rc):
        """
        链接mqtt
        """
        self.status = 'Connected'
        if rc == 0:
            print(self.entity_fbid, '消息队列连接成功')
            for topic in self.default_topics:
                try:
                    self.subscribe(topic, qos=0)
                    print('开始订阅主题', topic)
                except BaseException as err:
                    print(self.entity_fbid, '消息队列连接失败', err)
            self._messenger_queue_publish()
            self._notification_receive_subscribe()

    def on_message(self, client, userdata, msg):
        """
        收到消息
        """
        try:
            payload = msg.payload.decode("utf-8")
            print("raw>>>", payload)
        except ValueError:
            print("Failed parsing MQTT data on %s as JSON", msg.topic)
            return

        if msg.topic == '/t_ms':
            if "errorCode" in payload:
                error = payload["errorCode"]
                print(self.entity_fbid, '消息队列异常: ', error)
                print(self.entity_fbid, '重新建立连接')
                client.reconnect()

    def _messenger_queue_publish(self):
        payload = {
            "sync_api_version": 10,
            "max_deltas_able_to_process": 1000,
            "delta_batch_size": 500,
            "encoding": "JSON",
            "entity_fbid": self.entity_fbid
        }
        # 首次连接成功
        payload.update({
            "initial_titan_sequence_id": self.sequence_id,
            "device_params": None
        })
        self.publish('/messenger_sync_create_queue', json.dumps(payload, separators=(",", ":")), qos=1)

    def browser_close(self):
        self.publish("/browser_close", payload=b"{}", qos=1)

    def _notification_receive_subscribe(self):
        requestId = str(uuid.uuid1())
        routing_hint = '673b6d520eb7966860f2c7b70dec9230'
        actor_id = self.entity_fbid

        def make_payload(actor_id, requestId):
            source = b'{"transformContext":"{\\"viewerID\\":\\"[[actor_id]]\\",\\"appID\\":\\"0\\",\\"locale\\":\\"en-US\\",\\"queryID\\":\\"3092664784174297\\",\\"serializedQueryParameters\\":\\"{\\\\\\"input\\\\\\":{\\\\\\"environment\\\\\\":\\\\\\"MAIN_SURFACE\\\\\\",\\\\\\"client_subscription_id\\\\\\":\\\\\\"[[requestId]]\\\\\\"},\\\\\\"is_work_user\\\\\\":false,\\\\\\"scale\\\\\\":2,\\\\\\"%options\\\\\\":{\\\\\\"client_has_ods_usecase_counters\\\\\\":true}}\\",\\"useOSSResponseFormat\\":false}","locale":"en-US"}'
            rep = source.replace(b'[[actor_id]]', actor_id.encode())
            rep.replace(b'[[requestId]]', requestId.encode())
            return base64.b64encode(rep).decode()

        payload = {
            "batchId": 1,
            "frames": [
                {
                    "type": 1,
                    "request": {
                        "streamId": 1,
                        "requestType": 1,
                        "headers": {
                            "requestId": requestId,
                            "routing_hint": routing_hint,
                            "method": "FBGQLS:WEB_NOTIFICATION_RECEIVE_SUBSCRIBE",
                            "topic": f"gqls/web_notification_receive_subscribe/actor_id_{actor_id}_environment_MAIN_SURFACE"
                        },
                        "extraHeader": json.dumps({"requestId": requestId, "routing_hint": routing_hint,
                                                   "method": "FBGQLS:WEB_NOTIFICATION_RECEIVE_SUBSCRIBE",
                                                   "topic": f"gqls/web_notification_receive_subscribe/actor_id_{actor_id}_environment_MAIN_SURFACE"}),
                        "payload": make_payload(actor_id, requestId)
                    }
                }
            ]

        }
        self.publish('/br_sr', json.dumps(payload), qos=1)

    def onListening(self):
        print("Listening...")

    def _reconnect_wait(self):
        self.status = 'ReConnecting'
        if self._reconnect_delay and self._reconnect_delay > 15:
            print(self.entity_fbid, '放弃重试')
            self._thread_terminate = True
            self.disconnect()
            return

        time_func = time.time
        now = time.time()
        with self._reconnect_delay_mutex:
            if self._reconnect_delay is None:
                self._reconnect_delay = self._reconnect_min_delay
            else:
                self._reconnect_delay = min(
                    self._reconnect_delay * 2,
                    self._reconnect_max_delay,
                )

            target_time = now + self._reconnect_delay

        remaining = target_time - now
        print(self.entity_fbid, '即将重连', remaining)
        while (self._state != mqtt_cs_disconnecting
               and not self._thread_terminate
               and remaining > 0):
            time.sleep(min(remaining, 1))
            remaining = target_time - time_func()

    def on_disconnect(self, client, userdata, rc):
        """
        断开链接
        """
        if rc != 0:
            print('断开链接')

    def connect(self, **kwargs):
        """
        链接
        """
        super().connect('edge-chat.facebook.com', 443, keepalive=5)

    def listen(self, onListening=None):
        """
        启动mqtt
        """
        error_reason = None
        for i in range(3):
            try:
                self.connect()
            except Exception as e:
                error_reason = e
                print(self.entity_fbid, 'mqtt链接失败', e)
                time.sleep(3)
            else:
                break

        onListening and onListening()

        if not error_reason:
            self.loop_forever(retry_first_connection=True)
        else:
            self._exception = error_reason
            print(self.entity_fbid, 'mqtt链接失败', error_reason)

    def stop(self):
        """
        停止mqtt
        :return:
        """
        try:
            self.browser_close()
        except:
            pass
        self.disconnect()

    def _send_pingreq(self):
        """
        定时重连
        :return:
        """
        self._ping_counter += 1
        if self._ping_counter * 10 == 3600 * 4:
            print(self.entity_fbid, '每隔4小时自动重连')
            self._ping_counter = 0
            self.reconnect()
            return 0

        return super()._send_pingreq()

    def ws_on_open(self, ws):
        print(ws, '### open ###')
        self.listen(self.onListening)

    def ws_on_message(self, ws, message):
        print(ws, '### message ###', message)

        # self._ws.send('456')

    def ws_on_error(self, ws, error):
        print(ws, '### error ###', error)

    def ws_on_close(self, ws):
        print(ws, "### closed ###")

    def run(self):
        self._ws.run_forever()


if __name__ == '__main__':
    # headers = {
    #     'Cookie': 'c_user=100060616839779; datr=qKnqX8na9fKA2vozZxNnGQKn; dbln=%7B%22100060616839779%22%3A%22WloXhcCq%22%7D; dpr=2; fr=1hKozHite5vE37W5v.AWWEdhu3W7rL8NJ88aNQU3_ObxM.Bf6qmo.5L.AAA.0.0.Bf6yyi.AWVIFIwY3Cc; locale=en_US; sb=qKnqX0xMbs3KOa6stHvAnL-j; spin=r.1003140261_b.trunk_t.1609214414_s.1_v.2_; wd=1440x756; xs=8%3AjomG0_7dDQBFtg%3A2%3A1609214402%3A-1%3A-1%3A%3AAcW5o7TGnnjStjn8SSqLWDlLNyAG45dnF2dATYePHg',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    #     'Origin': 'https://www.facebook.com',
    #     'Host': 'edge-chat.facebook.com'
    # }
    # username = {'u': '100060616839779', 's': 2459824407951115, 'cp': 3, 'ecp': 10, 'chat_on': True, 'fg': True,
    #             'd': '2b0638e0-49d4-11eb-a7a7-acde48001122', 'ct': 'websocket', 'mqtt_sid': '', 'aid': 219994525426954,
    #             'st': [], 'pm': [], 'dc': '', 'no_auto_fg': True, 'gas': None, 'pack': []}
    # proxy = {'proxy_type': 3, 'proxy_addr': '127.0.0.1', 'proxy_port': 1087}
    # # proxy = {'proxy_type': 2, 'proxy_addr': '127.0.0.1', 'proxy_port': 1086}
    # test_json = {
    #     'path': '/chat?region=prn&sid=3982506796823071&cid=2b0638e0-49d4-11eb-a7a7-acde48001122',
    #     'username': username,
    #     'headers': headers,
    #     'sequence_id': 25,
    #     'proxy': proxy
    # }
    # print(json.dumps(test_json, separators=(",", ":")))
    import sys

    json_path = sys.argv[1]

    test_json = json.load(open(json_path, 'r'))
    ws = MqttClient(**test_json)
    ws.run()
