# import torch
import argparse
import random
# import numpy as np
import yaml

# from dataset import DatasetTrain


######### Set Seeds ###########
# random.seed(1234)
# np.random.seed(1234)
# torch.manual_seed(1234)
# torch.cuda.manual_seed_all(1234)





def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='/data/h00026370/Moon/codes/EDKE/config/training.yaml', help='the path of config file')
    # parser.add_argument('')
    args = parser.parse_args()
    return args



def Config(opt, args):
    """
        A function to read config (YAML) file
    
        Parameters
        ----------
        opt:(YAML) file path
        args:the arguments for training
    
    """
    with open(opt, 'r') as f:
        cfg = yaml.load(f)
    for k, v in cfg.items():
        setattr(args, k, v)
    return cfg



def train(args):
    






if __name__ == "__main__":
    args = parse_args()
    Config(args.config, args)
    train(args)



