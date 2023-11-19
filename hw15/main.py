import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "가위 바위 보 게임을 시작합니다."}

@app.get("/game")
def game(player_choice: str):
    valid_choices = ['가위', '바위', '보']

    if player_choice not in valid_choices:
        return {"error": "Invalid choice. Choose from '가위', '바위', '보'"}

    computer_choice = random.choice(valid_choices)
    result = determine_winner(player_choice, computer_choice)

    return {
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result
    }

def determine_winner(player, computer):
    if player == computer:
        return "무승부"
    elif (
            (player == '가위' and computer == '보') or
            (player == '바위' and computer == '가위') or
            (player == '보' and computer == '바위')
    ):
        return "플레이어 승리"
    else:
        return "컴퓨터 승리"
