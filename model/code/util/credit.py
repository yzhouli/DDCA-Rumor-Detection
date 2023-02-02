from tqdm import tqdm


class credit(object):

    @staticmethod
    def build_db_credit_att(topic_li, level_snap, a):
        """
        Calculating list of element credibility.
        :param topic_li: topic list
        :param level_snap: Number of fans level interval
        :param a: Attenuation factor
        :return: Reputation list
        """
        result_li = []
        desc = 'process credit att'
        for sentence_li in tqdm(topic_li, desc=desc):
            temp_li = dict()
            for index, item in enumerate(sentence_li):
                author, fans_num = item['author'], item['fans']
                credit_att = credit.to_level(author=author, fans_num=fans_num, level_snap=level_snap, a=a)
                temp_li[index] = credit_att
            result_li.append(temp_li)
        return result_li


    @staticmethod
    def to_level(author, fans_num, level_snap, a):
        """
        Calculating element credibility.
        :param author: Official level
        :param fans_num: Number of fans
        :param level_snap: Number of fans level interval
        :param a: Attenuation factor
        :return: Reputation of element
        """
        level = int(fans_num) // level_snap
        return int(author) + a * level

