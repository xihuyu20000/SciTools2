from api import util, config, dao
from api.util import CutWords


def cut_words(df):
    """
    针对title和summary切词，填充title_words和summary_words两个字段
    """
    stopwords = util.stopwords()
    cutwords = CutWords(config.user_cut_dict_path)
    for index, row in df.iterrows():
        title_words = cutwords.cut_words(row['title'], stopwords=stopwords)
        summary_words = cutwords.cut_words(row['summary'], stopwords=stopwords)
        dao.updateOdsData(row['id'], {'title_words': title_words, 'summary_words': summary_words})


def co_keywords(df):
    """
    共词矩阵
    """
    words = []
    for w in df['kws']:
        words.extend(w)

    for w1 in words[:30]:
        for w2 in words[:30]:
            print(w1, w2)
    # select hasAll(['科学计量', '文献'],kws) from default.ods_bib ob