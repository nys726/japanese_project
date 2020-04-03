'''
일본어 데이터 정제
오상혁 나윤수
2020.3.30 월 데이터 정제하는 코드
좋은 문장 선별
[한자로만 된 문장 제거]
문장에서 조사는 히라가나로만 작성됨
조사가 없는 문장은 비문일 확률이 높으므로
한자로만 되어있거나 가타카나로만 되어있는 문장 제거
[적절한 길이 이외 문장 제거]
너무 짧아서 문장 성분이 부족할거라 예상 되는 문장과
너무 길어서 사용 하기 힘든 문장 제거
'''
import re
def good(japanese_text, min=8, max=135):

    #한자로만 된 문장 제거
    sub_chinese_character= re.sub('\n[^あ-んア-ン]*\n','',japanese_text)
    #가타카나로만 되어있는 문장 제거
    sub_kata=re.sub('\n[ア-ンー]*\n','',sub_chinese_character)
    #적절한 길이 이외의 문장 제거
    sub_len_short = re.sub('\n.{0,min}\n', '', sub_kata)
    sub_len_long = re.sub('\n.{max,}', '', sub_len_short)

    return sub_len_long

