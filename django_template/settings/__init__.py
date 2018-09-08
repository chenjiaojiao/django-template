# -*- encoding: utf-8 -*-
# 在这里选择环境配置
DEPLOY_ENV = 'dev'

exec('from %s import *' % DEPLOY_ENV)
