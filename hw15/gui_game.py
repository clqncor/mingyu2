import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Text("가위바위보 게임")],
    [sg.Text("플레이어 선택: "), sg.InputText(key='-PLAYER_CHOICE-'), sg.Button('게임하기')],
    [sg.Button('가위'), sg.Button('바위'), sg.Button('보')],
    [sg.Text(size=(30, 2), key='-RESULT-')],
    [sg.Text("3번 먼저 이기면 최종 승자입니다.", key='-FINAL_RESULT-')],
    [sg.Text("진행 상황: ", key='-GAME_PROGRESS-')],
]

window = sg.Window('가위 바위 보 게임', layout)

def get_computer_choice():
    import random
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return '무승부'
    elif (player_choice == '가위' and computer_choice == '보') or \
         (player_choice == '바위' and computer_choice == '가위') or \
         (player_choice == '보' and computer_choice == '바위'):
        return '플레이어 승리'
    else:
        return '컴퓨터 승리'

player_wins = 0
computer_wins = 0
rounds_played = 0

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    if event == '게임하기' and (player_wins <= 2 and computer_wins <= 2):
        player_choice = values['-PLAYER_CHOICE-']
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        if result:
            if result == '플레이어 승리':
                player_wins += 1
            elif result == '컴퓨터 승리':
                computer_wins += 1
            rounds_played += 1

            if player_wins > 2:
                window['-FINAL_RESULT-'].update("최종 승자: 플레이어")
            elif computer_wins > 2:
                window['-FINAL_RESULT-'].update("최종 승자: 컴퓨터")

            window['-RESULT-'].update(f"플레이어: {player_choice}, 컴퓨터: {computer_choice}, 결과: {result}")
            window['-GAME_PROGRESS-'].update(f"진행 상황: {player_wins}승 {computer_wins}패")

            if player_wins > 2 or computer_wins > 2:
                sg.popup("게임이 종료되었습니다.")
                break

    elif event in ('가위', '바위', '보') and (player_wins <= 2 and computer_wins <= 2):
        player_choice = event
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        if result:
            if result == '플레이어 승리':
                player_wins += 1
            elif result == '컴퓨터 승리':
                computer_wins += 1

            rounds_played += 1

            if player_wins > 2:
                window['-FINAL_RESULT-'].update("최종 승자: 플레이어")
            elif computer_wins > 2:
                window['-FINAL_RESULT-'].update("최종 승자: 컴퓨터")

            window['-RESULT-'].update(f"플레이어: {player_choice}, 컴퓨터: {computer_choice}, 결과: {result}")
            window['-GAME_PROGRESS-'].update(f"진행 상황: {player_wins}승 {computer_wins}패")

            if player_wins > 2 or computer_wins > 2:
                sg.popup("게임이 종료되었습니다.")
                break

window['-PLAYER_CHOICE-'].update(disabled=True)
window['게임하기'].update(disabled=True)
window.close()
