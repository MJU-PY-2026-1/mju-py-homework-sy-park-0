# 파일이름 : 캠퍼스 커리어 플래너  
# 작 성 자 :60211865 박성연   

print("============캠퍼스 커리어 플래너==============")

user_name = input("이름 입력 : ")
task_name = input("할일 이름 : ")

print("\n분야 선택")
print("1. 학교공부")
print("2. 연구")
print("3. 취업")
print("4. 자격증")
category_num = int(input("번호 입력 : "))

days_left = int(input("마감까지 남은 일수 : "))
importance = int(input("중요도(1~5) 입력 : "))
study_hours = int(input("예상소요시간 : "))

if category_num == 1 :
  category = "학교공부"
elif category_num == 2 :
  category = "연구"
elif category_num == 3 :
  category = "취업"
elif category_num == 4 :
  category = "자격증"
else :
  category = "잘못입력"

task_info = [user_name, task_name, category, days_left, importance, study_hours]

if category == "잘못입력" or importance <1 or importance > 5 or days_left < 0 or study_hours < 0 :
  print("\n입력값이 올바르지 않음")
  print("분야번호, 중요도, 남은일수, 예상소요시간을 다시 확인")

else :
  urgency_score = (importance * 10) + (study_hours * 2) - days_left

  if urgency_score >= 50 :
    grade = "S"
  elif urgency_score >= 40 :
    grade = "A"
  elif urgency_score >= 30 :
    grade = "B"
  elif urgency_score >= 20 :
    grade = "C"
  else :
    grade = "D"

  if (category == "취업" and days_left <= 3 and importance >= 4) or (category == "연구" and importance == 5) :
    special_title = "최우선 집중 일정"
  elif category == "자격증" and (days_left <= 7 or study_hours >= 5):
    special_title = "단기 관리 필요 일정"
  elif category == "학교공부" and importance >= 4 and study_hours >= 4 :
    special_title = "학습 집중 일정"
  else :
    special_title = "일반 일정"

  if grade == "S" or grade == "A" :
    if category == "취업" :
      message = "가장 먼저 확인해야 할 채용/인턴 일정"
    elif category == "연구" :
      message = "연구 우선순위가 매우 높음"
    elif category == "학교공부" :
      message = "이번 학업 일정은 최우선으로 처리해야함"
    else :
      message = "자격증 준비를 빠르게 진행"
  else :
    if days_left <= 3 :
      message = "등급은 높지 않지만 마감이 가까우니 주의"
    else :
      message = "계획적으로 진행하면 되는 일정"


print("\n========입력한 일정 정보===========")
print(f"이름 : {task_info[0]}")
print(f"할일 : {task_info[1]}")
print(f"분야 : {task_info[2]}")
print(f"남은기한 : {task_info[3]}일")
print(f"중요도 : {task_info[4]}")
print(f"예상소요시간 : {task_info[5]}시간")
print("\n========분석 결과===========")
print(f"긴급도 점수 : {urgency_score}")
print(f"우선순위 등급 : {grade}")
print(f"특별 분류 : {special_title}")
print(f"안내 메세지 : {message}")
