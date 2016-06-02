
import json

from gensim import corpora, models, similarities


def print_similaries(model, corpus, zip_data, index):

    def get_sim(vec, threshold=0.1):
        sims = index[model[vec]]
        lsims = list(enumerate(sims))
        return filter(lambda x: x[1] > threshold, sorted(lsims, key=lambda tup:tup[1], reverse=True))

    def get_similar_data(idx, vec, threshold=0.25):
        sim_vec = get_sim(vec, threshold)
        # sim_data = map(lambda x: [','.join(zip_data[x[0]][2]), x[1]], sim_vec)
        # sim_data = map(lambda x: {"title": zip_data[x[0]][0], "score": float(x[1])}, sim_vec)
        sim_data = map(lambda x: "%.2f" % float(x[1]) + "|" + zip_data[x[0]][0], sim_vec)
        # original_data = 'xxxx|' + zip_data[idx][0]
        return sim_data[:4]

    print('----------------------')
    print('calculate similaries..')
    print('----------------------')
    # print(get_sim(vec))

    dx = {}
    good_sim = 0
    bad_sim = 0
    for idx, c in enumerate(corpus[:200]):
        sim_data = get_similar_data(idx, c)

        if len(sim_data) <= 1:
            # print('---')
            bad_sim += 1
            continue

        good_sim += 1
        dx[idx] = sim_data
        # p.pprint(sim_data)
        print(json.dumps(sim_data, ensure_ascii=False, indent=4,
                     sort_keys=False, separators=(',', ':')))

    print('good_sim: ' + str(good_sim))
    print('bad_sim: ' + str(bad_sim))