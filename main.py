# 파일이름 : 캠퍼스 커리어 플래너  
# 작 성 자 :60211865 박성연   

task_list = []

def show_menu():
  print("캠퍼스 커리어 플래너 v3.0")
  print("1. 일정 입력")
  print("2. 저장된 일정 조회")
  print("3. 긴급도 분석")
  print("4. 종료")

def calculate_urgency(importance, hours, days_left):
  urgency_score = (importance * 10) + (hours * 2) - days_left
  return urgency_score

def decide_grade(score):
  if score >= 50 :
    grade = "S"
  elif score >= 40 :
    grade = "A"
  elif score >= 30:
    grade = "B"
  elif score >= 20 :
    grade = "C"
  else:
    grade = "D"
  return grade

def add_task():
  global task_list
  
  print("\n[일정 입력]")
  user_name = input("이름 입력: ")
  task_name = input("할 일 입력: ")
  print("\n분야 선택")
  print("1. 학교공부")
  print("2. 연구")
  print("3. 취업")
  print("4. 자격증")
  category_num = int(input("번호 입력: "))
  
  if category_num == 1 :
    category = "학교공부"
  elif category_num == 2:
    category = "연구"
  elif category_num == 3:
    category = "취업"
  elif category_num == 4:
    category = "자격증"
  else :
    category = "잘못입력"
    
  days_left = int(input("마감까지 남은 일수 입력: "))
  importance = int(input("중요도(1~5)를 입력: "))
  hours = float(input("예상 소요 시간을 입력: "))
  score = calculate_urgency(importance, hours, days_left)
  grade = decide_grade(score)
  task = [user_name, task_name, category, days_left, importance, hours, score, grade]
  task_list.append(task)
  print("\n일정 저장 완료")

def show_task():
  print("\n[저장된 일정 조회]")
  
  if len(task_list) == 0:
    print("저장된 일정 없음")
  else:
    task = task_list[-1]
    
    print(f"이름: {task[0]}")
    print(f"할일: {task[1]}")
    print(f"분야: {task[2]}")
    print(f"남은 기한: {task[3]}일")
    print(f"중요도: {task[4]}")
    print(f"예상소요시간: {task[5]:.1f}시간")

def analyze_task(task):
  print("\n[긴급도 분석]")
  
  if len(task)==0:
    print("분석할 일정 없음")
  else:
    last_task = task[-1]
    category = last_task[2]
    days_left = last_task[3]
    importance = last_task[4]
    hours = last_task[5]
    score = last_task[6]
    grade = last_task[7]
    if (category == "취업" and days_left <= 3 and importance >= 4 ) or (category == "연구" and importnace == 5):
      special_title = "최우선 집중 일정"
    elif category == "자격증" and (days_left <= 7 or hours >= 5):
      special_title = "단기 관리 필요 일정"
    elif category == "학교공부" and importnace >= 4 and hours >= 4:
      special_title = "학습 집중 일정"
    else:
      special_title = "일반 일정"
      
    if grade == "S" or grade == "A":
      if category == "취업":
        message = "가장먼저 확인해야 할 채용/인턴 일정"
      elif category == "연구":
        message = "연구 우선순위가 매우 높음"
      elif category == "학교공부":
        message = "학업 일정을 우선적으로 처리해야 함"
      else:
        message = "자격증 준비를 진행"
    else:
      if days_left <= 3:
        message = "등급은 높지 않지만 마감이 가까우니 주의 필요")
      else:
        message = "계획적으로 진행하면 되는 일정")
        
    print(f"긴급도 점수: {score:.1f}")
    print(f"우선순위 등급: {grade}")
    print(f"특별 분류: {special_title}")
    print(f"안내 메세지: {message}")

while True:
  show_menu()
  choice = input("메뉴를 선택: ")
  
  if choice =="1":
    add_task()
  elif choice == "2":
    show_task()
  elif choice == "3":
    analyze_task(task_list)
  elif choice == "4":
    print("프로그램 종료")
    break
  else:
    print("잘못된 메뉴. 다시 선택")
