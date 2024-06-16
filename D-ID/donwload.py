import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# 파일 다운로드
s3.download_file('d-id-talks-prod', 'google-oauth2|105896968890442581577/tlk_BySmwyIMLTtMckG84Udgl/1717222180713.mp4', 'local_filename.mp4')
