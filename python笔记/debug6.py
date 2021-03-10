import requests


def login_king(username: str, password: str, proxies: str):
    """
    登录皇冠
    :param username: 帐号
    :param password: 密码
    :return:
    """
    session = requests.session()
    session.proxies = {'http': proxies,
                       'https': proxies}
    session.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
    )
    data = {
        'username': username,
        'passwords': password,
        'langx': 'zh-cn',
        # 'auto': 'GAADAF',
        # 'blackbox': '0400E6tBivBut4bjK9GFecOQi80H7tjLo@BrZCJd36GZeAbO0ue34k@NmF7Jmb0alpSABduz6/V@VQHlo0jXgAXDSebHa83CDZB6XSMH6DcdF4cxMU/WoNLu9vOr9u52MhSGxJ9mJdLgVEWAAq@cnKwLKGizCEUlVi6spx285qKQ3aopQs/EGzmZL40jGqnvlH2yAj7p6pz/L4njUpY5tm629mtGMuSZx2KTzQfu2Muj4GtkIl3foZl4Bs7S57fiT42YXsmZvRqWlIAF27Pr9X5VAeWjSNeABcNJwKr0Mf@ogWY6D3DsjsRSNsiu7qdJERNY@59F2g7ujisgrBH5xvykmUPKtcSzTI8WFkgxCcQUbk2OWHK0IFpevahdVV6ejv2EFCcyLcmOKsEwxpVDNS4sSPnpxi5knfQyLEjP9Ek@ysqg7DiXXLCq3E6HC5jftRCVGRpAINeGe6iYzYYmEY19JhpJj1hhEbOcsyfdNj2MFusAgOh4QdvciMt/GuHpyFP1YorHgKQu64z/K9AK8/SqOWZ7@EnMfC4L6d/HnNkh/KA3koT6Hdqn9fi8fptuT4V@57LnmsP38HYt/DAN1odVqCYFUpNKXClEwgybEudID5aqDEHBx0MaguKzeqo5BsuwPljubQOyZ@ldxGNGyhUUUYuoKmLN7sWccnDB2QnB46V1G2mpGiKJ4Ao5VNMvaDXf7E1Pf46IvXtYdEyMOakFzprLKk3u1s0Iq1jEc21Hw6uz3fcDTzC/HkjXzk77ILZ/eUsQ7RNrLro1kTKIs1496YkpIh3A707lm2e25SQbo1Nbcs192pVnV2j2vlUvZqAyHKNCV/CVusXmY1XpDGBtyUYBKknoROYtYNJHJfSFZ@3gIY9aebixkgyCiDVa0KzSSe0zAMBEe5XN1/EvKVgGJuwRUFY7xdAiqlr028/3Pq98uECtRBzoupzlUmkejozSOe0RxWZbWQzqNqtge7PenRkwfCqvl92YzYwqJgJvmWth5Nwu1x6PILE@TZSSoO91gRgN@Z8HAFhGFzd/m6snVqi2XJwwQEvUjPJV6TCEjn@0@9d9ASD4otFWwM1TOcz7giVFA7zpIPQ4hLssfn3WSDtD3YUYq567IKh8cj1oeYpV8Lsfk4HM8mvRIRFr5PRtU94iY2v9RU9XqLz@1vlqUAr9dE2jcfl004eOzsc7kItlmFcayM9EEc6tWDkTnxEACXZjVj@Jpy/gAwCH1F3SoDINRCQGbbX7eF2tLN6fC/aIrukwLD3N1CfZgaIQ/SsVTEVdGJlxBwCc8acbcKqAuWf7gouzBPJaEMCy0s3hRLlX3uHnT/mMqzEnDVj65t4JMFVxXhkQTqZuUMtvhwCYVKDl1FsZY8jwFaXKqt5H5j@zoEkNBc35XGtVsYmdWtM9fyGFDb76Q8kmYue3mmS/sUVtlTUlIx7mK2/lD4vAGQ9VJUiLP0GDKsz9z5rLaEtDkYZHETw1xh1EHPNLt0VCWuVzX1ZNalmLiynsbWM73McmciECfKYTFildd0Otev4uOk9m0QVUzExD29XJJc2KIU7SZ23C7pEZC/WxDzjzcvye4BKRVkhHeph5berrRNinVZSqav@9XlSeO8siu/KoG/sSUJ/7b/PbPoJ@wzBSCeQZfbCNStXVKtYsGwEzBWgoyJkmDK0I0r0PnweHcgz/bh1EAxxzyYrJvmaaMe7e9pSea1h3/CE93R8XBMHBkbVtBSrDhNltJwWH5C623/DfTuheQMX9TUTvFdbioHX10c7z3wafI/WYHD@t9zphX3g@bZ/KaW8jWERJ2L1GMcCBwYbLk5y7tWRU3eln9a65pRAlF@pPKGFmqCKWCY0bLaB6SUpGCTU5RhA921kLz7AG6JiIyjWZf9dTMwp6u6ykuw@Ifk9ysrIpE3IGGe06JjlwgK6sPLKMle3zH5gmEfKTL@Y3rQYZsZzu8Lm3dJnCEDKiB0MS3fGKaCVIFuHF87v76OUS0/pt7LJJG4oAn3pXyERtOsyb0Gq6Hy7AwBuo0PW9PCr8EzxDKo5RksALnJ5imj/HgAHSndfYGW151M8PIPSzTtZuzh4mhE5ThIU@7E2Dchu@2lGv9V543P8ciZCxtdgH5rKvPh@FdAOmUgdEE9GLPVxxXBHwI0HK/tpL@S6MNe3lt6WlusDNh3Ni0mmTkkat@iT7qn0mt9fsfA4tXhYm56UypZLWoqAzat3COeGb1a2XkLKbQO3u5yyFq/DVa4gScXOkHdJ6mBEpsvsG@9gfSX81L6KWhl8nQ9tU2ghlbBCCXIaRajUL2jDUTOKI2d8NfFhMBTSThPpb4/n123Rnl7WkdQdvgJTtE1d2lz904hiAcL/dBgQsLD4xQlj155sIgPMzEM1umC6j4iYHxtzzlxpPlz@Pz9Ve3RDQDFzjUWxqkv7F6DGaTsaFO14M90LoskAlU/NFYeCwc8url5Fs8W4X@Xx/psQzlPJ@t@WEnQajjAk@osJxEWfxLjF@6B2ckrooaYM48ESBIcDZvvGhjIPx7zlBXQlblQT79A1@DW@uEh@PN/GhjIPx7zlB90MzKEW5vquB4cyfEeXJSd01ucAFceYWteaqqzsBHrxjvuJB7oUtpyxBBp671HWta1j2/LVD7YcpADa@yrWk51tzXxkDpL2IMNBYGfTL0tTPNV0m46npiIDX7tZxDC/7NZ0IERTEqgFJoUsgF0@jFr303Nm0HUaqWQ2jh60jcCRTJuVSvyLuRjMkfBVSkAveBZkZz0PI67V2KT4EIhFconQ@rlIMTewVhRJLGBGeFVM=;0400TjGoeoV6xmiVebKatfMjIFX26joNaH1KmxaTbmNX0Pn8i8M6BOcfE0bBBkJC0RDbTuvuaGovymPrdsVePX6iYJRvFCMSbl5xzGdSY53LTtv3DtBR5aVloipq4/eQIAw4ZOY6osDdKdFvJq7ODD65YL2ZQOAAQs7xsRxtFqaM8sL1A/CGmLYYDO7M/1GjrAwst3KlCG0MIczV4d@RnQegnNK3Sga2t5uGqOaD8lxRvFKh0HCGMBRtHCIHtiFmCY@klU99UoH2xkmiqXr@P@pMA2ogs7F@MKQjoMwFY590CjecBtc8p53hLo1YbXsov9Fd8uMM90UPIKVO1Tp84e7/t28mrs4MPrlgvZlA4ABCzvGxHG0WpozywvUD8IaYthgM7sz/UaOsDCy3cqUIbQwhzO9RJsn4u3PdHf7WUtiodkRfHKXDT4dcvBEQfNoh8wNOVGGqfWYBpwFv47mN@mlXb@bhtQqIxjoTC4ylpWh7G3G5Ufeglbz3fl@keaQIdNT5aJs4v2XRodmUS/87DU7APOt2a9la1qxSzaaWtu4XIbGgXkyvbIVWo2kXD1wvQg9ts8/f4xwsdsIS6V2DlbRuo2zTQJPV3QZ2lWGnDD@rB9WMEVdQDFhMpI72gsHP1@05ywOBMHnR8NRhG5GYWCbpzHTUKQi/6ZhLfRLCUCuqGl0CwRvkp0e1JVuaMgcE8fIqKPP7Ec@2O4THKtQyJ0pA90N13n2vmAeytJRmnJsVxcAILXKPYzpp/GO7P/zAA1mnVagB1dsnJeLd0HwZFZsoI7u4fdGNP6EcxS9GTGQ/PXGUReO78f8dn4s//BPd61qfeuNoiWMTvBwsf@xD@xeqTTINRCQGbbX7eF2tLN6fC/aIrukwLD3N1CfZgaIQ/SsVTEVdGJlxBwCc8acbcKqAuWf7gouzBPJaEMCy0s3hRLlX3uHnT/mMqzEnDVj65t4JMFVxXhkQTqZuUMtvhwCYVKDl1FsZY8jwFg79lnzS933qfcFw6EylEEJT4mnZFS18dUsprl5Sq8nl3OCiMt8Ua6LE8yqMVQun0jxRYAmjKb1P4ehBV15lxPf61/NduSTlaPa@VS9moDIO0@r@OXJLSyhoIRKccj8TvX9j17x6IHj17VBkPiWbN3nNALrQ5jJzNgpzSXcapJWds97EDLH1crAtjgzHMGAk58fx3@Rcwz0I4HEJnGOmG0vEoXq/Y8/GXhBBz3OgEm8b/j6Q87qDY9m4JivOPiYRBNe8T77DDBWWYBXtZhD6P8SmRZOWcyLm/md0MLboxU6/TDp0UzLYSzsntGrOrjOhiSkiHcDvTuVFWopiv1Rjk6BlbWMnixy0YRCREsUiSzEzqbwpmWa8I730XlOhjRFIr8BUasnqUFuLLTx8TmYiVXSw7PtSQtURBVc9B6uBWZ@bv9v5O0nh/9/7HinDpb16xsYSmrsKhFi8VDdLGBfK9PH/LgnAtMTg3G/gqjChOr20Q73jZPZeZgFaxEVmsKD2TMj6Y82LrlflYU9iUMb03QtuHmc6Pe7cNepEKIoJSuxTQRdWXuxQ4d6gjH5ZCaYNkNrAXEvbWw7IauRtCQwBH0aLtD0@WrHlBgZ3Ja/RTpg5dvlQf6oRSSEIEB4/Linj/3T03jNWh/gI1JkXIB6wRkiRlFGsxIK/d1nz7CQvK/Sf8dmkomcwGtTJl3DAk9PMAEirag/jdy4gQwNwgPz27UiffkFcjqDm0sAesCH0AfNwaqPyOuzPoGpwYWEO8Yn@YSRpyxroLsJx0hQWi3VUuGS@X0xSKnKPpz/sXLKwwBH/FfHPmIcnYaLjAvlkC6ix5GwMchIozX1AudaF09Pqoqoskd1tXFuJzWYTHlPicx4xsGw2bx4mA/lBF0aI8TPiDPWCyXC02/rz3wafI/WYHD@t9zphX3g@bZ/KaW8jWERJ2L1GMcCBwYbLk5y7tWRU3eln9a65pRAlF@pPKGFmqCKWCY0bLaB6SUpGCTU5RhBiPqUIoJ5dY0BIxggag2ev/8hg4snisnzc7NXKoCBLGyYN8k/Nd27mXJvS1dIMyhL5HMW8xkX1uc4IJCn8VPIXkLVSObSM03GiB0MS3fGKaCVIFuHF87v76OUS0/pt7LLpHnM/3kpW06Obf5TOL6v6Xk6xfbUNmXTIap7knmmuQxPxcPhHhHgx5l4X2KxLMyz/YKU5Y6iHX2ihiJuN7Is7M9Hb9NlT2cfy/GQUHG5Zv0LwoDBJ9uWF03YEpUAbE3hffyupqg2P4fZvCWBya9Y8C084g4mQKjzQmMyeGerZjJ/K@43kBr5edBVJnaWFT6YqadcV6kL3QekazlUh5hLeePo1M6Hp8zhvlj@8LEsWHlPrbmePuOfKSr8G@R/0jCpQA/0xnxZL3x54D/SGn@YEIG5fZTO8eWdoP5eBPQ@zTSyEmgN0xUu0U7oczh@iiXSHfBgfW9d1xH027Cj1QfqOHiqgVfPKC@ko06/zBHt9JOQjTrpopKIwOVavUEHOVSbEt9Uh8uyiOt09CO7kpqs9gdc4EaKRdhavketmNpZ5dZXxKVvl6jKOzhLnr69vcRNkEOwZwve2ev@t2iEWW/t/08t8E/3oSmAhpwCo1cQGrULgzcSXRgcwG5I9HSll19TO6DeYwZU@YIFkb32rQ6IzKEoGgEgONTbgD8Jq5ij/Ey2kFvVIo30LdYDEPpY0YDyzp1q0Wl2s5GhzeZgE7y7jp@8v8fie1LByoiuJDYwoMPGUIx@8A4rJF560KfYZCf1wnlsdD@@kU8GlWzo@z0yzTOclAK/aifR7WzUptLWnI0yWvGrfn0XFPhDSaV6XrD6s3XsHJna5plhM8WPnjkpYwTpqC7aOF/FFOZTREOLj/g==',
        # 'nowsite': 'new',
    }
    rsp = session.post('http://205.201.4.165/app/member/new_login.php', data=data)
    print(rsp.text)
    back_list = rsp.text.split('|')
    try:
        uid = back_list[3]
    except Exception as err:
        print(err)
    session.cookies.update({'gamePoint_23817144': '2021-02-24*0*0'})
    return session,


# 81ns8ztcm23817144l265575b0
if __name__ == '__main__':
    login_king(username='money888go', password='Wahaha82', proxies='http://47.119.136.230:59394')
    # test()
