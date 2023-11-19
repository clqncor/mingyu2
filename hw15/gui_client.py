import PySimpleGUI as sg
import requests

def run():
    layout = [
        [sg.Text("가위 바위 보 게임")],
        [sg.Text("플레이어 선택"), sg.InputCombo(['가위', '바위', '보'], key='player_choice')],
        [sg.Button("게임 시작"), sg.Button("종료")]
    ]

    window = sg.Window("Rock Paper Scissors Game", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == '종료':
            break
        elif event == '게임 시작':
            player_choice = values['player_choice']
            play_game(player_choice)

    window.close()

def play_game(player_choice):
    response = send_request(player_choice)

    if "error" in response:
        sg.popup_error(response["error"])
    else:
        result_message = f"플레이어 선택: {response['player_choice']}\n" \
                         f"컴퓨터 선택: {response['computer_choice']}\n" \
                         f"결과: {response['result']}"
        sg.popup("게임 결과", result_message)

def send_request(player_choice):
    try:
        response = requests.get(f"http://127.0.0.1:8000/game?player_choice={player_choice}")
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Request error: {e}"}

if __name__ == "__main__":
    run()
