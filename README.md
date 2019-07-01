# Chess Test Software 1.0

We will keep on adding new test cases.

This test software is for chess game at http://chesstest.solidfire.net:8080/json-rpc

# Software design:

1. Tests are written in test_chess.py file.
2. lib.py file all the required libraries.
3. chess_exception.py file has all the custom exceptions.

# To run the tests:

1. pip install requirements.txt
2. run command "python test_chess.py", you will get the output on console as
   well as in log file inside log folder.

# Sample output of tests including test case names:
```
avik git:(master) ✗ python test_chess.py
2019-07-01 22:02:46,512 - __main__ - INFO - **** RUNNING TEST: test_invalid_move ****
2019-07-01 22:02:46,513 - lib - INFO - Sending request to http://chesstest.solidfire.net:8080/json-rpc with json: {'jsonrpc': '2.0', 'params': {'playerState': 'w', 'move': 'Nc3', 'boardState': [{'loc': 'a9', 'type': 'r'}, {'loc': 'b8', 'type': 'n'}, {'loc': 'c8', 'type': 'b'}, {'loc': 'd8', 'type': 'q'}, {'loc': 'e8', 'type': 'k'}, {'loc': 'f8', 'type': 'b'}, {'loc': 'g8', 'type': 'n'}, {'loc': 'h8', 'type': 'r'}, {'loc': 'a7', 'type': 'p'}, {'loc': 'b7', 'type': 'p'}, {'loc': 'c7', 'type': 'p'}, {'loc': 'd7', 'type': 'p'}, {'loc': 'e7', 'type': 'p'}, {'loc': 'f7', 'type': 'p'}, {'loc': 'g7', 'type': 'p'}, {'loc': 'h7', 'type': 'p'}, {'loc': 'a1', 'type': 'R'}, {'loc': 'b1', 'type': 'N'}, {'loc': 'c1', 'type': 'B'}, {'loc': 'd1', 'type': 'Q'}, {'loc': 'f1', 'type': 'B'}, {'loc': 'g1', 'type': 'N'}, {'loc': 'h1', 'type': 'R'}, {'loc': 'a2', 'type': 'P'}, {'loc': 'b2', 'type': 'P'}, {'loc': 'c2', 'type': 'P'}, {'loc': 'd2', 'type': 'P'}, {'loc': 'e2', 'type': 'P'}, {'loc': 'f2', 'type': 'P'}, {'loc': 'g2', 'type': 'P'}, {'loc': 'e1', 'type': 'K'}, {'loc': 'h2', 'type': 'P'}]}, 'method': 'MakeMove', 'id': 1}
2019-07-01 22:02:53,243 - lib - INFO - Response: {u'id': 1, u'error': {u'message': u'Invalid vertical coordinate.', u'code': -32020, u'data': u'9'}}
2019-07-01 22:02:53,243 - __main__ - INFO - invalid move, expected error :Invalid vertical coordinate.
2019-07-01 22:02:53,244 - __main__ - INFO - **** TEST PASSED: test_invalid_move passed.

2019-07-01 22:02:53,244 - __main__ - INFO - **** RUNNING TEST: test_invalid_board ****
2019-07-01 22:02:53,725 - __main__ - INFO - **** TEST PASSED: test_invalid_board passed.

2019-07-01 22:02:53,725 - __main__ - INFO - **** RUNNING TEST: test_player_cannot_make_move ****
2019-07-01 22:02:54,209 - __main__ - INFO - **** TEST PASSED: test_player_cannot_make_move passed.

2019-07-01 22:02:54,209 - __main__ - INFO - **** RUNNING TEST: test_unknown_player ****
2019-07-01 22:02:54,689 - __main__ - INFO - **** TEST PASSED: test_unknown_player passed.

2019-07-01 22:02:54,689 - __main__ - INFO - **** RUNNING TEST: test_wrong_method ****
2019-07-01 22:02:55,178 - __main__ - INFO - **** TEST PASSED: test_wrong_method passed.

2019-07-01 22:02:55,179 - __main__ - INFO - **** RUNNING TEST: test_method_not_specified ****
2019-07-01 22:02:55,736 - __main__ - INFO - **** TEST PASSED: test_method_not_specified passed.

2019-07-01 22:02:55,737 - __main__ - INFO - **** RUNNING TEST: test_game_state_check ****
2019-07-01 22:02:56,222 - __main__ - INFO - **** TEST PASSED: test_game_state_check passed.

2019-07-01 22:02:56,222 - __main__ - INFO - **** RUNNING TEST: test_game_state_checkmate ****
2019-07-01 22:02:56,707 - __main__ - INFO - **** TEST PASSED: test_game_state_checkmate passed.

2019-07-01 22:02:56,708 - __main__ - INFO - **** RUNNING TEST: test_game_state_stalemate ****
2019-07-01 22:02:57,191 - __main__ - INFO - **** TEST FAILED: test_game_state_stalemate failed.

2019-07-01 22:02:57,191 - __main__ - INFO - **** RUNNING TEST: test_next_player_state ****
2019-07-01 22:02:58,159 - __main__ - INFO - **** TEST PASSED: test_next_player_state passed.

2019-07-01 22:02:58,160 - __main__ - INFO -
Total tests = 10, Passed = 9, Failed = 1
➜  avik git:(master) ✗
```
