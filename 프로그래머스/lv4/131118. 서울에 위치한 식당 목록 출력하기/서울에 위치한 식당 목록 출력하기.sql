-- 코드를 입력하세요 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고
-- 균점수를 기준으로 내림차순 정렬 /평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬
SELECT I.REST_ID,REST_NAME,FOOD_TYPE, FAVORITES AS FAVORITES,ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO I, REST_REVIEW R
WHERE I.REST_ID = R.REST_ID 
GROUP BY R.REST_ID
HAVING ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC