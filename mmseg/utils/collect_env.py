'''
Copyright (C) 2010-2022 Alibaba Group Holding Limited.
This file is modified from:
https://github.com/open-mmlab/mmsegmentation/blob/master/mmseg/utils/colect_env.py
'''
from mmcv.utils import collect_env as collect_base_env
from mmcv.utils import get_git_hash

import mmseg


def collect_env():
    """Collect the information of the running environments."""
    env_info = collect_base_env()
    env_info['MMSegmentation'] = f'{mmseg.__version__}+{get_git_hash()[:7]}'

    return env_info


if __name__ == '__main__':
    for name, val in collect_env().items():
        print('{}: {}'.format(name, val))
