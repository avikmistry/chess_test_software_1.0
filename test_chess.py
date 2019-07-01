from lib import *
from chess_exception import *
import logging
from datetime import datetime
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

test_status = {"total_tests": 0, "passed": 0, "failed": 0}


def test_invalid_move():
  """
  This tests invalid move.
  """
  boardState = [{"loc":"a9","type":"r"},{"loc":"b8","type":"n"},{"loc":"c8","type":"b"},{"loc":"d8","type":"q"},{"loc":"e8","type":"k"},{"loc":"f8","type":"b"},{"loc":"g8","type":"n"},{"loc":"h8","type":"r"},{"loc":"a7","type":"p"},{"loc":"b7","type":"p"},{"loc":"c7","type":"p"},{"loc":"d7","type":"p"},{"loc":"e7","type":"p"},{"loc":"f7","type":"p"},{"loc":"g7","type":"p"},{"loc":"h7","type":"p"},{"loc":"a1","type":"R"},{"loc":"b1","type":"N"},{"loc":"c1","type":"B"},{"loc":"d1","type":"Q"},{"loc":"f1","type":"B"},{"loc":"g1","type":"N"},{"loc":"h1","type":"R"},{"loc":"a2","type":"P"},{"loc":"b2","type":"P"},{"loc":"c2","type":"P"},{"loc":"d2","type":"P"},{"loc":"e2","type":"P"},{"loc":"f2","type":"P"},{"loc":"g2","type":"P"},{"loc":"e1","type":"K"},{"loc":"h2","type":"P"}] 
  payload = create_request_json(boardState=boardState)
  try:
    send_request(payload=payload)
  except MoveError as exc:
    log.info("invalid move, expected error :"
             "{0}".format(str(exc)))

def test_invalid_board():
  """
  This tests invalid board position.
  """
  boardState = [{"loc":"a8","type":"z"},{"loc":"b8","type":"n"},{"loc":"c8","type":"b"},{"loc":"d8","type":"q"},{"loc":"e8","type":"k"},{"loc":"f8","type":"b"},{"loc":"g8","type":"n"},{"loc":"h8","type":"r"},{"loc":"a7","type":"p"},{"loc":"b7","type":"p"},{"loc":"c7","type":"p"},{"loc":"d7","type":"p"},{"loc":"e7","type":"p"},{"loc":"f7","type":"p"},{"loc":"g7","type":"p"},{"loc":"h7","type":"p"},{"loc":"a1","type":"R"},{"loc":"b1","type":"N"},{"loc":"c1","type":"B"},{"loc":"d1","type":"Q"},{"loc":"f1","type":"B"},{"loc":"g1","type":"N"},{"loc":"h1","type":"R"},{"loc":"a2","type":"P"},{"loc":"b2","type":"P"},{"loc":"c2","type":"P"},{"loc":"d2","type":"P"},{"loc":"e2","type":"P"},{"loc":"f2","type":"P"},{"loc":"g2","type":"P"},{"loc":"e1","type":"K"},{"loc":"h2","type":"P"}]
  payload = create_request_json(boardState=boardState)
  try:
    send_request(payload=payload)
  except BoardError as exc:
    log.info("invalid board, expected error : "
             "{0}".format(str(exc)))


def test_player_cannot_make_move():
  """
  This tests if the given move can not be made by the given player.
  """
  payload = create_request_json(playerState="b")
  try:
    send_request(payload=payload)
  except MoveError as exc:
    log.info("Player can not make given move, expected error : "
             "{0}".format(str(exc)))

def test_unknown_player():
  """
  This test api, when unknow player is send in request, that is neither w or b.
  """
  payload = create_request_json(playerState="k")
  try:
    send_request(payload=payload)
  except BoardError as exc:
    log.info("Unkown player, expected error : "
             "{0}".format(str(exc)))

