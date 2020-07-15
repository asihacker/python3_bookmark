import asyncio
import json
import datetime
import threading
from queue import Queue

from asyn与wait与yeild.zhenji.aes_secure import AESCipher


class StreamClient(object):
    def __init__(self, host: str, port: int, heartbeat_int: int):
        self.host = host
        self.port = port
        self.heartbeat_int = heartbeat_int
        self.loop = asyncio.get_event_loop()
        # self.loop = asyncio.new_event_loop()
        self.sequence_number = 1
        self.cipher = AESCipher('0123456789abcdef0123456789abcdef'.encode())
        self.reader = None
        self.writer = None
        self.encrypt = False
        self.queue = Queue()

    def start(self):
        self.loop.run_until_complete(self._run())

    def _write_message(self, prototype: int, clear: str):
        message = bytearray()
        message.extend(self.sequence_number.to_bytes(4, byteorder='little', signed=False))
        message.extend(prototype.to_bytes(1, byteorder='little', signed=True))
        message.extend(clear.encode())

        # print('before encrypt: %s' % message.hex())
        if self.encrypt:
            message = self.cipher.encrpyt(message)
        # print('after encrypt: %s' % message.hex())

        self.sequence_number += 1

        result = bytearray()
        result.extend((4 + len(message)).to_bytes(4, byteorder='little', signed=True))
        result.extend(message)
        print(threading.current_thread().name, 'write', clear)
        self.writer.write(result)

    async def _read_message(self):
        body_length = await self.reader.readexactly(4)
        body_length = int.from_bytes(body_length, byteorder='little', signed=False)
        body = await self.reader.readexactly(body_length - 4)

        if self.encrypt:
            body = self.cipher.decrypt(body)
        return int.from_bytes(body[4:5], byteorder='little', signed=False), body[5:]

    def _change_resolution(self, width, height):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'ResolutionEvent',
                'data': json.dumps({
                    'ScreenWindowWidth': width,
                    'ScreenWindowHeight': height
                })
            })
        }))

    def _get_installed_apps(self):
        self.queue.put([-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'GetInstalledAppsAction'
            })
        })])
        # self._write_message(-127, json.dumps({
        #     'cmd': 65,
        #     'data': json.dumps({
        #         'type': 'GetInstalledAppsAction'
        #     })
        # }))

    def _install_app(self, packageName, versionCode, downloadUrl, selfStarting):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'InstallAppAction',
                'data': json.dumps({
                    'packageName': packageName,
                    'versionCode': versionCode,
                    'downloadUrl': downloadUrl,
                    'selfStarting': selfStarting
                })
            })
        }))

    def _reboot(self):
        self.queue.put([-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'RebootAction'
            })
        })])

        # self._write_message(-127, json.dumps({
        #     'cmd': 65,
        #     'data': json.dumps({
        #         'type': 'RebootAction'
        #     })
        # }))

    def _launch_app(self, packageName):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'LaunchAppAction',
                'data': json.dumps({
                    'packageName': packageName
                })
            })
        }))

    def _kill_app(self, packageName):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'KillAppAction',
                'data': json.dumps({
                    'packageName': packageName
                })
            })
        }))

    def _set_time(self):
        self.queue.put([-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'TimeEvent',
                'data': (datetime.datetime.now() + datetime.timedelta(hours=1)).astimezone(
                    datetime.timezone(datetime.timedelta(hours=8))).strftime(
                    '%Y-%m-%d %H:%M:%S:000,%Z')
            })
        })])

    def _get_adb_log(self, max_lines):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'GetLogAction',
                'data': max_lines,
            })
        }))

    def _get_screenshot(self):
        self.queue.put([-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'TakeScreenshotAction',
            })
        })])
        # self._write_message(-127, json.dumps({
        #     'cmd': 65,
        #     'data': json.dumps({
        #         'type': 'TakeScreenshotAction',
        #     })
        # }))

    def _change_info(self, data):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'ChangeInfoAction',
                'data': json.dumps(data),
            })
        }))

    def _restore_original_info(self):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'RestoreOriginalInfo',
            })
        }))

    def _send_keyevent(self, key_code, key_action):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'KeyEvent',
                "data": json.dumps({
                    "keyCode": key_code,
                    "keyAction": key_action
                })
            })
        }))

    def _send_touchevent(self, action_type, x, y):
        self._write_message(-127, json.dumps({
            'cmd': 65,
            'data': json.dumps({
                'type': 'TouchEvent',
                "data": [{
                    "actionType": action_type,
                    "id": 0,
                    "x": x,
                    "y": y,
                }]
            })
        }))

    async def _send_click_event(self, x, y):
        self._send_touchevent(0, x, y)
        await asyncio.sleep(0.1)
        self._send_touchevent(1, x, y)

    async def _send_scroll_up(self, steps, step_size=50):
        # down
        self._send_touchevent(0, 540, 950)
        await asyncio.sleep(0.1)
        for i in range(steps):
            # move
            self._send_touchevent(2, 540, 950 - i * step_size)
            await asyncio.sleep(0.1)
        # up
        self._send_touchevent(1, 540, 950 - steps * step_size)

    async def _run(self):
        print('socket', threading.current_thread().name)
        await self.get_client()

        logon_result = await self.logon()
        if logon_result:
            self.loop.create_task(self._start_heartbeat())
            self.loop.create_task(self._queue_send())

            # self._change_info({
            #     "gsm.version.baseband": "MOLY.LR12A.R3.MP.V32.2",
            #     "ro.hardware": "mt6765",
            #     "ro.build.fingerprint": "alps/full_yk919_lwg65_32/yk919_lwg65_32:8.1.0/O11019/1580268964:userdebug/test-keys",
            #     "ro.product.board": "",
            #     "ro.board.platform": "mt6765",
            #     "ro.build.version.codename": "REL",
            #     "ro.product.cpu.abi": "armeabi-v7a",
            #     "ro.product.device": "yk919_lwg65_32",
            #     "ro.build.characteristics": "default",
            #     "ro.product.model": "yk919_lwg65_32",
            #     "ro.build.host": "wish-ThinkPad-X390",
            #     "ro.build.version.incremental": "1580268964",
            #     "ro.build.tags": "test-keys",
            #     "ro.build.type": "userdebug",
            #     "ro.build.user": "wish",
            #     "ro.build.display.id": "ifull_yk919_lwg65_32-userdebug 8.1.0 O11019 1580268964 test-keys",
            #     "ro.product.manufacturer": "alps",
            #     "ro.product.name": "full_yk919_lwg65_32",
            #     "ro.serialno": "0123456789ABCDEF",
            #     "ro.sf.lcd_density": "240",
            #     "ro.product.brand": "alps",
            #     "ro.build.version.release": "8.1.0",
            #     'simMcc': '460',
            #     'simMnc': '00',
            #     'imsi': '',
            #     'imei1': '354765085303335',
            #     'imei2': '354765085303333',
            #     'meid1': '354765085303335',
            #     'meid2': '354765085303333',
            #     'wifimac': 'b8:d7:af:7a:99:47',
            #     'btmac': 'b4:bf:f6:76:66:b2',
            # })

            try:
                while True:
                    prototype, body = await self._read_message()
                    print(f'prototype,body > {prototype},{body}')
                    if prototype == 4 or prototype == 5:
                        print('> get heartbeat')

                        # self.loop.call_soon(self._get_installed_apps)

                        continue

                    if prototype == 128:
                        try:
                            body_str = body.decode('utf-8')
                        except:
                            body_str = body.hex()

                        print('get message, prototype: %s, message: %s' % (prototype, body_str))
                    elif prototype == 129:
                        with open('screenshot.png', 'wb') as f:
                            f.write(body)
                        print('get screenshot saved to screenshot.png')

            except KeyboardInterrupt:
                print('Closing connection with server...')
                self.writer.close()
                self.loop.close()
        else:
            print('Logon unsuccessful, closing connection with server...')
            self.writer.close()
            self.loop.close()

    async def get_client(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port, loop=self.loop)

    async def _start_heartbeat(self):
        while True:
            print(threading.current_thread().name, '> Sending heartbeat...')
            self._write_message(3, json.dumps({'cmd': 14}))
            # self._set_time()
            await asyncio.sleep(self.heartbeat_int)

    async def logon(self):
        print('Sending handshake')
        self._write_message(1, json.dumps({
            "cmd": 54,
            "handshake": "hello cloudphone",
            "token": 'ffff00112233445566778899aabbccddeeff0000',
            "device_id": "0000800000000000040010",
        }))

        prototype, body = await self._read_message()

        if prototype == 2:
            # login response
            error_code = int.from_bytes(body, byteorder='little', signed=True)
            print('login response, error code: %s' % error_code)
            if error_code != 0:
                self.writer.close()
                return False
            else:
                self.encrypt = True
                return True

        return False

    async def _queue_send(self):
        while True:
            if not self.queue.empty():
                args = self.queue.get()
                print(threading.current_thread().name, '> Sending queue...', args)
                if args:
                    self._write_message(*args)
            await asyncio.sleep(1)


if __name__ == '__main__':
    a = StreamClient('47.93.37.9', 7200, 3)
    threading.Thread(target=a.start).start()
