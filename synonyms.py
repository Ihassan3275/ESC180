'''Semantic Similarity: starter code
Author: Michael Guerzhoy, Ibrahim Hassan. Last modified: Dec. 08, 2021.
'''

import math

# ===========================================================================
def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

# ===========================================================================
def cosine_similarity(vec1, vec2):
    top = 0
    vec1_keys = list(vec1.keys())
    vec1_values = list(vec1.values())
    vec2_keys = list(vec2.keys())
    vec2_values = list(vec2.values())
    for i in range(len(vec1_keys)):
        for j in range(len(vec2_keys)):
            if vec1_keys[i] == vec2_keys[j]:
                top += vec1_values[i] * vec2_values[j]
                denominator = norm(vec1) * norm(vec2)
    return float(top/ denominator)

#
# #
#     upper=0.0
#     for keys in vec1:
#         if keys in vec2:
#             upper += vec1[keys]*vec2[keys]
#     return upper / (norm(vec1)*norm(vec2))
#         # else:
#         #     return upper
# #
#
#
#
#     # intersection = set(vec1.keys()) & set(vec2.keys())
#     # for x in intersection:
#     #    numerator = sum([vec1[x] * vec2[x]])
#     # num = 0.0
#     #
#     # sum1 = sum([vec1[x]**2 for x in vec1.keys()])
#     # sum2 = sum([vec2[x]**2 for x in vec2.keys()])
#     # denominator = math.sqrt(sum1) * math.sqrt(sum2)
#     #
#     # if denominator:
#     #   return float(numerator) / denominator
#     # else:
#     #    return num
#
# # ===========================================================================
# def build_semantic_descriptors(sentences):
#     pass
#
#
#
# # f = open("demofile.txt", "r")
# # print(f.read())
# #
# # # def build_semantic_descriptors_from_files(filenames):
# #     # text = " "
# #     #
# #     # for i in range(len(filenames)):
# #     #     text = open(filenames[i], "r", encoding="latin1").
# #     #     text.read()
# #     #     text = " "
# #     #
# #     # text = text.replace(",", " ")
# #     # text = text.replace("-", " ")
# #     # text = text.replace("--", " ")
# #     # text = text.replace("!", ".")
# #     # text = text.replace(":", " ")
# #     # text = text.replace(";", " ")
# #     # text = text.replace("?", ".")
# #     # text = text.replace("\n", " ")
# #     #
# #     # text = text.split(".")
# #     #
# #     # final_out = []
# #     # for i in range(len(text) - 1):
# #     #     final_out.append(text[i].split(" "))
# #     #
# #     #
# #     # for i in final_out:
# #     #     for j in i:
# #     #         while ''in i:
# #     #             i.remove('')
# #     #
# #     # return build_semantic_descriptors(final_out)
#
#
# # ===========================================================================
# def build_semantic_descriptors_from_files(filenames):
#     s = []
#
#     for i in range(len(filenames)):
#         text = open(filenames[i], "r", encoding="latin1").
#         text.read()
#
#     for file in filenames:
#         list = []
#         f = open(filenames[i], "r", encoding="latin1")
#         f = f.read()
#     f_split = f.split(".")
#     f_split = f.split("!")
#     f_split = f.split("?")
#     text = text.replace(",", " ")
#     text = text.replace("-", " ")
#     text = text.replace("--", " ")
#     text = text.replace(":", " ")
#     text = text.replace(";", " ")
#     text = text.replace("\n", " ")
#         for item in f_split:
#            list.append(item.split())
#         s += list
#     return build_semantic_descriptors(s)
#
#
# # ===========================================================================
# def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
#     pass
#
#     """Out of the choices, returns the choice that returns the greatest
#     cos similarity. Otherwise return -1 if similarity cannot be computed."""
#     similarities = {}
#     for choice in choices:
#         if choice in list(semantic_descriptors.keys()):
#             cos_sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
#             similarities[choice] = cos_sim
#         else:
#             similarities[choice] = -1
#     #print(similarities)
#     return max(similarities, key=similarities.get)
#
#  # =========
#
#     output = choices[0]
#     max = 0
#     word = word.lower()
#     for i in range (len(choices)):
#         choices[i] = choices[i].lower()
#     if word not in semantic_descriptors:
#         return output
#     for a in range (len(choices)):
#
#         if choices[a] not in semantic_descriptors:
#             similarity = -1
#         else:
#
#             similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[a]])
#         if a == 0:
#             max = similarity
#         if similarity > max:
#             max = similarity
#             output = choices[a]
#     return output
#
#
#
# # ===========================================================================
# def run_similarity_test(filename, semantic_descriptors, similarity_fn):
#     list = []
#     f = open(filename, "r", encoding="latin1").read()
#
#
# # # #     new_f = open(filename, "r")
# #     f = new_f.read()
# #     lines = f.split('\n')
# #     n_correct = 0
# #     n_total = 0
# #     for v in range(len(lines)):
# #         line = lines[v].split(' ')
# #         #print (line)
# #         choices = line[2:]
# #         if line == ['']:
# #             continue
# #         w_guess = most_similar_word(line[0], choices, semantic_descriptors, cosine_similarity)
# #         #print (line[1] + '        ' + str(w_guess))
# #         if w_guess == line[1]:
# #             n_correct += 1
# #         n_total += 1
# #     return (n_correct/n_total) * 100
#
#
#     # correct_counter = 0.0
#     # f = open(filename, "r", encoding="latin1").read()
#     # f = f.casefold()
#     # f = f.split("\n")
#     # list = []
#     # for item in f:
#     #     if item != "":
#     #
#     #        list.append(item.split())
#     # for testing in list:
#     #     if most_similar_word(testing[0], testing[2:], semantic_descriptors, similarity_fn) == testing[1]:
#     #         correct_counter += 1
#     #
#     # return correct_counter/len(list)*100