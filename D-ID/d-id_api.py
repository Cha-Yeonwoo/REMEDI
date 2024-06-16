import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# 파일 다운로드
s3.download_file('d-id-projects-prod', 'google-oauth2|105896968890442581577/prj_7IsORMUF9xmyLCw71xyT-/result.mp4', 'result.mp4')
