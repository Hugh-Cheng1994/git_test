from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = '24079464'
API_KEY = 'FjhGVRyMOuIjmv2m2pBo6Smc'
SECRET_KEY = 'cI6PTW9TgPuMVs4PjBG50gzT7heyutr1'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()