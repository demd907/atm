#잔액 초기화
balance = 1000


while True: # 조건이 True면 계속 작동합니다.
    num = input('사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료): ')
    # 4를 입력하면 종료라는 출력메시지 print()를 보여주는 코드를 작성해주세요
    # 개발할때 최소한의 자원만 쓸 수 있도록 고려를 해보는게 더 좋습니다.

    #1번 입금 기능 코드
    if num == '1':
        #얼마를 입금할거야?
        deposit_amount = int(input('입금할 금액을 입력해주세요: '))
        #balance
        balance += deposit_amount #결과를 별도의 저장공간에 담아줘
        print(f'입금하신 금액은 {deposit_amount}원입니다. 현재 잔액은 {balance}원입니다.')  

    #2번 출금 기능 코드
    if num == '2':
        #얼마를 출금할거야?q
        withdraw_amount = int(input('출금할 금액을 입력해주세요: '))
        #잔액이 충분한지 확인
        #if withdraw_amount > balance:
        withdraw_amount = min(balance, withdraw_amount) #잔액이 충분한지 확인
        balance -= withdraw_amount

        if withdraw_amount > balance:
            print('잔액이 부족합니다.')
        else:
            balance -= withdraw_amount #결과를 별도의 저장공간에 담아줘
            print(f'출금하신 금액은 {withdraw_amount}원입니다. 현재 잔액은 {balance}원입니다.')


    #4번 종료 기능 코드
    if num == '4': 
        print('종료')
        break

