import os
from functools import singledispatchmethod

import yaml


class ServicesInventory:
    """
        inventory结构说明:
        services:                          # 辅测服务集合:【固定关键字】【类型：字典】
         xxx_server:                      # 服务类型【自定义项】
           protocol: ssh                  # 服务连接的协议类型【固定关键字】【必填项】【类型：字符串】
           conf_group:                    # 配置组：【固定关键字】【非必填】【类型：字典】:提供配置组模板
             defaults: &ftp_defaults      # 默认配置模板，“ftp_defaults”配置模板名称，配置信息可以通过配置模板名称进行引用，语法为“<<: *ftp_defaults”
               address: 127.0.0.1
               port: ""                   # 配置信息
               user: ""                   # 配置信息
               passwd: ""
           queries:                       # 服务的连接集合【固定关键字】【必填】【类型：】。服务的目标集合配置为【目标地址@别名】别名用来关联配置组，没有别名则使用ip地址进行配置组关联。
             alias:                        # 连接别名【自定义字段】，后期使用别名来创建链接
               address: 172.18.6.90        # 连接的地址【必填】，如果定义链接项则地址为必填项。
               <<: *ftp_defaults           # 引用配置模板
               port: "433"                 # 专有配置修改

        ----------------------------------------------------------------
    """

    def __init__(self, inventory: dict, service_groups=None):
        self.inventory = inventory["services"]  # 需要修改直接字典传递
        self.service_groups = service_groups or {}
        self._group_inventory = {}

    def get_query_config(self, category, alias):
        service_category = self.inventory.get(category.value, {})
        if service := service_category["queries"].get(alias, {}):
            return service
        else:
            return {}

    def get_inventory(self):
        return self.inventory

    @singledispatchmethod
    def get_group_inventory(self, name):
        raise NotImplementedError("Unsupported types")

    @staticmethod
    def new_from_file(file):
        if not os.path.exists(file):
            inventory = None
        else:
            with open(file, "r", encoding="utf-8") as f:
                cfg = yaml.safe_load(f)
                inventory = ServicesInventory(cfg)
        return inventory
