"""Command-line experiment runner without third-party packages."""
import argparse
import json
from genesislab.experiments import run_trial

def main():
 parser=argparse.ArgumentParser(description='GenesisLab synthetic sequential experiment')
 parser.add_argument('--seed',type=int,default=49)
 parser.add_argument('--budget',type=int,default=16)
 parser.add_argument('--policy',choices=['adaptive','random'],default='adaptive')
 args=parser.parse_args()
 print(json.dumps(run_trial(args.seed,args.budget,args.policy),indent=2))
if __name__=='__main__':main()
