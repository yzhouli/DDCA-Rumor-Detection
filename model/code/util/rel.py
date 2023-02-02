import difflib


class relation(object):

    @staticmethod
    def build_rel_item_weight(context_li, sentence, weight_value, start_index):
        """
        Calculate the weight of relationship elements
        :param context_li: Text list of other elements in the topic field
        :param sentence: Text of current element
        :param weight_value: Minimum value for establishing relationship
        :param start_index: Just to reduce the amount of computation
        :return: the weight of relationship elements
        """
        result = []
        if start_index >= len(context_li):
            return result
        for index in range(start_index, len(context_li)):
            weight = difflib.SequenceMatcher(None, context_li[index], sentence).quick_ratio()
            if weight > weight_value:
                result.append((index, weight))
        return result