def test_wrong_method():
  """
  This test passes wrong method name to the api.
  """
  payload = create_request_json(method="MakeMovee")
  try:
    send_request(payload=payload)
  except ChessError as exc:
    log.info("Wrong method, expected error : "
             "{0}".format(str(exc)))

def test_method_not_specified():
  """
  This test passes no method to api request.
  """
  payload = create_request_json(method="")
  try:
    send_request(payload=payload)
  except ChessError as exc:
    log.info("Wrong method, expected error : "
             "{0}".format(str(exc)))

def test_next_player_state():
  """
  This test checks that next player state returned is as expected..
  """
  payload = create_request_json(playerState="w", move="Nc3")
  out = send_request(payload=payload)
  playerState = out["result"]["playerState"]
  assert playerState == "b"
  boardState = out["result"]["boardState"]
  payload = create_request_json(playerState="b", move="Nc6", boardState=boardState)
  out = send_request(payload=payload)
  assert out["result"]["playerState"] == "w"

def test_game_state_check():
  """
  This test checks gamestate check.
  """
  boardState = [{"loc": "a1", "type": "k"}, {"loc": "b3", "type": "Q"}, {"loc": "d1", "type": "K"}]
  payload = create_request_json(boardState=boardState, move="Qa3")
  out = send_request(payload=payload)
  assert out["result"]["gameState"] == "check","gamestate is not 'check' in response"

def test_game_state_checkmate():
  """
  This test checks gamestate checkmate.
  """
  boardState = [{"loc": "a1", "type": "k"}, {"loc": "b3", "type": "Q"}, {"loc": "c1", "type": "K"}]
  payload = create_request_json(boardState=boardState, move="Qa3")
  out = send_request(payload=payload)
  assert out["result"]["gameState"] == "checkmate","gamestate is not 'checkmate' in response"

def test_game_state_stalemate():
  """
  This test checks gamestate stalemate.
  """
  boardState = [{"loc": "h1", "type": "k"}, {"loc": "g5", "type": "Q"}, {"loc": "f7", "type": "K"}]
  payload = create_request_json(boardState=boardState, move="Qg6")
  out = send_request(payload=payload)
  assert out["result"]["gameState"] == "stalemate","gamestate is not 'stalemate' in response"

def test_invalid_player():
  """
  This tests invalid player in api request.
  """
  log.info("Testing invalid palyer in api request with json: {0}".format(default_json))
  try:
    send_request(payload=default_json)
  except PlayerError as exc:
    log.info("invalid player, failed as expected with error :"
             "{0}".format(str(exc)))

def test_api_error():
  """
  This tests invalid api request.
  """
  default_json["params"]["boardState"][0]["loc"] = "a9"
  log.info("Testing invalid api request with json: {0}".format(default_json))
  try:
    send_request(payload=default_json)
  except ApiError as exc:
    log.info("invalid api request, failed as expected with error :"
             "{0}".format(str(exc)))

def runner(test_method):
  test_status["total_tests"] = test_status["total_tests"] + 1
  log.info("**** RUNNING TEST: {0} ****".format(test_method.__name__))
  try:
    test_method()
    log.info("**** TEST PASSED: {0} passed.\n".format(test_method.__name__))
    test_status["passed"] = test_status["passed"] + 1
  except:
    log.info("**** TEST FAILED: {0} failed.\n".format(test_method.__name__))
    test_status["failed"] = test_status["failed"] + 1

if __name__=="__main__":
  runner(test_invalid_move)
  runner(test_invalid_board)
  runner(test_player_cannot_make_move)
  runner(test_unknown_player)
  runner(test_wrong_method)
  runner(test_method_not_specified)
  runner(test_game_state_check)
  runner(test_game_state_checkmate)
  runner(test_game_state_stalemate)
  runner(test_next_player_state)
  #test_invalid_player()
  #test_api_error()
  log.info("\nTotal tests = {0}, Passed = {1}, Failed = "
    "{2}".format(test_status["total_tests"], test_status["passed"], test_status["failed"]))
