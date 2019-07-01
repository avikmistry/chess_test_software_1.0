import requests
import json
import time
from datetime import datetime
import sys
from chess_exception import *

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log_file = "./log/test_chess_{0}.log".format(datetime.now().strftime("%Y%m%d-%H%M%S"))
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
log.addHandler(file_handler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)

def create_request_json(method=None, boardState=None, move=None,
      playerState=None):
  """
  This method creates json for chess.
  Args:
    method(str): Method to be used for request.
    boardState(list): boardState to be used in request params.
    move(str): Move to be made by a player.
    playerState(str): Either white or black.
    id(int): Id to be used in request.
    jsonrpc(str): json rpc version to be used.
  Returns:
    dict, updated json based on the arguments.
  """
  default_json = {"method":"MakeMove","params":{"boardState":[{"loc":"a8","type":"r"},{"loc":"b8","type":"n"},{"loc":"c8","type":"b"},{"loc":"d8","type":"q"},{"loc":"e8","type":"k"},{"loc":"f8","type":"b"},{"loc":"g8","type":"n"},{"loc":"h8","type":"r"},{"loc":"a7","type":"p"},{"loc":"b7","type":"p"},{"loc":"c7","type":"p"},{"loc":"d7","type":"p"},{"loc":"e7","type":"p"},{"loc":"f7","type":"p"},{"loc":"g7","type":"p"},{"loc":"h7","type":"p"},{"loc":"a1","type":"R"},{"loc":"b1","type":"N"},{"loc":"c1","type":"B"},{"loc":"d1","type":"Q"},{"loc":"f1","type":"B"},{"loc":"g1","type":"N"},{"loc":"h1","type":"R"},{"loc":"a2","type":"P"},{"loc":"b2","type":"P"},{"loc":"c2","type":"P"},{"loc":"d2","type":"P"},{"loc":"e2","type":"P"},{"loc":"f2","type":"P"},{"loc":"g2","type":"P"},{"loc":"e1","type":"K"},{"loc":"h2","type":"P"}],"move":"Nc3","playerState":"w"},"id":1,"jsonrpc":"2.0"}
  if method is not None:
    default_json["method"] = method
  if boardState is not None:
    default_json["params"]["boardState"] = boardState
  if move is not None:
    default_json["params"]["move"] = move
  if playerState is not None:
    default_json["params"]["playerState"] = playerState
  return default_json

def send_request(payload={}):
  """
  This method is wrapper method for api request.
  Args:
    payload(dict): payload to be used in api request.
  Returns:
    json, Api response.
  """

  URL = "http://chesstest.solidfire.net:8080/json-rpc"
  log.info("Sending request to {0} with json: {1}".format(URL, payload))
  r = requests.post(URL, json=payload, verify=False, headers={'Content-Type': 'application/json'})
  #r = requests.post(URL, data=json.dumps(payload), verify=False, headers={'Content-Type': 'application/json'})
  out = r.json()
  log.info("Response: {0}".format(out))
  check_error(out)
  return out

def check_error(out):
  """
  This method checks for the errors in api response.
  Args:
    out(json): Json response of the api request.
  Returns:
    None, if there is no error.
  """
  if "error" in out:
    err_code = out["error"]["code"]
    if err_code == -32000:
      raise BoardError(out["error"]["message"])
    elif err_code == -32010:
      raise PlayerError(out["error"]["message"])
    elif err_code == -32020:
      raise MoveError(out["error"]["message"])
    elif err_code == -32030:
      raise ApiError(out["error"]["message"])
    else:
      raise ChessError(out["error"]["message"])
  else:
    return

if __name__=="__main__":
  log.info(send_request())
