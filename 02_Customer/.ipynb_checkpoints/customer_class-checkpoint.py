import re

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

class UserInfo:
    def __init__(self):
        self.gender = self.get_gender()
        self.email = self.get_email()
        self.birth = self.get_birth()
        self.customer= {"Gender" : self.gender, "Email" : self.email, "Birthday": self.birth}
        custlist.append(customer) 
        
    def get_gender(self):
        while True:
            gender= input("성별을 입력해주세요 M / F").upper()

            if gender in ('M', 'F'):
                break
        return gender
    def get_email(self):
        while True:
            email = input("이메일을 입력해주세요")
            conf =re.search('@',email)

            if conf:
                break
            else: print("'@'를 포함하세요")
        return email

    def get_birth(self):
        while True:
            birth = input("생일을 4자리로 입력해주세요")
            if len(birth) == 4:
                break
        return birth
    
    

    


def customer_info(x):   # 현재 고객 -> 마지막 고객을 보여줌. 그럼 다음 고객 정보는 의미없는거아냐?
    if page >=0:
        if x == 1:
            print("현재 고객 정보 조회")
            print(custlist[page])
            print(f"현재 페이지는 {page+1} 입니다")
        if x == 2:
            print("이전 고객 정보 조회")
            if page == 0:
                print(custlist[page])
            else: print(custlist[page-1])
        if x == 3:
            print("다음 고객 정보 조회")
            apa = 0
            if page == page:
                apa = -1
            print(custlist[page+1+apa])

    else : print("아직 고객 정보가 없습니다")

def ex_amend():
    while True:
        choice=input('''
            그 외에 수정할 정보를 선택해 주세요 :
            G : 성별 수정
            B : 생년월일 수정
            Exit : 프로그램 종료 ''').upper()
        
        if choice=="G":
            custlist[idx]['Gender']=gender_()
                    
        elif choice=="B":
            custlist[idx]['Birthday']=birth_()
                        
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
        ex_amend()


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
custlist = []
cmd = 0
while cmd != 'Q':
    print_menu()
    cmd = input().upper()
    if cmd == 'I':
        user_info= UserInfo()
        page += 1
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