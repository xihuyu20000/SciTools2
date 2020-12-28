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
    # select hasAll(['科学计量', '文献'],kws) from default.sci_dataset ob