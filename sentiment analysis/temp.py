import re


text = '\"hist\"ahita.aa...'
print('before: ', text)
text = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'》]', "", text)
print([v for v in text.split('.') if v])
print("after : ", text)