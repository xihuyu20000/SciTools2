# 判断是否是纯中文
def is_all_chinese(strs):
    for i in strs:
        if not '\u4e00' <= i <= '\u9fa5':
            return False
    return True


# 判断是否是纯英文
def is_all_eng(strs):
    import string
    for i in strs:
        if i not in string.ascii_lowercase + string.ascii_uppercase:
            return False
    return True


# 判断字符串是英文还是中文
def strings_is_eng(strings):
    words = [word for word in strings if word!='[' and word!=']' and word!='.' and word!=',' and word!='(' and word!=')' and word.strip()]
    words_cn = len([word for word in words if is_all_chinese(word)])
    words_en = len([word for word in words if is_all_eng(word)])
    return True if words_cn<words_en else False
