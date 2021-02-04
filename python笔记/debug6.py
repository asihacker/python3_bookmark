# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = test_from_dict(json.loads(json_string))
import json
from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast
from uuid import UUID
from datetime import datetime
import dateutil.parser

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Test:
    id: Optional[int] = None
    uuid: Optional[UUID] = None
    username: Optional[str] = None
    password: Optional[str] = None
    alias: Optional[str] = None
    grade: Optional[int] = None
    status: Optional[int] = None
    create_time: Optional[datetime] = None
    is_distribution: Optional[int] = None
    is_distribution_chat: Optional[int] = None
    is_auto_reply: Optional[int] = None
    is_auto_reply_chat: Optional[int] = None
    is_keyword: Optional[int] = None
    is_keyword_chat: Optional[int] = None
    is_hide_moblie: Optional[int] = None
    is_online: Optional[int] = None
    is_upload: Optional[int] = None
    is_delete: Optional[int] = None
    order_order_id: Optional[str] = None
    is_release: Optional[int] = None
    is_auto_trans: Optional[int] = None
    is_auto_trans_chat: Optional[int] = None
    staff_id: Optional[int] = None
    cnt: Optional[int] = None
    items: Optional[List[Any]] = None
    order_status: Optional[int] = None
    is_upload_updating: Optional[bool] = None
    is_deleting: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Test':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        uuid = from_union([lambda x: UUID(x), from_none], obj.get("uuid"))
        username = from_union([from_str, from_none], obj.get("username"))
        password = from_union([from_str, from_none], obj.get("password"))
        alias = from_union([from_str, from_none], obj.get("alias"))
        grade = from_union([from_int, from_none], obj.get("grade"))
        status = from_union([from_int, from_none], obj.get("status"))
        create_time = from_union([from_datetime, from_none], obj.get("create_time"))
        is_distribution = from_union([from_int, from_none], obj.get("is_distribution"))
        is_distribution_chat = from_union([from_int, from_none], obj.get("is_distribution_chat"))
        is_auto_reply = from_union([from_int, from_none], obj.get("is_auto_reply"))
        is_auto_reply_chat = from_union([from_int, from_none], obj.get("is_auto_reply_chat"))
        is_keyword = from_union([from_int, from_none], obj.get("is_keyword"))
        is_keyword_chat = from_union([from_int, from_none], obj.get("is_keyword_chat"))
        is_hide_moblie = from_union([from_int, from_none], obj.get("is_hide_moblie"))
        is_online = from_union([from_int, from_none], obj.get("is_online"))
        is_upload = from_union([from_int, from_none], obj.get("is_upload"))
        is_delete = from_union([from_int, from_none], obj.get("is_delete"))
        order_order_id = from_union([from_str, from_none], obj.get("order_order_id"))
        is_release = from_union([from_int, from_none], obj.get("is_release"))
        is_auto_trans = from_union([from_int, from_none], obj.get("is_auto_trans"))
        is_auto_trans_chat = from_union([from_int, from_none], obj.get("is_auto_trans_chat"))
        staff_id = from_union([from_int, from_none], obj.get("staff_id"))
        cnt = from_union([from_int, from_none], obj.get("cnt"))
        items = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("items"))
        order_status = from_union([from_int, from_none], obj.get("order_status"))
        is_upload_updating = from_union([from_bool, from_none], obj.get("isUploadUpdating"))
        is_deleting = from_union([from_bool, from_none], obj.get("isDeleting"))
        return Test(id, uuid, username, password, alias, grade, status, create_time, is_distribution,
                    is_distribution_chat, is_auto_reply, is_auto_reply_chat, is_keyword, is_keyword_chat,
                    is_hide_moblie, is_online, is_upload, is_delete, order_order_id, is_release, is_auto_trans,
                    is_auto_trans_chat, staff_id, cnt, items, order_status, is_upload_updating, is_deleting)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["uuid"] = from_union([lambda x: str(x), from_none], self.uuid)
        result["username"] = from_union([from_str, from_none], self.username)
        result["password"] = from_union([from_str, from_none], self.password)
        result["alias"] = from_union([from_str, from_none], self.alias)
        result["grade"] = from_union([from_int, from_none], self.grade)
        result["status"] = from_union([from_int, from_none], self.status)
        result["create_time"] = from_union([lambda x: x.isoformat(), from_none], self.create_time)
        result["is_distribution"] = from_union([from_int, from_none], self.is_distribution)
        result["is_distribution_chat"] = from_union([from_int, from_none], self.is_distribution_chat)
        result["is_auto_reply"] = from_union([from_int, from_none], self.is_auto_reply)
        result["is_auto_reply_chat"] = from_union([from_int, from_none], self.is_auto_reply_chat)
        result["is_keyword"] = from_union([from_int, from_none], self.is_keyword)
        result["is_keyword_chat"] = from_union([from_int, from_none], self.is_keyword_chat)
        result["is_hide_moblie"] = from_union([from_int, from_none], self.is_hide_moblie)
        result["is_online"] = from_union([from_int, from_none], self.is_online)
        result["is_upload"] = from_union([from_int, from_none], self.is_upload)
        result["is_delete"] = from_union([from_int, from_none], self.is_delete)
        result["order_order_id"] = from_union([from_str, from_none], self.order_order_id)
        result["is_release"] = from_union([from_int, from_none], self.is_release)
        result["is_auto_trans"] = from_union([from_int, from_none], self.is_auto_trans)
        result["is_auto_trans_chat"] = from_union([from_int, from_none], self.is_auto_trans_chat)
        result["staff_id"] = from_union([from_int, from_none], self.staff_id)
        result["cnt"] = from_union([from_int, from_none], self.cnt)
        result["items"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.items)
        result["order_status"] = from_union([from_int, from_none], self.order_status)
        result["isUploadUpdating"] = from_union([from_bool, from_none], self.is_upload_updating)
        result["isDeleting"] = from_union([from_bool, from_none], self.is_deleting)
        return result


def test_from_dict(s: Any) -> Test:
    return Test.from_dict(s)


def test_to_dict(x: Test) -> Any:
    return to_class(Test, x)


if __name__ == '__main__':
    result = test_from_dict(json.loads('{"id":124948,"uuid":"0dce4cd2-a005-11ea-9657-00163e01407d","username":"xiwei13210","password":"xiwei132","alias":"xiwei1321111","grade":3,"status":1,"create_time":"2021-02-03 17:04:22","is_distribution":1,"is_distribution_chat":1,"is_auto_reply":1,"is_auto_reply_chat":1,"is_keyword":0,"is_keyword_chat":0,"is_hide_moblie":1,"is_online":0,"is_upload":0,"is_delete":0,"order_order_id":"21030213021","is_release":0,"is_auto_trans":0,"is_auto_trans_chat":1,"staff_id":124948,"cnt":0,"items":[],"order_status":20,"isUploadUpdating":false,"isDeleting":false}'))
    pass