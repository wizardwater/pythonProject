import re, pickle, json

def load_data():
    f = open('02_Customer/data.json','r')
    return json.load(f)

def save_data(custlist):
    f = open("02_customer/data.json","w")
    json.dump(custlist,f,indent=2)
    f.close()


def print_menu():
    print('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료 ''')

def gender_():
    while True:
        gender= input("성별을 입력해주세요 M / F").upper()

        if gender in ('M', 'F'):
            break
    return gender
def email_():
    regex = re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,10}.[a-z]{2,10}')
    while True:
        email = input("이메일을 입력해주세요 :")
        conf =regex.search(email)
        if conf:
            break
        else: print("'@'를 포함하여 이메일 형식으로 입력하세요")
    return email

def birth_():
    while True:
        birth = input("출생년도를 4자리로 입력해주세요 :")
        if len(birth) == 4:
            break
    return birth
    

def new_customer():  # 성별 /이메일/ 생일 받기
    gender = gender_()
    email = email_()
    birth = birth_()

    customer= {"Gender" : gender, "Email" : email, "Birthyear": birth}
    custlist.append(customer)
    
    

def customer_info(x):
    global page  # 전역변수를 변경하는 것임을 공표
    if page >=0:
        if x == 1:
            print("현재 고객 정보 조회")
        if x == 2:
            print("이전 고객 정보 조회")
            if page !=0:
                page -= 1 
        if x == 3:
            print("다음 고객 정보 조회")
            if page < len(custlist)-1:  # 고객3명일때 > 2 page =2
                page +=1
        print(custlist[page])
        print(f"현재 페이지는 {page+1} 입니다")

    else:
        print("아직 고객 정보가 없습니다")

def ex_amend(idx):
    while True:
        choice=input('''
            그 외에 수정할 정보를 선택해 주세요 :
            G : 성별 수정
            B : 출생년도 수정
            Exit : 프로그램 종료 ''').upper()
        
        if choice=="G":
            custlist[idx]['Gender']=gender_()
                    
        elif choice=="B":
            custlist[idx]['Birthyear']=birth_()
                        
        elif choice=="EXIT":
            print("수정창 종료")
            break

def amend_customer():
    idx = -1 
    print("고객 정보 수정")
    new_email = input("수정할 이메일 주소를 입력해주세요")
    for a in range(len(custlist)):
        if new_email == custlist[a]['Email']:
            idx = a
    if idx ==-1:
        print("등록되지 않은 정보입니다.") 
    else:
        email = email_()
        custlist[idx]['Email'] = email
        ex_amend(idx)


def del_customer():
    print("고객 정보 삭제")
    delok = 0
    del_email = input("정보 삭제를 위해서 이메일 주소를 입력해주세요 ") # 동일한 이메일 주소를 가진 고객정보 삭제
    for a in range(len(custlist)):
        if del_email ==custlist[a]['Email']:
            del custlist[a]
            delok = 1
    if delok == 0:  # for문을 돌리고도 찾지 못했을 경우가 0
        print("등록되지 않은 정보입니다.")
    elif delok ==1: # page 1번을 삭제 했을 경우 >> 남은 페이지가 없으므로 page = -1
        if a ==0:
            page = -1
        else: page = len(custlist) -1

# 계속 실행할 while 문
page = -1
custlist=load_data()
page = len(custlist)-1
cmd = 0
while cmd != 'Q':
    print_menu()
    cmd = input().upper()
    if cmd == 'I':
        new_customer()  # 성별 /이메일/ 생년월일 받기
        page =len(custlist)-1
        print(page)
    elif cmd == 'C':
        customer_info(1)
    elif cmd == 'P':
        customer_info(2)
    elif cmd == 'N':
        customer_info(3)
    elif cmd == 'U':
        amend_customer()
    elif cmd == 'D':
        del_customer()