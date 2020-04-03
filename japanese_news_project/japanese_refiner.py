'''
일본어 데이터 정제
오상혁 나윤수
2020.3.30 월
데이터 정제 메인 코드
[텍스트 파일명 입력]
정제할 텍스트 파일명을 입력
[통계데이터 표시]
문장 길이의 평균 값, 최대값 등
추세 그래프 생성
[샘플데이터의 량]
얻고싶은 샘플의 갯수 입력
[저장 위치 및 파일 명]
파일 이름 및 경로를 설정 할 수 있습니다

'''
import sys
import good_sentence as gs
import bad_sentence as bs
import preprocessing as pr
# import data_statistic as ds

if len(sys.argv)!=5:
    print('다섯 종류의 옵션을 입력해주세요')
    print('--------------------------------------------------------------------')
    print('argument : [파일 위치] [통계 데이터 종류] [샘플데이터의 양] [저장 위치 및 파일 명]')
    print('예) text.txt max 1000 fine_data.txt','\n')
    print('* 통계 데이터 종류 \n max(문장 길이 최대값 출력) \t mean(문장 길이 평균값) \n range(문장길이의 범위) \t all(전부출력)\n')
    print('* 샘플 데이터는 정제 데이터와 같은 경로에 저장 됩니다')
    print('---------------------------------------------------------------------')

    exit()
    # raise ValueError
file=sys.argv[1]
option=sys.argv[2]
sample_num=sys.argv[3]
text_name=sys.argv[4]
sample_text_name='sample_'+text_name
# 중간 log 기록
text=open(file,'r',encoding='utf-8')
text_str=''.join(text)
preprocess=pr.prepro(text_str)

bad_sentence_file=bs.bad(preprocess)

good_sentence_file= gs.good(bad_sentence_file)

text_sort=good_sentence_file.split('\n')
text_sort_len=text_sort.sort(key=len)
str_len='\n'.join(text_sort)
# ds.statistic_data(text_str,option)
write_text=open(text_name,'w',encoding='utf-8')
write_text.write(str_len)
print('완료')


# write_sample=open(sample_text_name,'w',encoding='utf-8')
# write_sample.write(ds.sample(str_len,sample_num))


# sample 옵션으로


