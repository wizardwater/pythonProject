import re
custlist=[]
page=-1


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()

    if choice=="I":        
        print("고객 정보 입력")
        # 성별, 이메일, 생년월일 입력받기
        while True:
            gender= input("성별을 입력해주세요 M / F ").upper()

            if gender in ('M', 'F'):
                break
        
        regex = re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,10}.[a-z]{2,10}')
                
        while True:
            email = input("이메일을 입력해주세요 ")
            # conf =re.search('@',email)
            check =regex.search(email)
            
            if check:
                break
            else: print("'@'를 포함하세요")

        while True:
            birth = input("생년월일을 4자리로 입력해주세요 ")
            if len(birth) == 4:
                break
            
        customer= {"Gender" : gender, "Email" : email, "Birthday": birth}
        custlist.append(customer)
        # 그리고 page 값 바꾸기
        page +=1
        
    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >=0:
            print(custlist[page])
            print(f"현재 페이지는 {page+1}입니다")
        else: print("입력된 정보가 없습니다")
        
    elif choice == 'P':
        print("이전 고객 정보 조회")
        
        if page <=0:
            print("첫번째 페이지 입니다.")
            print(custlist[page])
        else: 
            page -=1   # 이러면 3페이지 까지 있었는데 1페이지로 만들고 새로 추가하면 덮어쓰기되는뎅
            print(f"현재 페이지는 {page+1}입니다")
            print(custlist[page])
        
    elif choice == 'N':
        print("다음 고객 정보 조회")
        
        if page >=len(custlist)-1:
            print("마지막 페이지입니다.")
        else:
            page += 1
            print(f"현재페이지는 ")
            print(custlist[page+1])
        
    elif choice=='D':
        print("고객 정보 삭제")
        delok =0
        del_email = input("삭제할 이메일 주소를 입력해주세요 ")
        for a in range(len(custlist)):
            if del_email ==custlist[a]['Email']:
                del custlist[a]
                delok =1
        if delok == 0:  # for문을 돌리고도 찾지 못했을 경우가 0
            print("등록되지 않은 정보입니다.")
    elif choice=="U": 
        print("고객 정보 수정")
        idx = -1 # 기본값
        new_email = input("수정할 이메일 주소를 입력해주세요")
        for a in range(len(custlist)):
            if new_email == custlist[a]['Email']:
                idx = a
        if idx ==-1:
            print("등록되지 않은 정보입니다.") # 하고 다시받아야함? ㄴㄴ
        else:  # 이메일 다시 받기
            while True:
                email = input("이메일을 입력해주세요")
                conf =re.search('@',email)

                if conf:
                    break
                else: print("'@'를 포함하세요")
            # 그외에 수정할 정보 선택하기
            while True:
                choice=input('''
                그 외에 수정할 정보를 선택해 주세요 :
                G : 성별 수정
                B : 생년월일 수정
                Exit : 프로그램 종료
                ''')  
                
                if choice=="G": 
                    
                    while True:
                        gender = input("성별을 입력하시오. M / F ").upper()
                        
                        if gender == "M" or gender == "F":
                            break
                        else: print("다시 입력하세요")
                        
                        custlist[a]['Gender']=gender
                    
                elif choice=="B": 
                    
                    while True:
                        birth = input("생년월일 4자리를 입력하세요 ")
                        
                        if len(birth) == 4:
                            break
                        else: print("다시 입력하세요")
                        
                elif choice=="exit": 
                    print("수정창 종료")
                    break
        
    elif choice=="Q":
        print("프로그램 종료")
        break
