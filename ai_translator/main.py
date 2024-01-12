import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import ArgumentParser,ConfigLoader,LOG
from model import GLMModel,OpenAIModel
from translator import PDFTranslator
if __name__=="__main__":
    argument_parser=ArgumentParser()
    args=argument_parser.parse_arguments()
    